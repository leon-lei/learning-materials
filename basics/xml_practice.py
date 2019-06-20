# Code sample from Omar Quimbaya Youtube channel

import xml.etree.ElementTree as et

from pathlib import Path


base_path = Path.cwd()
xml_file = base_path / 'product_listing.xml'
xml_file.touch(exist_ok=True)

tree = et.parse(xml_file)
root = tree.getroot()

# Write to XML
new_product = et.SubElement(root, 'product', attrib={'id': '4'})
new_prod_name = et.SubElement(new_product, 'name')
new_prod_desc = et.SubElement(new_product, 'description')
new_prod_cost = et.SubElement(new_product, 'cost')
new_prod_ship = et.SubElement(new_product, 'shipping')

new_prod_name.text = 'Shio Ramen'
new_prod_desc.text = 'Straight noodles with garlicky broth'
new_prod_cost.text = '10.99'
new_prod_ship.text = '2.99'

tree.write(xml_file)

# Read XML
for child in root:
    print(child.tag, child.attrib)

for child in root:
    for element in child:
        print(f'{element.tag}: {element.text}')
    print('#'*35)