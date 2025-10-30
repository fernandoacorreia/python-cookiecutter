# Python Project Template

A Copier template for Python projects following modern best practices with Python 3.13+.

## Features

- **Modern Python**: Python 3.13+ with full type hints and strict type checking
- **Fast Package Manager**: Uses [uv](https://github.com/astral-sh/uv) for dependency management
- **Template Updates**: Supports updating existing projects with `copier update`
- **Custom Development CLI**: Plugin-based `./dev` script for common tasks
- **Comprehensive Testing**: pytest with custom fixtures and coverage support
- **Code Quality**: Integrated black, ruff, and basedpyright
- **Environment-Based Configuration**: python-dotenv for environment variables
- **Configurable Logging**: Supports both human-readable and JSON structured logging
- **License Options**: Apache 2.0 or Proprietary

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Fast Python package manager (used in generated projects)
- [Copier](https://copier.readthedocs.io/) - Template engine for project generation

## Quick Start

### Install Copier

```bash
# Using uv (recommended)
uv tool install --with jinja2-time copier
```

### Generate a New Project

```bash
# From GitHub
copier copy --trust gh:fernandoacorreia/python-project-template your-project-name

# From local directory
copier copy --trust /path/to/python-project-template your-project-name
```

You will be prompted for:
- **project_name**: Human-readable project name (e.g., "My Project")
- **project_slug**: URL/package-friendly name with hyphens (auto-generated, e.g., "my-project")
- **package_name**: Python module name with underscores (auto-generated, e.g., "my_project")
- **project_description**: One-line description of your project (e.g., "A Python project following best practices")
- **author_name**: Your full name (e.g., "Your Name")
- **author_email**: Your email address (e.g., "your.email@example.com")
- **python_version**: Python version (e.g., "3.13")
- **license**: License type (Apache-2.0 or Proprietary)

### Running Copier Non-Interactively (for Scripts)

To run Copier without prompts in scripts or automated workflows, use the `--data` flag to pass variables:

```bash
# Using --data flags
copier copy --trust --defaults \
  --data project_name="My Project" \
  --data project_slug="my-project" \
  --data package_name="my_project" \
  --data project_description="A Python project" \
  --data author_name="John Doe" \
  --data author_email="john@example.com" \
  --data python_version="3.13" \
  --data license="Apache-2.0" \
  /path/to/python-project-template your-project-name
```

Alternatively, use a data file:

```bash
# Create answers.yml
cat > answers.yml <<EOF
project_name: My Project
project_slug: my-project
package_name: my_project
project_description: A Python project
author_name: John Doe
author_email: john@example.com
python_version: "3.13"
license: Apache-2.0
EOF

# Use --data-file
copier copy --trust --defaults --data-file answers.yml \
  /path/to/python-project-template your-project-name
```

**Note**: The `--defaults` flag is required when running non-interactively to use default values for any variables not explicitly provided.

### Post-Generation Setup

The template includes post-generation tasks that automatically:
1. Initializes a Git repository
2. Creates CLAUDE.md symlink to AGENTS.md
3. Initializes virtual environment and installs dependencies (via `uv sync`)
4. Initializes development tools (via `./dev init`)
5. Creates an initial commit

After generation, activate your environment and start coding:

```bash
cd your-project-name
source .venv/bin/activate
./dev --help
```

### Updating an Existing Project

To update a project generated from this template:

```bash
cd your-project-name
copier update
```

Copier will prompt you for any new questions and update your project while preserving your customizations.

### Answers File

Your project's `.copier-answers.yml` file tracks:
- Template source (`_src_path`)
- Template version (`_commit`)
- Your answers to template questions

Keep this file in version control to enable future updates.

## Generated Project Structure

```
your-project/
├── src/
│   └── your_project/              # Main package (underscores, not hyphens)
│       ├── main.py                # Application entry point
│       └── py.typed               # PEP 561 type marker
├── tests/                         # Test suite
│   ├── conftest.py                # pytest fixtures
│   ├── main_test.py               # Example tests
│   └── data/                      # Test data files
├── scripts/                       # Development scripts
│   ├── dev.py                     # Main CLI dispatcher
│   └── commands/                  # Command modules
├── .copier-answers.yml            # Copier template metadata
├── .env                           # Environment variable definitions
├── .gitignore                     # Git ignore rules
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── .yamllint.yaml                 # YAML linting configuration
├── AGENTS.md                      # Claude Code instructions
├── CLAUDE.md -> AGENTS.md         # Symlink for Claude Code
├── dev                            # Development CLI entry point (executable)
├── example.env                    # Environment variable template
├── LICENSE                        # Project license
├── pyproject.toml                 # Project metadata and dependencies
├── README.md                      # Project documentation
└── uv.lock                        # Dependency lock file
```

## Development Commands

The generated project includes a `./dev` script:

```bash
./dev --help    # Show all available commands
```

## Template Customization

### Modifying the Template

To customize this template for your needs:

1. Edit `copier.yml` to add/modify variables
2. Update template files in `template/`
3. Add `.jinja` suffix to files that contain template variables
4. Modify `_tasks` in `copier.yml` for custom post-generation tasks
5. Use Jinja2 syntax for dynamic content: `{{ variable_name }}`

### Example: Adding a New Variable

1. Add to `copier.yml`:
```yaml
your_new_variable:
  type: str
  help: Description of your variable
  default: default_value
```

2. Use in template files (file must have `.jinja` suffix):
```python
# In any template file with .jinja suffix
MY_CONFIG = "{{ your_new_variable }}"
```

## Architecture Highlights

### Custom Development CLI
- Plugin-based architecture for easy extensibility
- Each command is a separate module in `scripts/commands/`
- Unknown arguments are forwarded to underlying tools (pytest, claude)

### Test Infrastructure
- Custom pytest fixtures: `test_data_dir` and `temp_dir`
- Automatic cleanup of temporary directories
- Example tests demonstrating best practices

### Type Safety
- Strict basedpyright checking for production code (`src/`)
- Relaxed checking for tests (`tests/`)
- PEP 561 compliant with `py.typed` marker

### Logging Configuration
- Environment-based configuration via `.env`
- Two formats: pretty (human-readable) and JSON (structured)
- Custom `JSONFormatter` for production logging

## License

This template itself is licensed under the Apache License 2.0.
Projects generated from this template will use the license you select during project generation (Apache 2.0 or Proprietary).

## Resources

- [Copier Documentation](https://copier.readthedocs.io/)
- [Copier Template Creation Guide](https://copier.readthedocs.io/en/stable/creating/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)