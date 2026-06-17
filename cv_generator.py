#! /usr/bin/env python3

import argparse
import os

from jinja2 import Environment, FileSystemLoader

from libs.helpers.project_checker import check_project_consistency
from libs.processors import (
    business_skills,
    formation,
    highlights,
    interests,
    languages,
    personal_info,
    tagline,
    technical_skills,
    xp,
)
from libs.services import i18n


def generate(name: str):
    check_project_consistency(name)

    _ = i18n.get_translator()

    env = Environment(loader=FileSystemLoader("cv_sample"))
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

    with open(os.path.join(os.getcwd(), name, "out.html"), "w") as f:
        f.write(out_html)

    # personal_info_data = PersonalInfo(data=personal_info.load_file(name))

    # write on big html file


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


def process_args():
    parser = argparse.ArgumentParser(
        prog="cv_generator", description="Options de cv_generator"
    )

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

    args = parser.parse_args()

    if len(vars(args)) == 0:
        parser.print_help()

    return args


if __name__ == "__main__":
    args = process_args()

    locale = os.environ["LANG"] if args.lang is None else args.lang

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

    if args.generate is not None:
        print(f">> process Generation for {args.generate}")
        generate(args.generate)
        exit()

    if args.new is not None:
        print("Create!")
        exit()
