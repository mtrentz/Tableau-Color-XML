def save_tableau_xml(hex_list, scheme_name):
    xml_str = ''
    xml_str += f'<color-palette name="{scheme_name}" type="regular">'
    for hex_code in hex_list:
        xml_str += '\n'
        xml_str += '\t'
        xml_str += f'<color>{hex_code}</color>'
    xml_str += '\n'
    xml_str += '</color-palette>'

    with open(f'{scheme_name}.xml', 'w+') as f:
        f.write(xml_str)

    return xml_str


schema_name = "Name (Shows on Tableau Colors)"
my_list = [
    # Hex codes
    '#251e20',
    '#5C4B51',
    '#30544c',
    '#8CBEB2',
    '#90801d',
    '#F2EBBF',
    '#7f4d0a',
    '#F3B562',
    '#7b0c0c',
    '#F06060',
    ]

print(save_tableau_xml(my_list, schema_name))