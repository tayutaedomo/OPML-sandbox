import sys
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        xml = f.read()
        tree = ET.ElementTree(ET.fromstring(xml))
        root = tree.getroot()

        print(xml)
        print(root.tag)
