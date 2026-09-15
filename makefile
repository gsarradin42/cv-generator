PO_DIR = locales
MO_DIR = locales

PO_FILES := $(shell find $(PO_DIR) -name '*.po')
MO_FILES := $(patsubst %.po,%.mo,$(PO_FILES))

.PHONY: all clean test install

all: $(MO_FILES)

install:
	venv/bin/pip install -r requirements.txt

%.mo: %.po
	msgfmt $< -o $@

clean:
	find $(MO_DIR) -name '*.mo' -delete

test: all
	venv/bin/python -m unittest discover tests
