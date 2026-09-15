# CV Generator

Generate a CV to HTML format using data recorded through YAML files.

Weasyprint can be used to convert to PDF.
If document layout is a little bit complex (using columns), prefered using web browser's printing feature. (it's possible to do printing in headless mode through selenium)

Goal: have the control of CV data for versioning (with Git), easier to create / modify / insert new XP, easier to maintain several languages, fork it, backport it, tag it, etc.

Generate html
```sh
$ cv_generator.py -g my_cv/
```

## Recommended way to generate
I recommend you to create a new project CV with the generator: it will create new git project with sample data to generate CV.
It will also contain a `Makefile` in order to automate generation.

```sh
$ cv_generator.py -i my_cv_project
```

You can then derived your CV project for customisation (against a job ad for example)

Look at [this doc](resources/README.md) for further information

## CV structured data

CV data must be structured through YAML files. Each file represents a CV section.

### Main data
Main data are located in the root folder of a CV, each file handles language variant:

- `personal_info.yml` : full name, position title, nationality, years of xp, contact details
- `tagline.yml` : tagline paragraph for self introduction
- `technical_skills.yml` : table of technical skills group by theme
- `business_skills.yml` : table of business expertises group by theme
- `formation.yml` : formations with organization, year, content and languages with level
- `interests.yml` : center of interests

### XP data
Professional experiences are located in a "XP" named folder that contains as many subfolder as experiences, <start_date_as_MM.YYYY>-<short_title> (e.g. 2021-WorldCompany) and must contains files:

- `metadata.yml` : period, short title, it keywords, business domain (no language variant)
- `content_<lang>.yml` : title, summary, introduction, tasks (separated file for each language variant)

## Template
CV Generator use HTML template (by using Jinja2) to produce the desired output. It uses target folder template.

## Build project

```sh
$ make clean all
```
It compiles i18n files (`.mo` to `.po` located in **locales/[lang]/LC_MESSAGES**)


## Printing with browser in headless modes
TODO
