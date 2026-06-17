from libs.helpers.load_yaml import load_yaml
from libs.helpers.text_utils import category_list, indent_multiple_line
from libs.models.dto.technical_skills_dto import TechnicallSkillsDto
from libs.services import i18n


def map(project) -> TechnicallSkillsDto:
    _ = i18n.get_translator()

    data = load_file(project)

    title = i18n.get_data_keylang(data, "title")

    list = data.get("list")

    skill_list = category_list(list, "title", "it_keywords")

    return TechnicallSkillsDto(title, skill_list)


def load_file(project):
    return load_yaml(project, "technical_skills.yml")
