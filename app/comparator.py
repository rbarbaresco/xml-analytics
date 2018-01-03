import unittest
import xml.etree.ElementTree  as ET
from app.exceptions import CompareException


class XMLComparator(unittest.TestCase):

    def __init__(self):
        super(XMLComparator, self).__init__()
        self.longMessage = True

    def compare(self, xml_1, xml_2):
        el_tree_1 = ET.fromstring(xml_1)
        el_tree_2 = ET.fromstring(xml_2)
        self._do_compare(el_tree_1, el_tree_2)

    def _do_compare(self, el_tree_1, el_tree_2):
        self._compare_tag(el_tree_1, el_tree_2)
        bigger, smaller = self._classify(el_tree_1, el_tree_2)
        for elb in bigger:
            theres_equivalent = False
            for els in smaller:
                try:
                    self._do_compare(elb, els)
                    theres_equivalent = True
                    break
                except:
                    pass
            if not theres_equivalent:
                raise CompareException('No equivalent tag for <{}>.'.format(elb.tag))

    def _compare_tag(self, el_tree_1, el_tree_2):
        self.assertEquals(el_tree_1.text, el_tree_2.text)
        self.assertDictEqual(el_tree_1.attrib, el_tree_2.attrib)

    def _classify(self, el_tree_1, el_tree_2):
        el_tree_1_children = list(el_tree_1)
        el_tree_2_children = list(el_tree_2)

        if len(el_tree_1_children) < len(el_tree_2_children):
            return el_tree_2_children, el_tree_1_children
        return el_tree_1_children, el_tree_2_children
