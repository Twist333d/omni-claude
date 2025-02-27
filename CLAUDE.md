# Kollektiv Development Guide

## Commands
- Build & Run: `kollektiv api` (API server), `kollektiv worker` (ARQ worker)
- Docker: `make up` (start services), `make down` (stop), `make dev` (watch mode)
- Testing: `pytest tests/` (all), `pytest tests/unit/path/to/test.py::test_name` (specific)
- Linting: `ruff check .` or `ruff format .`
- Type checking: `mypy src/`

## Code Style
- Python: 3.12 with strict typing (use `mypy` for checking)
- Format: 120 line length, double quotes, Google-style docstrings
- Imports: Use `import x` for stdlib, `from x import y` for own code
- Error handling: Use custom exceptions from `src.core._exceptions`
- Decorators: Use `@supabase_operation`, `@anthropic_error_handler` for API calls
- Naming: snake_case for variables/functions, PascalCase for classes
- Async: Prefer async/await patterns with proper error handling

## Architecture
- FastAPI endpoints in `src/api/`
- Core business logic in `src/core/`
- Infrastructure (DB, Redis, etc.) in `src/infra/`
- Domain models in `src/models/`
- Application services in `src/services/`
