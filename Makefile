up: docker-up
down: docker-down
reset: down up
hardreset: down docker-up-build

mainpy: docker-run-main-py

docker-up:
	docker-compose up -d devmanweb

docker-up-build:
	docker-compose up --build -d devmanweb

docker-down:
	docker-compose down -v --remove-orphans

docker-run-main-py:
	docker-compose run devmanweb python main.py

