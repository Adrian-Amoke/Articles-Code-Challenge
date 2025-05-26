# Articles-Code-Challenge

## Project Description
Welcome to the Articles-Code-Challenge project! This is a simple Python application that helps you manage articles, authors, and magazines using a lightweight SQLite database. The project provides easy-to-use Python classes for working with articles, authors, and magazines, letting you create, update, and query your data effortlessly.

## Installation

To get started, make sure you have Python 3.7 or higher installed on your machine. We use Pipenv to manage dependencies, so if you don't have it yet, you can install it with:

```bash
pip install pipenv
```

Once Pipenv is installed, you can install the project dependencies by running:

```bash
pipenv install
```

After that, activate the virtual environment with:

```bash
pipenv shell
```

## Database Setup

This project uses SQLite for its database, which means you don't need to set up a separate database server. The database file is named `articles.db` and is located in the project root.

If you want to initialize the database schema or seed it with data, you can use the files in `lib/db/schema.sql` and `lib/db/seed.py`. Note that the scripts directory contains placeholders for setup and query scripts, but they are currently empty.

## Usage Overview

The core of the project revolves around three Python classes:

- `Article`: Represents an article with a title, author, and magazine.
- `Author`: Represents an author and provides methods to get their articles and magazines.
- `Magazine`: Represents a magazine with a name and category, along with methods to retrieve related articles and authors.

These classes make it easy to interact with your data, whether you're adding new records or fetching existing ones.

## Running Tests

Tests for the project are located in the `tests/` directory and cover the main models: articles, authors, and magazines.

To run the tests, first make sure you're inside the virtual environment, then run:

```bash
pytest
```

If you don't have `pytest` installed, you can add it to your environment using Pipenv.

## Project Structure

Here's a quick look at the project structure:

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

- The `scripts/` directory currently contains empty placeholder files for database setup and queries.
- You can use the `lib/db/schema.sql` and `lib/db/seed.py` files to initialize and seed the database as needed.

