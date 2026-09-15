import os
import re
import shutil
import unittest
from argparse import Namespace
from os import path

import cv_generator

# from globals import BASE_DIR

test_outdir = path.join("tests", "out")
outfile = path.join(
    test_outdir,
    "cv_sample",
    "out",
    "CV__The_Company__The_Position__The_City.html",
)


class TestGenSample(unittest.TestCase):
    def setUp(self):
        cv_generator.args = Namespace(
            lang="fr_CH",
        )

        if path.exists(test_outdir):
            raise SystemError(
                f"{test_outdir} already exists, it may contains sensitive data"
            )
        else:
            os.mkdir(test_outdir)
            shutil.copytree(path.join("resources", "cv_sample"), path.join(test_outdir, "cv_sample"))

    def tearDown(self):
        print(f"Suppression récursive du répertoire {test_outdir}")
        shutil.rmtree(test_outdir)

    def test_sample(self):
        cv_generator.generate(path.join(test_outdir, "cv_sample"))
        print("generate cv_sample done.")

        self.assertTrue(os.path.exists(outfile), "")

        with open(outfile, "r", encoding="utf-8") as f:
            outcontent = f.read()

        assert_forid_exists = self.assertForAttributeExists("id", outcontent)
        assert_forclass_exists = self.assertForAttributeExists("class", outcontent)

        #### HEADER ####
        assert_forid_exists("fullname", "Jean AYMARE")
        assert_forid_exists("title", "Fullstack Engineer")
        assert_forid_exists("my-xp", "42 années d'expérience")
        assert_forid_exists("nationality", "nationalité française (permis Z)")
        assert_forid_exists("tel", "tél: +42 01 02 03 04")
        assert_forid_exists("mail", "mél: jeanaimar@maville.org")
        assert_forid_exists(
            "adress", "Rue des rosiers fleuris 42 — 424242 Maville (Monpays)"
        )

        #### TECHNICAL SKILLS ####
        assert_forid_exists("skills-title", "COMPÉTENCES TECHNIQUES")

        assert_forclass_exists("skill-title", ["Outils", "OS"])
        assert_forclass_exists(
            "skill-it-keywords",
            ["Metasploit, Burp Suite, Qualys", "Linux, MacOS, Windows"],
        )

        #### TRAINING ####
        assert_forclass_exists(
            "formation-subject", ["Data Engineer", "Master en Informatique"]
        )

        assert_forclass_exists(
            "organization",
            ["IT TRAINING ACADEMY", "Massachusetts Institute of Technology"],
        )

        assert_forclass_exists("formation-year", ["2025", "2005"])


        #### LANGUAGES ####
        assert_forid_exists("languages-title", "Langues")

        assert_forclass_exists("lang-name", ["FRANÇAIS", "ANGLAIS"])
        assert_forclass_exists("lang-level", ["Langue maternelle", "Courant"])


        #### INTERESTS ####
        assert_forid_exists("interests-title", "Centre d'Intérêts")
        assert_forid_exists("interests-content", "<p>Joueur de bridge à haut niveau")


        #### TAGLINE ####
        assert_forid_exists(
            "tagline-content",
            "<p>Expert en cybersécurité et ancien hacker éthique,",
            compare_start=True,
        )

        assert_forid_exists("tagline-info", "Références : disponible sur demande")

        #### XP ####
        assert_forclass_exists(
            "xp-company", ["SecureMind Technologies", "CyberShield Consulting"]
        )

        assert_forclass_exists("xp-business", ["Sécurité", "Cybersécurité"])

        assert_forclass_exists(
            "xp-position",
            [
                "Directeur des opérations de sécurité",
                "Consultant senior en cybersécurité",
            ],
            compare_start=True,
        )

        assert_forclass_exists("xp-period", ["depuis 01.2021", "06.2014 – 12.2020"])

        assert_forclass_exists(
            "intro-or-summary",
            ["<p>Pilotage de programmes", "<p>Intervention auprès d’entreprises"],
            compare_start=True,
        )

        assert_forclass_exists(
            "xp-tasks",
            ["<ul><li>Conception de scénarios", "<ul><li>Conducted social engineering"],
            compare_start=True,
        )

        assert_forclass_exists(
            "xp-it",
            [
                "KnowBe4",
                "Burp Suite",
                "OWASP ZAP",
                "Nmap",
                "Wireshark",
                "Kali Linux",
                "Metasploit",
                "Microsoft Sentinel",
                "Splunk",
                "Qualys",
                "ServiceNow",
                "CrowdStrike Falcon",
                "Nessus",
                "Tenable.io",
            ],
        )

    def assertForAttributeExists(self, attribute_name: str, outcontent: str):
        def assertExists(
            attribute_value: str, expected: str | list[str], compare_start=False
        ):
            res = re.findall(
                rf'{attribute_name}="{attribute_value}">\s*(.*?)\s*</',
                outcontent,
                re.DOTALL,
            )
            if type(expected) is str:
                value = re.sub(r"\s+", " ", res[0])
                if compare_start:
                    self.assertTrue(value.startswith(expected))
                else:
                    self.assertEqual(expected, value)
            else:
                self.assertEqual(len(expected), len(res))

                for i in range(len(res)):
                    value = re.sub(r"\n", "", res[i])
                    if compare_start:
                        self.assertTrue(
                            value.startswith(expected[i]),
                            f"{value} doesn't start with {expected[i]}",
                        )
                    else:
                        self.assertEqual((",").join(expected), (",".join(res)))

        return assertExists
