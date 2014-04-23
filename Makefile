.PHONY: install test

all:
	@echo "make install"

install:
	virtualenv-2.7 --no-site-package venv
	source venv/bin/activate && pip install -r requirements.txt

test:
	py.test --username=YOUR_USERNAME --password=YOUR_PASSWORD tests
