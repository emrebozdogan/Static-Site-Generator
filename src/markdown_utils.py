import re
from blocktypes import *
from htmlnode import *
from parentnode import *
from leafnode import *
from textnode_utils import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    for line in blocks:
        line = line.strip("\n")
        if line.strip() == "":
            blocks.remove(line)
    return blocks
    
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    block_html_nodes = list()
    for block in markdown_blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            heading_text = block.lstrip('#').strip()
            block_html_nodes.append(ParentNode(tag=f"h{block.count('#')}", children=text_to_children(heading_text)))
        elif block_to_block_type(block) == BlockType.PARAGRAPH:
            block_html_nodes.append(ParentNode(tag="p", children=text_to_children(block)))
        elif block_to_block_type(block) == BlockType.CODE:
            if not (block.startswith("```") and block.endswith("```")):
                raise ValueError("Invalid code block")
            text = block[4:-3]
            text_node = TextNode(text, TextType.TEXT)
            child = text_node_to_html_node(text_node)
            code = ParentNode(tag="code", children=[child])
            block_html_nodes.append(ParentNode(tag="pre", children=[code]))
        elif block_to_block_type(block) == BlockType.QUOTE:
            lines = block.split('\n')
            clean_lines = [line.lstrip('> ').strip() for line in lines]
            quote_text = '\n'.join(clean_lines)
            block_html_nodes.append(ParentNode(tag="blockquote", children=text_to_children(quote_text)))
        elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            html_items = list()
            for item in items:
                text = item[2:]
                html_items.append(ParentNode(tag="li", children=text_to_children(text)))
            block_html_nodes.append(ParentNode(tag="ul", children=html_items))
        elif block_to_block_type(block) == BlockType.ORDERED_LIST:
            items = block.split("\n")
            html_items = list()
            for item in items:
                text = item[item.find(".")+2:]
                html_items.append(ParentNode(tag="li", children=text_to_children(text)))
            block_html_nodes.append(ParentNode(tag="ol", children=html_items))
        else:
            raise ValueError("Invalid block type")
    return ParentNode(tag="div", children=block_html_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
