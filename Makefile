.PHONY: lint clean run-cardioid run-sun run-spiral

lint:
	.venv/bin/flake8 *.py
	.venv/bin/mypy *.py

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache

run-cardioid:
	.venv/bin/python cardioid_shape.py

run-sun:
	.venv/bin/python fiery_sun_burst_desing.py

run-spiral:
	.venv/bin/python Rainbow_spiral.py
