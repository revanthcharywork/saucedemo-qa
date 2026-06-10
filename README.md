# SauceDemo QA Automation

End-to-end test automation framework for [SauceDemo](https://www.saucedemo.com) built with Python, Playwright, and pytest.

![CI](https://github.com/revanthcharywork/saucedemo-qa/actions/workflows/tests.yml/badge.svg)

## Tech Stack

- Python
- Playwright
- pytest
- pytest-html
- GitHub Actions

## Project Structure

```
saucedemo-qa/
├── .github/workflows/    # CI/CD pipeline
├── pages/                # Page Object Model classes
├── tests/                # Test cases
├── utils/                # Helper utilities
├── reports/              # Generated HTML reports
├── conftest.py           # pytest fixtures
└── pytest.ini            # pytest configuration
```

## Test Coverage

| Module | Tests |
|--------|-------|
| Login | Valid login, invalid login, locked-out user, empty username, empty password |
| Inventory | Product sort by price low to high |
| Cart | Remove item updates cart count |

## Design Pattern

Page Object Model (POM) with a `BasePage` class. Each page has its own class under `pages/` encapsulating locators and actions. Tests in `tests/` use fixtures from `conftest.py` for browser and login setup.

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt
pip install pytest-html
playwright install chromium

# Run all tests
pytest

# Run only smoke tests
pytest -m smoke

# Run with visible browser
pytest --headed
```

## CI/CD

Tests run automatically on every push and pull request to `main` via GitHub Actions. HTML report is uploaded as a build artifact after each run.
