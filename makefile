PO_DIR = locales
MO_DIR = locales

PO_FILES := $(shell find $(PO_DIR) -name '*.po')
MO_FILES := $(patsubst %.po,%.mo,$(PO_FILES))

all: $(MO_FILES)

%.mo: %.po
	msgfmt $< -o $@

clean:
	find $(MO_DIR) -name '*.mo' -delete
