build: snapshot install db

db:
	docker-compose build

snapshot:
	pip-compile

install:
	pip install -r requirements.txt

start:
	python3 main.py -v DEBUG input output

run: build up

up:
	docker-compose up

test:
	nosetests tests

style:
	python3 -m black .