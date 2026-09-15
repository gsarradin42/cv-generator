# CV Project
Congrats! this is your own CV Project!

Here are preexisting data that need to be change in order to match your informations.

## File structure
Every file you need is located at root level
  * `*.yml` and `XP/**/*.yml`: those files are data used for CV generation, data structured are quite self-explainatory
    > Note: Pro XP data are located in `XP/` directory, each experience is a subdirectory and will be used for generation in reverse alphabetic order
    > so if you want generator to take experiences in reverse chronological order hint is to name xp subdir name like `YYYYMM-XPNAME`
  * `template/`: directory that contains the template to construct the CV on generation with a css file, it's expressed in Jinja2 format, a user-friendly one.
  * `makefile`: contains recipes to generate CV (HTML, PDF) and other operations
    * `make new`: will create new git branch, branch name will be based on `job_ad.yml` infos
    * `make copy_assets`: copy necessary asset for generation (css, images, etc.)
    * `make all`: generate the PDF (from HTML generation)
    * `make html`: generate the HTML only
    * `make view`: view the PDF (generate the PDF first if none was generated)
    > Note: The name of the PDF and HTML results files will be automatically generated based on `job_ad.yml` infos
    > (e.g. `CV__The_Company__The_Position__The_City__<yyyy-mm-dd>`)
    * `make out/anyfile.pdf`: suppose you have a generated HTML `out/anyfile.html` (from a previous generation), so this command will generate the PDF from this file

## Mini-howto before new job advertisment application
1. Change `job_ad.yml` infos
2. `make new` to create a new branch
3. Change `*.yml` files content
4. `make all` or `make view` to generate PDF

Iterate 3 and 5 at every CV need for change.
