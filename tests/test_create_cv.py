import os
import shutil
import subprocess
import unittest
from os import path

import cv_generator

test_outdir = path.join("tests", "out")
project_dir = path.join(test_outdir, "my_cv_project")


class TestCreateCVProject(unittest.TestCase):
    def setUp(self):
        if path.exists(test_outdir):
            raise SystemError(
                f"{test_outdir} already exists, it may contains sensitive data"
            )
        else:
            os.mkdir(test_outdir)

    def tearDown(self):
        print(f"Suppression récursive du répertoire {test_outdir}")
        shutil.rmtree(test_outdir)

    def test_create_project(self):
        cv_generator.init(project_dir)

        regular_files = [
            "makefile",
            "env.mk",
            "job_ad.yml",
            "README.md",
            ".gitignore",
            "business_skills.yml",
            "formation.yml",
            "highlights.yml",
            "interests.yml",
            "personal_info.yml",
            "tagline.yml",
            "technical_skills.yml",
        ]

        dir_files = [
            "template",
            "XP",
            ".git",
        ]

        for file in regular_files + dir_files:
            self.assertFileExists(path.join(project_dir, file))

        self.assertFileExists(path.join(project_dir, "template", "template.html"))

        self.assertFileExists(
            path.join(project_dir, "XP", "202101-SecureMind", "metadata.yml")
        )

        self.assertTrue(path.isdir(path.join(project_dir, ".git")))

    def test_create_cv(self):
        cv_generator.init(project_dir)

        genfilenames = [
            f"CV__The_Company__The_Position__The_City.{ext}" for ext in ["html", "pdf"]
        ]
        open(path.join(project_dir, "myphoto.jpg"), "a").close()
        open(path.join(project_dir, "cv.css"), "a").close()

        env_vars = "CV_GENERATOR='../../../cv_generator.py' PDF_DRIVER='touch' ASSETS='cv.css myphoto.jpg'"

        subprocess.run(
            f'cd {project_dir} && echo "o" | {env_vars} make new all',
            check=False,
            shell=True,
        )

        for f in ["cv.css", "myphoto.jpg", *genfilenames]:
            self.assertFileExists(path.join(project_dir, "out", f))

    def assertFileExists(self, file: str):
        self.assertTrue(path.exists(file), f"File {file} doesn't exist!")
