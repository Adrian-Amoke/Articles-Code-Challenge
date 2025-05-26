# Articles-Code-Challenge

## Project Description
This project manages articles, authors, and magazines using a SQLite database backend. It provides Python models for `Article`, `Author`, and `Magazine` with relationships between them, allowing for creation, querying, and updating of records.

## Installation

1. Ensure you have Python 3.7+ installed.
2. Install [Pipenv](https://pipenv.pypa.io/en/latest/) for dependency management:
   ```bash
   pip install pipenv
   ```
3. Install project dependencies:
   ```bash
   pipenv install
   ```
4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Database Setup

The project uses SQLite as the database, with the database file named `articles.db`. The connection is handled via the `lib/db/connection.py` module.

To set up the database schema and seed data, you may need to run the appropriate scripts or commands (not provided in this repository). Ensure the `articles.db` file is present in the project root or update the connection path accordingly.

## Usage Overview

The project provides Python classes to interact with the database:

- `Article`: Represents an article with attributes like title, author, and magazine.
- `Author`: Represents an author and includes methods to retrieve their articles and magazines.
- `Magazine`: Represents a magazine with a name and category, and methods to get related articles and authors.

These models support saving new records, updating existing ones, and querying by various attributes.

## Running Tests

Tests are located in the `tests/` directory and cover the models for articles, authors, and magazines.

To run the tests, ensure you are in the virtual environment and run:

```bash
pytest
```

Make sure `pytest` is installed in your environment (it should be included in the Pipfile if used).

## Project Structure

```
.
├── lib/
│   ├── controllers/
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.py
│   │   ├── seed.py
│   ├── models/
│       ├── article.py
│       ├── author.py
│       ├── magazine.py
├── scripts/
│   ├── run_queries.py
│   ├── setup_db.py
├── tests/
│   ├── test_article.py
│   ├── test_author.py
│   ├── test_magazine.py
├── Pipfile
├── Pipfile.lock
├── README.md
```

## Notes

- The `scripts/` directory contains scripts for database setup and running queries, but these files appear to be empty or placeholders.
- The database schema and seed files are located in `lib/db/schema.sql` and `lib/db/seed.py` respectively, which can be used to initialize the database.
