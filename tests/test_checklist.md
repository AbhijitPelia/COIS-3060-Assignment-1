# Manual Test Checklist

Tests the parts of the page that need a browser: clicking, visual highlight, and layout.

| # | Test | Steps | Expected Result | Requirement | Pass/Fail |
|---|---|---|---|---|---|
| T1 | Default tab on load | Open the page | Data Sources tab is highlighted and its table is shown; other sections are hidden | R2 | |
| T2 | Switch tabs | Click each of the four tabs | Only the clicked tab's section is shown | R1, R2 | |
| T3 | Active tab highlight | Click a different tab | Highlight moves to the clicked tab | R3 | |
| T4 | Data Sources content | Open Data Sources | 7 rows, each with source name, data provided, and description | R4, R5, R6 | |
| T5 | Hover state | Hover over an inactive tab | Tab outline and text change to blue | R3 | |
| T6 | Narrow screen | Shrink the browser window to phone width | Tabs wrap and the table scrolls sideways without breaking the page | R10 | |
| T7 | Live site | Open the GitHub Pages URL after merging to main | Page loads and behaves the same as locally | R11 | |