import unittest
from app.comparator import XMLComparator


class XMLComparatorTest(unittest.TestCase):

    def setUp(self):
        self.longMessage = True
        self.comparator = XMLComparator()

    def test_nao_deveria_lancar_excessao_com_uma_tag_igual(self):
        xml_1 = '<pai atributo="valor">texto</pai>'
        xml_2 = '<pai atributo="valor">texto</pai>'
        self.comparator.compare(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_a_tag_nao_for_igual(self):
        xml_1 = '<pai atributo="valor">texto</pai>'
        xml_2 = '<paidiff atributo="valor">texto</paidiff>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_o_nome_do_atributo_nao_for_igual(self):
        xml_1 = '<pai atributo="valor">texto</pai>'
        xml_2 = '<pai atributodiff="valor">texto</pai>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_o_valor_do_atributo_nao_for_igual(self):
        xml_1 = '<pai atributo="valor diferente">texto</pai>'
        xml_2 = '<pai atributo="valor">texto</pai>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_o_texto_nao_for_igual(self):
        xml_1 = '<pai atributo="valor">texto</pai>'
        xml_2 = '<pai atributo="valor">texto diferente</pai>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_um_tiver_filho_e_o_outro_nao(self):
        xml_1 = '<pai atributo="valor">texto</pai>'
        xml_2 = '<pai atributo="valor">texto<filho></filho></pai>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_um_tiver_filho_e_o_atributo_for_diferente(self):
        xml_1 = '<pai atributo="valor">texto<filho attr_filho="valor"></filho></pai>'
        xml_2 = '<pai atributo="valor">texto<filho></filho></pai>'
        self.assert_raises(xml_1, xml_2)

    def test_deveria_lancar_excessao_quando_um_tiver_neto_e_o_outro_nao(self):
        xml_1 = '<pai atributo="valor">texto<filho></filho></pai>'
        xml_2 = '<pai atributo="valor">texto<filho><neto></neto></filho></pai>'
        self.assert_raises(xml_1, xml_2)

    def assert_raises(self, xml_1, xml_2):
        with self.assertRaises(Exception) as error:
            self.comparator.compare(xml_1, xml_2)
        print(str(error.exception))
