#!/bin/sh
cd /app/src/apps/rest_api/ && alembic upgrade head && cd -
uvicorn src.apps.rest_api.entrypoint:app --reload --host 0.0.0.0 --port 8080