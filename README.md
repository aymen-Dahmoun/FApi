# FastAPI Project Generator CLI

A CLI tool that scaffolds FastAPI projects with optional database and API structure.

---

## ✅ Features

| Feature                    | Description                                         |
| -------------------------- | --------------------------------------------------- |
| Generate FastAPI project   | Creates a full FastAPI folder structure             |
| Optional Database          | SQLite, PostgreSQL (Async), or MongoDB              |
| Redis & Caching            | Optional integrated Redis support                   |
| JWT Authentication         | Scaffold a full Auth system (JWT + Password Hashing) |
| WebSockets                 | Integrated WebSocket support & boilerplates         |
| Background Tasks           | Support for Celery or Arq workers                   |
| Mail Service               | Integrated FastAPI-Mail support                     |
| `fapi run`                 | Automatically detect entry point & run with uvicorn |
| `fapi add` commands        | Easily add routes, models, schemas, crud, services  |

---

## 📂 Project Output Structure

When everything is enabled:

```
project_name/
 ├─ app/
 │  ├─ main.py
 │  ├─ core/
 │  │   ├─ config.py      # Core config with .env loading
 │  │   ├─ database.py    # DB connection (SQLAlchemy Async or MongoDB)
 │  │   └─ security.py    # JWT & Auth logic
 │  ├─ models/
 │  │   └─ user.py
 │  ├─ schemas/
 │  │   └─ user.py
 │  ├─ crud/
 │  │   └─ user.py
 │  ├─ services/
 │  │   ├─ email.py       # Mail service
 │  │   └─ passwordHash.py
 │  ├─ api/
 │  │   ├─ ws/            # WebSocket routes
 │  │   ├─ deps.py        # DI for Auth
 │  │   └─ router.py      # Main router
 │  ├─ tasks/             # Worker logic (Celery/Arq)
 │  └─ __init__.py
 ├─ .fastapi              # internal flag to detect project
 ├─ .env                  # Generated with configured keys
 ├─ requirements.txt
 └─ .venv/
```

---

## 🧰 Installation

### Clone Repo

```bash
pip install fapier
```
or
```bash
pipx install fapier
```

> Requires Python 3.10+

---

## Usage

### Create a project

```bash
fapi create myProject
```

### Advanced Options

```bash
fapi create myProject --db postgres --is-async --redis --auth jwt --websockets --tasks celery --mail --routes
```

| Option | Flag | Description |
| --- | --- | --- |
| Database | `--db` | `sqlite`, `postgres`, or `mongodb` |
| Async | `--is-async` | Enable async mode for SQLAlchemy |
| Redis | `--redis` | Add Redis integration |
| Auth | `--auth` | Scaffold JWT Auth (`jwt`) |
| WebSockets | `--websockets`| Add WebSocket boilerplates |
| Tasks | `--tasks` | `celery` or `arq` |
| Mail | `--mail` | Add Mail Service |

### Add new components

```bash
fapi add route product
fapi add model product --schema --crud
fapi add service payment
fapi add schema product
fapi add crud product

```

---

## 🚀 Run the project

Just navigate into your project and run:

```bash
fapi run
```

This automatically detects the virtual environment and runs the project using `uvicorn app.main:app --reload`.

---

## 📌 Roadmap

| Feature                | Status     |
| ---------------------- | ---------- |
| Basic FastAPI scaffold | ✅ Done     |
| PostgreSQL & MongoDB   | ✅ Done     |
| Async DB Support       | ✅ Done     |
| JWT Authentication     | ✅ Done     |
| Redis & WebSockets     | ✅ Done     |
| Background Workers     | ✅ Done     |
| `fapi run` command     | ✅ Done     |
| Publish on PyPI        | ✅ Done    |
| `fapi add` commands    | ✅ Done     |
| Alembic migrations     | 🔜 Planned |
| Docker support         | 🔜 Planned |

---

## 🤝 Contributing

Pull requests are welcome! 👐

---

⭐ If you like this tool, give the repo a star!
