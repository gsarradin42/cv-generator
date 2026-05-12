#! /usr/bin/env python3

import argparse
import os

from libs.helpers.project_checker import check_project_consistency
from libs.models.personal_info import PersonalInfo
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

    personal_info_data = PersonalInfo(data=personal_info.load_file(name))

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
    {personal_info.process(pi=personal_info_data)}
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
    {xp.process(name, personal_info_data)}
    </body>
</html>
"""

    with open(os.path.join(os.getcwd(), name, "out.html"), "w") as f:
        f.write(out_html)


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
