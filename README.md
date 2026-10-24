[![CI](https://github.com/AbhijitPelia/COIS-3060-Assignment-1/actions/workflows/ci.yml/badge.svg)](https://github.com/AbhijitPelia/COIS-3060-Assignment-1/actions/workflows/ci.yml)

# MSR Knowledge Base

A single-page reference guide for new PhD students in a Mining Software Repositories (MSR) research group. It organizes the four things new researchers need to know into tabs: **Data Sources**, **Collection Methods**, **Analysis Methods**, and **Publication Venues**.

**Live site:** https://abhijitpelia.github.io/COIS-3060-Assignment-1/

Built for COIS 3060H – Software Processes, Assignment 1, following a full software process: requirements analysis, project planning, implementation, testing, CI/CD, and documentation.

## Project Overview

The MSR Research Group Lead reported that new PhD students get overwhelmed because they don't know which data sources exist, how to collect data, which analysis methods to use, or where to publish. This project delivers a simple, clean reference page that students can open in any browser without downloading anything.

- **Requirements and user stories:** [`docs/requirements.md`](docs/requirements.md)
- **Tech stack:** HTML and CSS, Python `unittest` for automated tests, GitHub Actions for CI/CD, GitHub Pages for hosting

## Repository Structure

```
/docs
    requirements.md       Requirements analysis and user stories
/src
    index.html            Main page with four tab sections
    style.css             Styling and CSS-only tab switching
/tests
    test_page.py          Automated tests (run by CI)
    test_checklist.md     Manual test cases
/.github
    /workflows
        ci.yml            CI/CD pipeline
README.md
.gitignore
```

## Running the Tests

From the repository root (Python 3, no installs needed):

```
python3 -m unittest discover -s tests -v
```

## CI/CD Pipeline

The workflow in `.github/workflows/ci.yml` has two jobs:

1. **test** runs the automated tests on every push and pull request, on every branch.
2. **deploy** runs only on pushes to `main`, and only after the tests pass. It publishes `src/` to GitHub Pages, so the live site updates automatically with every change merged to `main`.

## Development Process

- **Branches:** `feature/page-structure-navigation` for the page, `test/page-structure-navigation` for the tests and CI workflow
- **Pull requests:** each branch was merged into `main` through a pull request that closed its issues
- **Commits:** small, focused commits that reference their issue numbers

## Completed Milestones

### Milestone 1: Page Structure & Navigation
| Issue | Description | Closed by |
|---|---|---|
| #1 | Build page structure and tab navigation | PR #8 |
| #3 | Add tests and CI/CD pipeline with GitHub Pages deploy | PR #9 |

### Milestone 2: Data Sources Content
| Issue | Description | Closed by |
|---|---|---|
| #2 | Add Data Sources content table (all 7 sources) | PR #8 |

## Remaining Milestones (Future Work)

### Milestone 3: Collection Methods Content
- **#4** Add all 6 collection methods (REST APIs, GraphQL, Web Scraping with Selenium and BeautifulSoup, Database Dumps, Manual Download), each with its use and pros/cons

### Milestone 4: Analysis Methods Content
- **#5** Add all 8 analysis methods, each with its type of analysis and common use cases, organized by type

### Milestone 5: Publication Venues Content
- **#6** Add all 9 venues (6 conferences, 3 journals) with abbreviation, type, focus area, and MSR relevance, with conferences and journals shown separately

### Milestone 6: Styling & Polish
- **#7** Refine the responsive layout and add professional touches

## AI-Use Declaration

I used Claude,to help with this assignment, mainly for testing and CI/CD. Claude helped write the automated tests in `tests/test_page.py`, mostly helping fix bugs. Claude suggested using Python's built-in `unittest` so the pipeline needs no installs, and wrote the GitHub Actions workflow in `.github/workflows/ci.yml`. I ran the tests locally, checked that each one maps to a requirement in `docs/requirements.md`, configured GitHub Pages, verified that the pipeline runs and passes, and completed the manual checklist on the live site. I made all commits, branches, and pull requests myself, and I understand all submitted code and documents and can explain how each part works.