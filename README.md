# Technical Test: HD Wallet test

## Description

Three services:
- __WALLET__: Is the app itself, it exposes a REST API; http://localhost:8081/
- __POSTGRES__: The database; **root/1234**
- __PGADMIN__: Tool to explore the database; **pgadmin4@pgadmin.org/admin**;  http://localhost:5050

## Wallet's features and endpoints

- Please, visit http://localhost:8081/docs to check all the available endpoints and play with them.

## Getting Started

Go to the project root and execute:
- "make run" to simply start the project.
- "make test" launches tests.

Feel free to explore the docker-compose.yaml file, everything you need is there.


### Prerequisites

- Docker and docker-compose.


