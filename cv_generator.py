#! /usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import sys

from jinja2 import Environment, FileSystemLoader

from libs.helpers.date import yymmdd_to_date
from libs.helpers.load_yaml import load_yaml
from libs.helpers.project_checker import check_project_consistency
from libs.helpers.text_utils import slugifier
from libs.processors import (
    formation,
    interests,
    languages,
    personal_info,
    tagline,
    technical_skills,
    xp,
)
from libs.services import i18n

JOB_AD_FILENAME = "job_ad.yml"


def generate(name: str):
    check_project_consistency(name)

    job_ad = load_yaml(name, JOB_AD_FILENAME)

    print("args", args)

    locale = args.lang or (job_ad and job_ad.get("locale")) or os.environ["LANG"]

    locale = locale.split(".")[0].split("_")
    lang = locale[0]
    zone = (
        os.environ["LANG"].split(".")[0].split("_")[1]
        if len(locale) < 2
        else locale[1].upper()
    )

    i18n.set_language(lang)
    i18n.set_zone(zone)

    print(f">> Generation for lang: '{lang}', zone: '{zone}'")

    _ = i18n.get_translator()

    env = Environment(loader=FileSystemLoader(os.path.join(name, "template")))
    template = env.get_template("template.html")
    # template = env.get_template("head_left_right.html")
    out_html = template.render(
        personal_info=personal_info.map(project=name),
        technical_skills=technical_skills.map(name),
        tagline=tagline.map(name),
        formation=formation.map(name),
        languages=languages.map(name),
        contact_title=_("contact"),
        interests=interests.map(name),
        xp=xp.map(name),
    )

    outfile = get_outfilename(name)

    if not os.path.exists(os.path.join(os.getcwd(), name, "out")):
        os.mkdir(os.path.join(os.getcwd(), name, "out"))

    outpath = os.path.join(os.getcwd(), name, "out", outfile + ".html")

    with open(outpath, "w") as f:
        f.write(out_html)

    print("Written to " + outpath)

    # personal_info_data = PersonalInfo(data=personal_info.load_file(name))

    # write on big html file


def create(name: str):
    output = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"], check=False, capture_output=True
    )

    if output.stderr or (
        output.stdout and output.stdout.decode("utf-8").strip() != "true"
    ):
        raise OSError("Not a git repository")

    job_ad = load_jobad(name)

    company_slug = slugifier(job_ad.get("company"))
    title_slug = slugifier(job_ad.get("title"))
    location_slug = slugifier(job_ad.get("location"))

    branch_name = f"{company_slug}__{title_slug}__{location_slug}"

    print("Nom de la branche : " + branch_name)
    user_input = input("Créer la branche ? (o/N)").lower() or "n"

    if user_input == "n":
        return

    print("Création de la branche")
    subprocess.run(
        ["git", "checkout", "-b", branch_name], check=False, capture_output=True
    )


def init(name: str):
    new_cv_path = os.path.join(os.getcwd(), name)

    if os.path.exists(new_cv_path):
        print(f"Le fichier ou le répertoire {name} existe déjà !")
        sys.exit(1)

    os.mkdir(name)

    subprocess.run(["git", "init"], cwd=name, check=False)

    resources_path = os.path.join(os.getcwd(), "resources")

    for file in [
        os.path.join("cv_project_build", "makefile"),
        os.path.join("cv_project_build", "env.mk"),
        "job_ad.yml",
        "README.md",
    ]:
        shutil.copy(os.path.join(resources_path, file), new_cv_path)

    os.mkdir(os.path.join(new_cv_path, 'out'))

    shutil.copy(
        os.path.join(resources_path, "gitignore"),
        os.path.join(new_cv_path, ".gitignore"),
    )

    shutil.copytree(os.path.join(os.getcwd(), 'resources', 'cv_sample'), new_cv_path, dirs_exist_ok=True)

#     out_html = f"""
#     {personal_info.map(pi=personal_info_data)}
#     {tagline.process(name)}
#     {technical_skills.process(name)}
#     {business_skills.process(name)}
#     <div id="fli-wrapper">
#         {formation.process(name)}
#         <div>
#         {languages.process(name)}
#         {interests.process(name)}
#         </div>
#     </div>
#     {set_doc_heading(personal_info_data)}
#     {highlights.process(name)}
#     {xp.process(name)}
#     </body>
# </html>
# """

# with open(os.path.join(os.getcwd(), name, "out.html"), "w") as f:
#     f.write(out_html)
#


def load_jobad(name: str):
    job_ad = load_yaml(name, JOB_AD_FILENAME)
    if job_ad == None:
        raise FileNotFoundError(JOB_AD_FILENAME)

    missing_keys = [
        key for key in ["company", "title", "location"] if job_ad.get(key) == None
    ]
    if missing_keys:
        raise ValueError("Missing key(s): " + ", ".join([key for key in missing_keys]))

    return job_ad


def get_outfilename(name: str):
    job_ad = load_jobad(name)
    company_slug = slugifier(job_ad.get("company"), lower=False)
    title_slug = slugifier(job_ad.get("title"), lower=False)
    location_slug = slugifier(job_ad.get("location"), lower=False)
    out = f"CV__{company_slug}__{title_slug}__{location_slug}"
    publish_date = yymmdd_to_date(job_ad.get("publish_date"))
    if publish_date:
        out += f"__{publish_date}"
    return out


def process_args():
    parser = argparse.ArgumentParser(
        prog="cv_generator", description="Options de cv_generator"
    )

    parser.add_argument("-i", "--init", type=str, help="Init a new CV repository")

    parser.add_argument(
        "-n",
        "--new",
        type=str,
        help="create new project (ex: cv_general)",
        required=False,
    )

    parser.add_argument(
        "-g",
        "--generate",
        type=str,
        help="generate from project (ex: cv_general)",
        required=False,
    )

    parser.add_argument(
        "-l",
        "--lang",
        type=str,
        help="lang to use for generation, default to system one",
        required=False,
    )

    parser.add_argument(
        "--outfilename",
        type=str,
        help="display outfilename",
        required=False,
    )

    args = parser.parse_args()

    if len(vars(args)) == 0:
        parser.print_help()

    return args


if __name__ == "__main__":
    args = process_args()

    if args.generate is not None:
        print(f">> process Generation for {args.generate}")
        generate(args.generate)
        sys.exit()

    if args.new is not None:
        create(args.new)
        sys.exit()

    if args.init is not None:
        init(args.init)
        sys.exit()

    if args.outfilename is not None:
        print(get_outfilename(args.outfilename))
        sys.exit()
