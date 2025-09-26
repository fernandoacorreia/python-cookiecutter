# python-scaffolding
Python project scaffolding

## Development Setup

### Prerequisites
- [uv](https://github.com/astral-sh/uv) package manager

### Setup Development Environment
```bash
# Create virtual environment
uv venv --python 3.13

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies and create virtual environment
uv sync --dev
```

### Running the Application
```bash
# Run the main application
uv run python -m python_scaffolding.main
```

### Code Formatting and Linting
```bash
# Format code with black
uv run --dev -m black .

# Lint code with ruff
uv run --dev -m ruff check --fix .
```

### Testing
```bash
# Run unit tests
uv run pytest -v
```

### Building
```bash
# Build wheel file
uv build
```

The wheel file will be created in the `dist/` directory.
