.PHONY: tests

# current git branch
BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

# Pin versions known to work together
PINNED_PIP      := 25.2
PINNED_PIPTOOLS := 7.5.1

init::
	# Tooling (pin pip to avoid CI drift)
	python -m pip install --upgrade "pip==$(PINNED_PIP)" "setuptools>=68" "wheel>=0.42" "build>=1.0.0"
	python -m pip install "pip-tools==$(PINNED_PIPTOOLS)"

	# Compile from .in to .txt (use backtracking resolver for consistency)
	python -m piptools compile --resolver=backtracking requirements/requirements.in
	python -m piptools compile --resolver=backtracking requirements/dev-requirements.in

	# Sync the environment to the compiled lock files
	python -m piptools sync requirements/dev-requirements.txt requirements/requirements.txt

tests:
	pytest -q

