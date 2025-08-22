import unittest
from blocktypes import *

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading_detection(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Level 2 heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#NoSpaceHeading"), BlockType.PARAGRAPH)

    def test_code_block_detection(self):
        self.assertEqual(block_to_block_type("```python\nprint('hello')\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```incomplete"), BlockType.PARAGRAPH)

    def test_quote_detection(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">NotAQuote"), BlockType.PARAGRAPH)

    def test_paragraph_default(self):
        self.assertEqual(block_to_block_type("Regular paragraph text"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)


if __name__ == '__main__':
    unittest.main() 