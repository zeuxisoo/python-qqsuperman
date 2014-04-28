.PHONY: install test clean clean-pyc

all:
	@echo "make install"

install:
	virtualenv-2.7 --no-site-package venv
	source venv/bin/activate && pip install -r requirements.txt

test:
	py.test --username=YOUR_USERNAME --password=YOUR_PASSWORD tests

clean: clean-pyc

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
