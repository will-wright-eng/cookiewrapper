#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Setup
.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))
.DEFAULT_GOAL := help

help: ## list make commands
	@echo ${MAKEFILE_LIST}
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

#* Commands
# https://jupyter-docker-stacks.readthedocs.io/en/latest/
run-nb: ## run jupyter notebook on port 10000
	@echo ""
	@echo "http://<hostname>:10000/?token=<token>"
	@echo "http://127.0.0.1:10000/lab"
	@echo ""
	docker run -it --rm -p 10000:8888 -v "${HOME}/repos/_tmp":/home/jovyan/work jupyter/datascience-notebook:85f615d5cafa

#* Cleaning
pycache-remove: ## pycache-remove
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

dsstore-remove: ## dsstore-remove
	find . | grep -E ".DS_Store" | xargs rm -rf

mypycache-remove: ## mypycache-remove
	find . | grep -E ".mypy_cache" | xargs rm -rf

ipynbcheckpoints-remove: ## ipynbcheckpoints-remove
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

pytestcache-remove: ## pytestcache-remove
	find . | grep -E ".pytest_cache" | xargs rm -rf

build-remove: ## build-remove
	rm -rf build/

lint: test check-codestyle mypy check-safety

cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove
