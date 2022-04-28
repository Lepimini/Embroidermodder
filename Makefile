default: lint

lint:
	pylint src/embroidermodder

qa_tests:
	pylint src/embroidermodder -f json > triage.json
	python3 src/triage.py
	cd src
	python3 tests.py

install:
	python3 -m pip install embroidermodder

dev-install:
	python3 -m build
	python3 -m pip install -U dist/*.whl --force-reinstall

dev-run: dev-install run

run:
	python3 -m pip install libembroidery
	python3 -m embroidermodder

run-without-install:
	python3 -m pip install libembroidery
	cd src
	python3 -m embroidermodder

clean:
	rm -fr dist src/embroidermodder.egg-info rating.txt triage.json

button:
	python3 src/make_button.py

tests:
	# We don't know if the user has added the command to their
	# PATH variable, so give the address from HOME.
	timeout 10 ~/.local/bin/embroidermodder

