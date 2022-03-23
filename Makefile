build: snapshot install

snapshot:
	pip-compile

install:
	pip install -r requirements.txt

runlocal:
	python3 main.py -v DEBUG input

run:
	docker-compose up

test:
	nosetests tests

style:
	python3 -m black .