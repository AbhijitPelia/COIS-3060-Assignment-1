"""
AI-Use Declaration:
    Claude was used to help write the test cases below. I reviewed every test, ran the suite locally to confirm it passes,
    and verified that each test maps to a requirement in docs/requirements.md.
"""

import unittest
from html.parser import HTMLParser
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"
TABS = ["data-sources", "collection-methods", "analysis-methods", "publication-venues"]
DATA_SOURCES = ["GitHub", "Stack Overflow", "JIRA", "App Stores", "Travis CI / Jenkins", "Mailing Lists", "npm Registry"]


class PageParser(HTMLParser):
    """
    Reads index.html once and records what the tests need:
    the tab labels in page order, each radio input and whether it is checked, each section id, and the rows 
    and text inside the Data Sources section. It tracks which section and table body it is currently inside, 
    so content from other sections and the table's header row are never counted
    """

    def __init__(self):
        super().__init__()
        self.labels = []
        self.radios = {}
        self.sections = []
        self.in_section = None
        self.in_tbody = False
        self.data_rows = 0
        self.data_text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "label" and "tab" in (a.get("class") or "").split():
            self.labels.append(a.get("for"))
        elif tag == "input" and a.get("type") == "radio":
            self.radios[a.get("id")] = "checked" in a
        elif tag == "section":
            self.sections.append(a.get("id"))
            self.in_section = a.get("id")
        elif tag == "tbody":
            self.in_tbody = True
        elif tag == "tr" and self.in_tbody and self.in_section == "data-sources":
            self.data_rows += 1

    def handle_endtag(self, tag):
        if tag == "section":
            self.in_section = None
        elif tag == "tbody":
            self.in_tbody = False

    def handle_data(self, data):
        if self.in_section == "data-sources":
            self.data_text.append(data)

# Parse the page and load the stylesheet once for all tests
page = PageParser()
page.feed((SRC / "index.html").read_text(encoding="utf-8"))
css = " ".join((SRC / "style.css").read_text(encoding="utf-8").split())


class TestNavigation(unittest.TestCase):
    """Checks that tab navigation is set up correctly"""

    def test_four_tabs_in_order(self):
        """
        The page has exactly four tabs: Data Sources, Collection Methods, Analysis Methods, Publication Venues.
        """
        self.assertEqual(page.labels, [f"tab-{t}" for t in TABS])

    def test_each_tab_has_radio_and_section(self):
        """
        Every tab is connected to a radio input (which tracks the selection) and a matching content section (which gets shown).
        A missing piece would leave a tab that does nothing when clicked.
        """
        for t in TABS:
            self.assertIn(f"tab-{t}", page.radios)
            self.assertIn(t, page.sections)

    def test_data_sources_selected_by_default(self):
        """
        When the page first loads, exactly one tab is selected and it is Data Sources, so the user always 
        sees content instead of a blank page.
        """
        checked = [rid for rid, on in page.radios.items() if on]
        self.assertEqual(checked, ["tab-data-sources"])

    def test_css_shows_each_selected_section(self):
        """
        Tab switching is done entirely in CSS, so the stylesheet must have a rule that shows each section when 
        its tab is selected.
        """
        for t in TABS:
            self.assertIn(f"#tab-{t}:checked ~ #{t}", css)

class TestDataSourcesContent(unittest.TestCase):
    """Checks that the Data Sources content displays correctly."""

    def test_all_seven_data_sources_listed(self):
        """
        The Data Sources table has exactly 7 rows and every source requested by the Group Lead appears by name.
        """
        self.assertEqual(page.data_rows, 7)
        text = " ".join(page.data_text)
        for name in DATA_SOURCES:
            self.assertIn(name, text)


if __name__ == "__main__":
    unittest.main()
