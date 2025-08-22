import unittest

from gencontent import *


class TestExtractTitle(unittest.TestCase):
    def test_extracts_h1_title(self):
        md = """
Intro text

# My Title

Some paragraph
## Subheading
"""
        self.assertEqual(extract_title(md), "My Title")

    def test_raises_when_only_h2_h3(self):
        md = """
## Not a main title
### Also not a main title
Paragraph
"""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_ignores_no_space_after_hash(self):
        md = """
#NoSpaceHeading
Paragraph
"""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_trims_title_whitespace(self):
        md = """
#   Title with extra spaces   
"""
        self.assertEqual(extract_title(md), "Title with extra spaces")

    def test_returns_first_h1_when_multiple(self):
        md = """
# First Title
Content
# Second Title
"""
        self.assertEqual(extract_title(md), "First Title")


if __name__ == "__main__":
    unittest.main()


