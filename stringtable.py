import os
import xml.etree.ElementTree as ET

from typing import Optional


class StringTable:
    name = ''
    start_index = None
    next_index = None
    nametable_tree = None
    entry_node = None

    def __init__(self, name: str, start_index: int):
        # load template
        with open('template/stringtable.xml') as stringtable_template_file:
            self.nametable_tree = ET.parse(stringtable_template_file)

        # initialize class variables
        self.name = name
        self.start_index = start_index
        self.next_index = start_index

        # initialize nametable tree
        tree_root = self.nametable_tree.getroot()
        tree_root.find('Name').text = self.name
        self.entry_node = tree_root.find('Entries')

    def insert(self, entry_text: str, entry_index: Optional[int] = None) -> int:
        if entry_index is None:
            entry_index = self.next_index

        # load template
        with open('template/stringtable_entry.xml') as entry_template_file:
            new_entry = ET.parse(entry_template_file).getroot()

        # insert new entry
        new_entry.find('ID').text = str(entry_index)
        new_entry.find('DefaultText').text = entry_text
        self.entry_node.append(new_entry)
        self.next_index += 1

        return entry_index

    def write(self, file_path: str):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.nametable_tree.write(file_path, encoding='utf-8', xml_declaration=True)
