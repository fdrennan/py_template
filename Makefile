snapshot:
	pip-compile

install:
	pip install -r requirements.txt

rebuild: snapshot install

run:
	docker-compose up

test:
	nosetests tests

style:
	python3 -m black .