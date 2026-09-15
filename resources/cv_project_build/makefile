SHELL := /bin/bash

include ./env.mk

FILENAME := $(shell $(CV_GENERATOR) --outfilename .)

ASSETS_OUT = $(patsubst %,$(OUTDIR)/%,$(ASSETS))

HTML = $(OUTDIR)/$(FILENAME).html
TARGET = $(OUTDIR)/$(FILENAME).pdf

.PHONY: all new html copy_assets clean view
#.PHONY : mount_remote send

all: $(TARGET)

copy_assets: $(ASSETS_OUT)

new: copy_assets
	$(CV_GENERATOR) -n .

html: $(HTML)

view: $(TARGET)
	open $(TARGET) &>/dev/null

# mount_remote:
# 	gio mount $(REMOTE) 2>/dev/null || echo -n

# send: $(TARGET) mount_remote
# 	gio mkdir $(FOLLOWUP_REMOTE)/$(FILENAME) || echo -n
# 	gio copy $(JOB_AD) $(FOLLOWUP_REMOTE)/$(FILENAME)/$(FILENAME).yml

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
	rm -f $(HTML) $(TARGET)
