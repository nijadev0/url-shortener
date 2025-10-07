.PHONY: help build up down logs shell test clean restart

help:
	@echo "URL Shortener - Available Commands:"
	@echo ""
	@echo "  make build    - Build Docker containers"
	@echo "  make up       - Start the application"
	@echo "  make down     - Stop the application"
	@echo "  make logs     - View application logs"
	@echo "  make shell    - Open Django shell in container"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Stop and remove all containers and volumes"
	@echo "  make restart  - Restart the application"
	@echo ""

build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

logs:
	docker compose logs -f

shell:
	docker compose exec web python manage.py shell

test:
	docker compose exec web python manage.py test

clean:
	docker compose down -v
	rm -rf data/

restart: down up
