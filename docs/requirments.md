# Requirements for MSR Research Group Project

## Customer
MSR Research Group Lead

## User Stories

### 1: Category tabs *(R1)*
**As a** PhD student, **I want** tabs for the four categories at the top of the page, **so that** I can switch between them without scrolling through everything.

**Acceptance criteria:**
- Four tabs are shown at the top: Data Sources, Collection Methods, Analysis Methods, Publication Venues
- Clicking a tab displays that category's content

**Milestone:** 1 – Page Structure & Navigation

---

### 2: One section at a time *(R2)*
**As a** PhD student, **I want** only the selected category's content to show, **so that** I can focus on one topic at a time.

**Acceptance criteria:**
- Exactly one section is visible at any time
- A default section is visible when the page first loads
- Switching tabs hides the previous section

**Milestone:** 1 – Page Structure & Navigation

---

### 3: Active tab indicator *(R3)*
**As a** researcher, **I want** to see which tab is currently selected, **so that** I always know which category I'm reading.

**Acceptance criteria:**
- The active tab is visually distinct from the inactive tabs
- The highlight moves when a different tab is clicked

**Milestone:** 1 – Page Structure & Navigation

---

### 4: Available data sources *(R4)*
**As a** PhD student, **I want** to see available data sources, **so that** I can choose which data to collect.

**Acceptance criteria:**
- The Data Sources section lists all 7 sources: GitHub, Stack Overflow, JIRA, App Stores, Travis CI / Jenkins, Mailing Lists, npm Registry
- Each source shows its name and the kind of data it provides

**Milestone:** 2 – Data Sources Content

---

### 5: Data source descriptions *(R5)*
**As a** researcher, **I want** a brief description of each data source, **so that** I can quickly understand what it is without leaving the page.

**Acceptance criteria:**
- Every data source has a one- to two-sentence description
- Content is displayed in a table with columns for Name, Data Provided, and Description

**Milestone:** 2 – Data Sources Content

---

### 6: Build and CI data sources *(R6)*
**As a** PhD student, **I want** to know which sources provide build and CI data, such as Travis CI and Jenkins, **so that** I can study build failures.

**Acceptance criteria:**
- Travis CI / Jenkins appears in the Data Sources section
- Its entry lists build logs, test results, and deployment data

**Milestone:** 2 – Data Sources Content

---

### 7: Collection method trade-offs *(R7)*
**As a** researcher, **I want** to see the pros and cons of each collection method, **so that** I can pick the most efficient one for my project.

**Acceptance criteria:**
- The Collection Methods section lists all 6 methods: REST APIs, GraphQL, Web Scraping (Selenium), Web Scraping (BeautifulSoup), Database Dumps, Manual Download
- Each method shows its name, what it is used for, and its pros and cons

**Milestone:** 3 – Collection Methods Content

---

### 8: Analysis methods by type *(R8)*
**As a** PhD student, **I want** to see common analysis methods with their type, **so that** I can choose an approach that fits my data.

**Acceptance criteria:**
- The Analysis Methods section lists all 8 methods: Statistical Analysis, Regression Analysis, Thematic Analysis, Grounded Theory, Machine Learning, Time Series Analysis, Network Analysis, Visualization
- Each method shows its name, type of analysis, and common use cases

**Milestone:** 4 – Analysis Methods Content

---

### 9: Compare publication venues *(R9)*
**As a** researcher, **I want** to compare publication venues, **so that** I can pick the most appropriate one.

**Acceptance criteria:**
- The Publication Venues section lists all 9 venues: ICSE, FSE, ASE, MSR, EASE, SANER (conferences) and EMSE, TSE, TOSEM (journals)
- Each venue shows its name and abbreviation, type, focus area, and MSR relevance (high or medium)
- Conferences and journals are displayed separately

**Milestone:** 5 – Publication Venues Content

---

### 10: Clean, readable layout *(R10)*
**As a** researcher, **I want** a clean, readable layout without animations, **so that** I can focus on the content.

**Acceptance criteria:**
- No decorative animations or transitions that delay content
- Readable font size and sufficient contrast between text and background
- Consistent table styling across all sections

**Milestone:** 6 – Styling & Polish

---

### 11: Live, auto-updating site *(R11)*
**As the** research group lead, **I want** the live site to update whenever content is added, **so that** students always see current information.

**Acceptance criteria:**
- The page is accessible through a public GitHub Pages URL
- Every merge to `main` that passes the tests automatically redeploys the site

**Milestone:** 1 – Page Structure & Navigation

## Out of Scope
- User accounts or login
- Editing content from the browser
- Search or filtering within sections

## Requirements Analysis

| # | Requirement (system should DO or HAVE) | F / NF | User / System | Who | Priority |
|---|---|---|---|---|---|
| R1 | The system should display four tabs at the top of the page: Data Sources, Collection Methods, Analysis Methods, and Publication Venues | F | User | Group Lead | Must |
| R2 | The system should show only the selected tab's section, with one section visible by default on page load | F | System | Group Lead | Must |
| R3 | The system should visually highlight the currently active tab | NF (usability) | User | Group Lead (derived from "easy to navigate") | Should |
| R4 | The system should list all 7 data sources, each with its name and the kind of data it provides | F | User | Group Lead | Must |
| R5 | The system should show a brief description of each data source in a table (Name, Data Provided, Description) | F | User | Group Lead | Must |
| R6 | The system should include Travis CI / Jenkins as a data source, listing build logs, test results, and deployment data | F | User | Group Lead | Should |
| R7 | The system should list all 6 collection methods, each with what it is used for and its pros and cons | F | User | Group Lead | Must |
| R8 | The system should list all 8 analysis methods, each with its type of analysis and common use cases | F | User | Group Lead | Must |
| R9 | The system should list all 9 publication venues with name and abbreviation, type, focus area, and MSR relevance (high/medium), with conferences and journals shown separately | F | User | Group Lead | Must |
| R10 | The system should have a clean, readable, professional layout with no decorative animations | NF (usability) | User | Group Lead | Should |
| R11 | The system should automatically redeploy to a public GitHub Pages URL on every merge to main that passes the tests | NF (availability, maintainability) | System | Course Instructor | Must |

**Unclear / missing information:**
- The meeting notes list the items for each section but not their descriptions, pros and cons, use cases, or focus areas. That content must be written by the developer and confirmed with the Group Lead.
- The MSR relevance rating (high/medium) for each venue is not specified.
- Analysis methods should be "organized by type," but the types themselves (e.g., quantitative vs. qualitative) are not defined.
- No default tab is specified for when the page first loads.
- Browser support, mobile/responsive requirements, and accessibility standards are not mentioned.
- It is unclear who will maintain and update the content after delivery.