from unittest import TestCase
from custom_hashtable import HashTable


class HashTableTests(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_init(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None, None, None, None], self.table._HashTable__keys)
        self.assertEqual([None, None, None, None], self.table._HashTable__values)

    def test_get_value_if_key_doesnt_exist_return_default_none(self):
        self.table.add("name", "Ani")
        self.assertEqual(None, self.table.get("other"))

    def test_get_value_if_success(self):
        self.table.add("name", "Ani")
        self.assertEqual("Ani", self.table.get("name"))

    def test_getitem_if_key_not_exist_raise_value_error_as_key_error(self):
        with self.assertRaises(KeyError) as error:
            self.table.__getitem__("name")

        self.assertEqual("'name'", str(error.exception))

    def test_getitem_if_key_exist_return_value(self):
        self.table.add("name", "Ani")

        self.assertEqual("Ani", self.table.__getitem__("name"))

    def test_setitem_if_key_exist_set_the_new_value(self):
        self.table.add("name", "Ani")
        self.table.__setitem__("name", "Ivan")

        self.assertEqual("Ivan", self.table.__getitem__("name"))

    def test_setitem_exceed_max_capacity(self):
        self.table.add("name1", "A")
        self.table.add("name2", "B")
        self.table.add("name3", "C")
        self.table.add("name4", "D")
        self.table.__setitem__("name5", "E")

        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_setitem_successful_set_key_and_value_to_indexes(self):
        self.table.__setitem__("name1", "Ani")
        index = self.table._HashTable__calc_index("name1")
        self.assertEqual(2, index)

        result_key = self.table._HashTable__keys[2]
        result_value = self.table._HashTable__values[2]

        self.assertEqual("name1", result_key)
        self.assertEqual("Ani", result_value)

    def test_len_of_full_cells(self):
        self.table.add("name1", "A")
        self.table.add("name2", "B")

        self.assertEqual(2, len(self.table))

    def test_calc_index_if_is_int(self):
        self.table.add(1, 1)
        self.assertEqual(1, self.table._HashTable__calc_index(1))

    def test_calc_index_if_any_ascii(self):
        self.table.add("name", "A")
        self.assertEqual(1, self.table._HashTable__calc_index("name"))

    def test_get_free_index(self):
        self.table.add("A", 1)
        self.table.add("B", 2)

        self.assertEqual(3, self.table._HashTable__get_free_index(2))

    def test_get_size(self):
        self.table.add("A", 1)
        self.table.add("B", 2)
        self.assertEqual(2, self.table.get_size())

    def test_resize(self):
        self.table.add("name1", "A")
        self.table.add("name2", "B")
        self.table.add("name3", "C")
        self.table.add("name4", "D")
        self.table.add("name5", "E")

        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_str_if_is_proper(self):
        self.table.add("name", "Ani")
        expected = '{name: Ani}'

        self.assertEqual(expected, str(self.table))

    def test_str_if_is_empty(self):
        self.assertEqual("{}", str(self.table))
