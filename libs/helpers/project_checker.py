import os
from pathlib import Path

from libs.helpers.directory_iterator import DirectoryIterator
from libs.services import i18n

root_files = {
    "business_skills": False,
    "formation": True,
    "interests": False,
    "personal_info": True,
    "tagline": False,
    "technical_skills": True,
}

xp_files = {"content": True, "metadata": True}


def check_project_consistency(name: str):
    path = os.path.join(os.getcwd(), name)
    print(f"project Path: {path}")

    if not os.path.exists(path) or not os.path.isdir(path):
        print(f"project {name} doesn't exist, create it first!")
        exit()

    for element, mandatory in root_files.items():
        file = os.path.join(path, element + ".yml")
        if mandatory and not os.path.exists(file):
            print(f"Mandatory '{element}' doesn't exists!")
            exit()

    lang = i18n.get_lang()

    path_xp_single = Path(os.path.join(path, "XP"))

    if path_xp_single.exists() and path_xp_single.is_dir():
        # dir_list = [el for el in path_xp.iterdir() if el.is_dir()]
        itPath = DirectoryIterator(path_xp_single)
        for element, mandatory in xp_files.items():
            if not itPath.has_next():
                break
            path_xp_single = next(itPath)

            if mandatory:
                file = (
                    path_xp_single.joinpath(f"{element}_{lang}.yml")
                    if element == "content"
                    else path_xp_single.joinpath(element + ".yml")
                )

                if not file.exists():
                    print(f"{file} is mandatory")
