import pytest
from test1.main import Secretery, documents, directories
secretery = Secretery('Bill', '1234567')


class TestDocs:

    @pytest.mark.parametrize("number,result", [('2207 876234', 'Василий Гупкин'), ('11-2', 'Геннадий Покемонов'),
                                               ('10006', 'Аристарх Павлов'), ('102', None)])
    def test_number_name(self, number, result):
        assert secretery.get_number_name(number) == result


    @pytest.mark.parametrize("number,result", [('2207 876234', '1'), ('11-2', '1'),
                                              ('10006', '2'), ('12345', None)])
    def test_number_dir(self, number, result):
        assert secretery.get_number_dir(number) == result


    def test_all_list(self):
        assert secretery.get__all_list() == ['passport "2207 876234" "Василий Гупкин"',
                                             'invoice "11-2" "Геннадий Покемонов"',
                                             'insurance "10006" "Аристарх Павлов"']


    def test_add_doc(self):
        assert secretery.add_doc('паспорт', '10', 'Милана Минаева', '2') == {'type': 'паспорт', 'number': '10', 'name': 'Милана Минаева'} == documents[-1]
        assert '10' in directories['2']
        assert secretery.add_doc('паспорт', '11', 'Михаил Шиндяев', '7') == None