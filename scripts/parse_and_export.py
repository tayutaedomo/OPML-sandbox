from dataclasses import dataclass
import sys
from typing import Optional
import xml.etree.ElementTree as ET


@dataclass
class RssOutline:
    text: str
    html_url: str
    xml_url: str
    tag: Optional[str]


def parse_opml_outlines(file_path: str) -> list[RssOutline]:
    with open(file_path, "r") as f:
        xml = f.read()
        tree = ET.ElementTree(ET.fromstring(xml))
        root = tree.getroot()
        outlines = root.findall("body/outline")

        rss_outlines = []
        for outline in outlines:
            if outline.get("type") == "rss":
                rss_outlines.append(parse_outline(outline))
            else:
                for nested_outline in outline:
                    rss_outline = parse_outline(nested_outline) 
                    rss_outline.tag = outline.get("text")
                    rss_outlines.append(rss_outline)

        return rss_outlines


def parse_outline(outline: ET.Element) -> RssOutline:
    text = outline.get("text")
    html_url = outline.get("htmlUrl")
    xml_url = outline.get("xmlUrl")
    return RssOutline(text, html_url, xml_url, None)


if __name__ == "__main__":
    file_path = sys.argv[1]
    rss_outlines = parse_opml_outlines(file_path)

    print(f"tag\ttext\thtml_url\txml_url") # Header
    for outline in rss_outlines:
        print(f"{outline.tag}\t{outline.text}\t{outline.html_url}\t{outline.xml_url}")
