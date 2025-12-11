# project-template-simple

A simple Python/data science project template with UV, Taskfile, pre-commit, ruff, black, mypy, and pytest.

## Using This Template

1. **Create your project** — Click the green "Use this template" button on GitHub, or fork this repo
2. **Clone** your new repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/your-project-name.git
   cd your-project-name
   ```
3. **Rename the project** in `pyproject.toml`:
   ```toml
   [project]
   name = "your-project-name"
   description = "Your project description"
   ```
4. **Run setup** and start coding:
   ```bash
   task setup
   ```

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [UV](https://docs.astral.sh/uv/) - Fast Python package manager
- [Task](https://taskfile.dev/) - Task runner

## Quick Start

```bash
# Install Task (if not already installed)
# macOS
brew install go-task

# Linux
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin

# Windows (with Chocolatey)
choco install go-task
```

```bash
# Install UV (if not already installed)
# For instructions:
task install:uv:help
```

```bash
# Full project setup (install dependencies + pre-commit hooks)
task setup

# Or just install dependencies
task install
```

## Available Tasks

Run `task` or `task --list` to see all available tasks:

| Task | Description |
|------|-------------|
| `task setup` | Full project setup (install + pre-commit) |
| `task install` | Install all dependencies |
| `task check` | Run all code quality checks (lint, format, types) |
| `task fix` | Auto-fix code issues (lint + format) |
| `task test` | Run tests |
| `task test:cov` | Run tests with coverage |
| `task pre-commit` | Run pre-commit on all files |
| `task clean` | Clean up generated files |

## Project Structure

```
project-template-simple/
├── data/               # Data files (gitignored)
├── src/                # Source code
│   └── __init__.py
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_example.py
├── .env                # Environment variables (gitignored)
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml      # Project config & dependencies
├── Taskfile.yml        # Task definitions
├── uv.lock             # Dependency lock file
└── README.md
```

## Development Workflow

1. **Setup**: Run `task setup` to install dependencies and pre-commit hooks
2. **Code**: Write your code in `src/`
3. **Test**: Run `task test` to run tests
4. **Check**: Run `task check` to run all quality checks
5. **Commit**: Pre-commit hooks will automatically format and lint your code

## Environment Variables

Copy the `.env.example` to `.env` and fill in your values (I primarily use it for API keys):

```bash
cp .env.example .env
```

Load environment variables in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

my_var = os.getenv("MY_VARIABLE")
```

## Tools Overview
These are the main tools that I use for projects.

| Tool | Purpose |
|------|---------|
| **[uv](https://docs.astral.sh/uv/)** | Fast Python package manager and virtual environment tool. Replaces pip/pip-tools/venv with a single, blazingly fast Rust-based tool. |
| **[Task](https://taskfile.dev/)** | Modern task runner (like Make, but simpler). Defines common commands in `Taskfile.yml` so you don't have to remember them. |
| **[Ruff](https://docs.astral.sh/ruff/)** | Extremely fast Python linter and code checker. Catches bugs, enforces style, and replaces dozens of tools (flake8, isort, etc.). |
| **[Black](https://black.readthedocs.io/)** | Opinionated Python code formatter. Automatically formats code to a consistent style—no debates about formatting. |
| **[pre-commit](https://pre-commit.com/)** | Git hooks manager. Automatically runs checks (ruff, black, mypy) before each commit to catch issues early. |
| **[mypy](https://mypy.readthedocs.io/)** | Static type checker for Python. Catches type errors before runtime if you use type hints. |
