# Lesson 7 – Python API Client

This repository contains a solution for **Lesson 7** in the Python course at ITHS 2026.

The task was to build a minimal Python client that communicates with an API, with focus
on structure, configuration and automation.

## Overview

The project demonstrates a way to:
- interact with an API by performing multiple HTTP requests in sequence
- complete a defined API flow and verify the result by retrieving a flag
- use Swagger/OpenAPI documentation as a reference for available endpoints
- package the solution in a reproducible way using a public GitHub repository
- install and run the client using standard Python tooling (`pip install -r requirements.txt`)

## Project structure

```text
api-client/
├── client.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/            (ignored by Git)
```

## How to run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python client.py
```

API settings such as base URL and token are read from environment variables using a .env file.

## Notes

This repository is based on the original course repository by Björn Ettelman.
All commits authored by me represent my own work and changes made as part of the assignment.

The purpose of this lab could be to demonstrate:

- basic Git usage (fork, commit, push)
- Python project structure
- simple API communication

Basic security considerations have been taken into account:

- API credentials are handled via environment variables and are not stored directly in the source code
- the client avoids unnecessary output that could expose internal or sensitive information
- the implementation is intentionally minimal and limited to the defined API flow
