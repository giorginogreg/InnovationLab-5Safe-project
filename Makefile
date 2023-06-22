POETRY = poetry run
BLACK = $(POETRY) black
PY = $(POETRY) python
.PHONY: format
format:
	$(BLACK) --exclude=.venv --line-length=79 --target-version=py310 $$(find il_5safe tests -name '*.py')
run:
	$(PY) $(file)
