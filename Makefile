run:
	docker-compose build && docker-compose up -d
test:
	docker-compose exec wallet pytest -s
