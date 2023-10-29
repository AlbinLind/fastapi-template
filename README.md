# FastAPITemplate

I created this template to have a quick start for my FastAPI projects. It my own take on the templates of [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql) and [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) repositories. To understand the folder structure see part about folder structure.

This project does **not** guarantee, nor does it try to say, that it is the best/only way to structure a FastAPI project. It is just my own personal preferance, and I am open to suggestions and improvements.

## Features
Some of the features that this template provides:
- `poetry` for dependency management
- `pytest` for testing
- `ruff` for linting and formatting
- `alembic` for database migrations
- `docker-compose` for running the API
- `GitHub` workflows for linting, and coverage.
- `.devcontainer` configuration for quick and isolated development


## Commands
You will do most coding for the backend in the `./backend` folder, to get there use `cd backend` where you can run the following commands:
- `poetry install` to install dependencies
- `poetry run migrate` to run the migrations, press enter to apply all migrations
- `poetry run api` to run the API/backend
- `poetry run lint` to run the linter
- `poetry run test` to run the tests and coverage

## Folder Structure
In the `./backend` folder you will find the source code (`./backend/src`), tests (`./backend/tests`), scripts (`./backend/scripts`), and migrations (`./backend/alembic`).