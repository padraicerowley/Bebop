import os
from xml.etree import ElementTree


def get_files_indirectory(path):
    n = []
    for top, dirs, files in os.walk(path):
        for nm in files:
            n.append(os.path.join(top, nm))
    return n


def parseXmlfile(fil):
    with open(fil, 'rt') as f:
        tree = ElementTree.parse(f)
    return tree


