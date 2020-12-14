up: docker-up
down: docker-down
reset: down up
in: docker-inside
hardreset: down docker-up-build

mainpy: docker-run-main-py
terminal: docker-run-terminal-py

docker-up:
	docker-compose up -d devmanweb

docker-up-build:
	docker-compose up --build -d devmanweb

docker-down:
	docker-compose down -v --remove-orphans

docker-run-main-py:
	docker-compose run devmanweb python main.py

docker-run-terminal-py:
	docker-compose run devmanweb python terminal.py

docker-inside:
	docker exec -it devman-django-orm_devmanweb_1 bash

