from xml.etree import ElementTree as et
from xml.dom import minidom

def parseExtract(xmlfile, key):
    const='''<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">'''
    tree=et.parse(xmlfile)
    root=tree.getroot()
    ns={'xsd': 'http://www.w3.org/2001/XMLSchema'}
    for element in root.findall('xsd:element', ns):
        if key in element.attrib['name']:
            xmlstr = minidom.parseString(et.tostring(element)).toxml().replace('''<?xml version="1.0" ?>''','').replace(''' xmlns:xs="http://www.w3.org/2001/XMLSchema"''','').replace('xs','xsd')
            print(xmlstr)
            with open("new.xsd", "w") as f:
                f.write(const+xmlstr+'''</xsd:schema>''')







parseExtract('ebbp-2.0.4.xsd','sky_condition')