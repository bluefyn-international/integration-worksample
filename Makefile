.phony: setup setup-dev lint

build:
	docker build . -t work-sample-diego

setup:
	pip install -r requirements.txt

setup-dev: build
	pip install -r requirements-dev.txt

lint:
	pycodestyle --show-source --show-pep8 job

docker-run:
	docker run -it work-sample-diego

run:
	PYTHONPATH=job python -m job
