import unittest

from markdown_utils import *

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
def test_extract_markdown_links(self):
    matches = test_extract_markdown_links(
        "This is a paragraph with a [link](https://www.google.com)"
    )
    self.assertListEqual([("link", "https://www.google.com")], matches)

def test_markdown_to_blocks(self):
        md = """
                This is **bolded** paragraph

                This is another paragraph with _italic_ text and `code` here
                This is the same paragraph on a new line

                - This is a list
                - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

def test_heading(self):
    md = """
# This is a h1 header

## This is a h2 header

### This is a h3 header with **bold** text
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>This is a h1 header</h1><h2>This is a h2 header</h2><h3>This is a h3 header with <b>bold</b> text</h3></div>",
    )

def test_unordered_list(self):
    md = """
- First item
- Second item with **bold** text
- Third item with _italic_ text
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>First item</li><li>Second item with <b>bold</b> text</li><li>Third item with <i>italic</i> text</li></ul></div>",
    )

def test_ordered_list(self):
    md = """
1. First item
2. Second item with **bold** text
3. Third item with _italic_ text
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>First item</li><li>Second item with <b>bold</b> text</li><li>Third item with <i>italic</i> text</li></ol></div>",
    )

def test_quote(self):
    md = """
> This is a quote block
> with multiple lines
> and **bold** text
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>This is a quote block with multiple lines and <b>bold</b> text</blockquote></div>",
    )

def test_invalid_code_block_missing_start(self):
    md = """
This is text that should remain
the **same** even with inline stuff
```
"""
    with self.assertRaises(ValueError) as context:
        markdown_to_html_node(md)
    self.assertEqual(str(context.exception), "Invalid code block")

def test_invalid_code_block_missing_end(self):
    md = """
```
This is text that should remain
the **same** even with inline stuff
"""
    with self.assertRaises(ValueError) as context:
        markdown_to_html_node(md)
    self.assertEqual(str(context.exception), "Invalid code block")

def test_invalid_block_type(self):
    md = """
# This is a valid heading

This is a valid paragraph

This is an invalid block type that doesn't match any known pattern
"""
    # This test assumes that the invalid block will cause an error
    # You might need to adjust this based on how block_to_block_type works
    # If it returns a default type, this test might need modification
    pass

