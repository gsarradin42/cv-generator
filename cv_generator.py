#! /usr/bin/env python3

import argparse
import os

from libs.helpers.project_checker import check_project_consistency
from libs.helpers.text_utils import indent_multiple_line
from libs.processors import (
    business_skills,
    formation,
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

    # write on big html file
    out_html = f"""
<html>
    <head>
        <meta charset="utf-8">
        <link href="cv.css" rel="stylesheet">
        <link href="cv.css" media="print" rel="stylesheet">
        <title>CV TODO</title>
        <meta name="description" content="My CV">
    </head>
    <body>
    {personal_info.process(name)}
    {tagline.process(name)}
    {technical_skills.process(name)}
    {business_skills.process(name)}
    <div id="fli-wrapper">
        {formation.process(name)}
        <div>
        {languages.process(name)}
        {interests.process(name)}
        </div>
    </div>
    {process_xp_list(name)}
    </body>
</html>
"""

    with open(os.path.join(os.getcwd(), name, "out.html"), "w") as f:
        f.write(out_html)


def process_xp_list(name):
    xp_dir = os.path.join(os.getcwd(), name, "XP")

    print("process XPs")

    listdir = filter(
        lambda f: os.path.isdir(os.path.join(xp_dir, f)), os.listdir(xp_dir)
    )

    return f"""
    <section id="xp">
        <h2>{_("xp_pro")}</h2>
    {indent_multiple_line("\n".join([xp.process(os.path.join(xp_dir, d)) for d in listdir]), 2)}
    </section>
    """


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
    lang = "fr"
    i18n.set_language(lang)
    _ = i18n.get_translator()

    args = process_args()

    if args.lang is None:
        lang = os.environ["LANG"]
        try:
            lang = lang.split(".")[0].split("_")[0]
        except Exception:
            lang = "en"
    else:
        lang = args.lang

    i18n.set_language(lang)

    if args.generate is not None:
        print(f">> process Generation for {args.generate}")
        generate(args.generate)
        exit()

    if args.new is not None:
        print("Create!")
        exit()
