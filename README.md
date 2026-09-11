# CV Generator

Generate a CV to HTML format using data recorded through YAML files.

Weasyprint can be used to convert to PDF.
If document layout is a little bit complex (using columns), prefered using web browser's printing feature. (it's possible to do printing in headless mode through selenium)

Goal: have the control of CV data for versioning (with Git), easier to create / modify / insert new XP, easier to maintain several languages, fork it, backport it, tag it, etc.

Generate html
```sh
$ cv_generator.py -g my_cv/
```

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

## Create new CV version
> Prerequisite: your CV must be a git project (do a `git init`)

> **`tl;dr`**
> ```
> $ cd mycv/ && cv_generator -n .
> ```

You also need a `job_ad.yml` file at your project root.

`job_ad.yml` structure:
```yaml
company: The Big Enterprise
title: Tech Lead Java
location: Moon
locale: fr_FR # <lang>_<zone>
publish_date: 2026.09.08

content: |
  job description, may be in markdown
```
`locale` is not mandatory, fallback to `-l` switch or system env.

With this example it will create a new branch named `the_big_entreprise__tech_lead_java__moon`

## Generate CV with automatic filename

> Prerequisite: need a `job_ad.yml`

Use `cv_generator --outfilename my_cv/` to generate the name based on `job_ad.yml` data.

With the same example over, the filename will be: `The_Big_Entreprise__Tech_Lead_Java__Moon__2026-09-08`

Let's use a `makefile` in the cv project:

```makefile
include ./env.mk

FILENAME := $(shell $(CV_GENERATOR) --outfilename .)

ASSETS_OUT = $(patsubst %,$(OUTDIR)/%,$(ASSETS))

HTML = $(OUTDIR)/$(FILENAME).html
TARGET = $(OUTDIR)/$(FILENAME).pdf

.PHONY: all html copy_assets clean view

all: $(TARGET)

copy_assets: $(ASSETS_OUT)

html: $(HTML)

view: $(TARGET)
	open $(TARGET) &>/dev/null

$(ASSETS_OUT): $(ASSETS)
	cp $(ASSETS) $(OUTDIR)

# $< stands for source ressources (or *.html) while $@ stands for generated (*.pdf)
# $^ stands for source + generated
$(OUTDIR)/%.pdf: $(OUTDIR)/%.html
	$(PDF_DRIVER) $< $@

$(HTML): $(ASSETS_OUT)
	$(CV_GENERATOR) -g .

clean:
	rm -f $(HTML) $(TARGET)
```

## Build project

```sh
$ make clean all
```
It compiles i18n files (`.mo` to `.po` located in **locales/[lang]/LC_MESSAGES**)


## Printing with browser in headless modes
TODO
