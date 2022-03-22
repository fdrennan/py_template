snapshot:
	pip-compile

restore:
	pip install -r requirements.txt

run:
	docker-compose up