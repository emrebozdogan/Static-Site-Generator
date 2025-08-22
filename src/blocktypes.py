from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    line = block
    hash_char = "#"
    result = BlockType.PARAGRAPH
    for _ in range(0, 6):
        if re.findall(r"^" + hash_char + " ", line):
            result = BlockType.HEADING
        hash_char += "#"
    if re.findall(r"```[\s\S]*?```", line):
            result = BlockType.CODE
    if re.findall(r"^> ", line):
            result = BlockType.QUOTE
    if re.findall(r"^- ", line):
            result = BlockType.UNORDERED_LIST
    if re.findall("1. ", line):
            result = BlockType.ORDERED_LIST
        
    return result