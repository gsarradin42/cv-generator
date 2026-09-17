SHELL := /bin/bash

include ./env.mk

FILENAME := $(shell $(CV_GENERATOR) --outfilename .)

ASSETS_OUT = $(patsubst %,$(OUTDIR)/%,$(ASSETS))

#JOB_AD_OUT = $(patsubst %.yml,$(OUTDIR)/$(FILENAME).md)
JOB_AD_OUT = $(OUTDIR)/$(FILENAME).md

HTML = $(OUTDIR)/$(FILENAME).html
TARGET = $(OUTDIR)/$(FILENAME).pdf

.PHONY: all new html copy_assets clean view gen_ad
#.PHONY : mount_remote send

all: $(TARGET)

copy_assets: $(ASSETS_OUT)

new: copy_assets
	$(CV_GENERATOR) -n .

html: $(HTML)

view: $(TARGET)
	open $(TARGET) &>/dev/null

gen_ad: $(JOB_AD_OUT)

$(JOB_AD_OUT): $(JOB_AD)
	$(CV_GENERATOR) --jobad-gen . > $(JOB_AD_OUT)

# mount_remote:
# 	gio mount $(REMOTE) 2>/dev/null || echo -n

# send: $(TARGET) gen_ad mount_remote
# 	gio mkdir $(FOLLOWUP_REMOTE)/$(FILENAME) || echo -n
# 	gio copy $(JOB_AD_OUT) $(FOLLOWUP_REMOTE)/$(FILENAME)/$(FILENAME).yml

$(ASSETS_OUT): $(ASSETS)
	cp -r $(ASSETS) $(OUTDIR)

# $< stands for source ressources (or *.html) while $@ stands for generated (*.pdf)
# $^ stands for source + generated
$(OUTDIR)/%.pdf: $(OUTDIR)/%.html
	$(PDF_DRIVER) $< $@

$(HTML): $(ASSETS_OUT)
	$(CV_GENERATOR) -g .

# $(TARGET): $(HTML)
# 	$(PDF_DRIVER) $(HTML) $(TARGET)

clean:
	rm -f $(HTML) $(TARGET) $(JOB_AD_OUT)
