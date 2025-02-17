lint:
	pre-commit run --all-files

local-dev:
	docker compose up -d
local-stop:
	docker compose stop
local-down:
	docker compose down
local-logs:
	docker compose logs -f