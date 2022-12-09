from unittest import TestCase, main

from custom_list import CustomList


class CustomListTests(TestCase):
    def setUp(self) -> None:
        self.sut = CustomList(1, 2)

    def test_append_should_add_element_at_the_end(self):
        # Act
        result = self.sut.append(3)

        # Assert
        self.assertEqual((1, 2, 3), result)

    def test_remove_should_raise_error_when_index_is_invalid(self):
        indexes = [-5, 10]
        for index in indexes:
            with self.assertRaises(Exception) as ctx:
                self.sut.remove(index)
            self.assertEqual("Invalid index!", str(ctx.exception))

    def test_remove_should_return_removed_element_when_index_is_valid(self):
        # Act
        removed_el = self.sut.remove(0)

        # Assert
        self.assertEqual(1, removed_el)
        self.assertEqual([2], self.sut._CustomList__data)

    def test_get_should_raise_error_when_idx_is_invalid(self):
        # Act
        indexes = [-10, 10]
        for index in indexes:
            with self.assertRaises(Exception) as ctx:
                self.sut.get(index)

            # Assert
            self.assertEqual("Invalid index!", str(ctx.exception))

    def test_get_should_return_element_when_idx_is_valid(self):
        # Act
        element = self.sut.get(0)

        # Assert
        self.assertEqual(1, element)

    def test_extend_should_raise_error_when_argument_is_empty(self):
        # Act
        with self.assertRaises(Exception) as ctx:
            self.sut.extend([])

        # Assert
        self.assertEqual("Empty iterable", str(ctx.exception))

    def test_extend_should_merge_data_with_iterable_when_iterable_has_elements(self):
        # Act
        result = self.sut.extend([3, 4])

        # Assert
        self.assertEqual((1, 2, 3, 4), result)
        self.assertEqual([1, 2, 3, 4, ], self.sut._CustomList__data)

    def test_insert_should_raise_error_when_idx_is_invalid(self):
        indexes = [-10, 10]
        for index in indexes:
            with self.assertRaises(Exception) as ctx:
                self.sut.insert(index, 100)
            self.assertEqual("Invalid index", str(ctx.exception))

    def test_insert_should_add_element_at_the_end_when_idx_is_after_the_last_el(self):
        # Act
        result = self.sut.insert(2, 10)

        # Assert
        self.assertEqual((1, 2, 10), result)
        self.assertEqual([1, 2, 10], self.sut._CustomList__data)

    def test_insert_should_add_element_at_given_idx(self):
        # Act
        result = self.sut.insert(1, 10)

        # Assert
        self.assertEqual((1, 10, 2), result)
        self.assertEqual([1, 10, 2], self.sut._CustomList__data)

    def test_pop_should_raise_error_when_list_is_empty(self):
        # Arrange
        sut = CustomList()

        # Act
        with self.assertRaises(Exception) as ctx:
            sut.pop()

        # Assert
        self.assertEqual("The custom list is empty", str(ctx.exception))

    def test_pop_should_remove_last_element(self):
        # Act
        removed_el = self.sut.pop()

        # Assert
        self.assertEqual(2, removed_el)
        self.assertEqual([1], self.sut._CustomList__data)

    def test_clear_should_remove_all_elements(self):
        # Act
        self.sut.clear()

        # Assert
        self.assertEqual([], self.sut._CustomList__data)

    def test_index_should_return_default_value_when_element_does_not_exist(self):
        # Act
        idx = self.sut.index(100)

        # Assert
        self.assertEqual(-1, idx)

    def test_index_should_return_element_idx_when_exists(self):
        # Act
        idx = self.sut.index(2)

        # Assert
        self.assertEqual(1, idx)

    def test_reverse_should_return_elements_in_reverse_order(self):
        # Act
        reversed_result = self.sut.reverse()

        # Assert
        self.assertEqual([2, 1], reversed_result)
        self.assertEqual([1, 2], self.sut._CustomList__data)

    def test_copy_should_return_new_list_instance(self):
        # Act
        copy_result = self.sut.copy()

        # Assert
        self.assertEqual([1, 2], copy_result)

        copy_result.append(3)

        self.assertNotEqual(copy_result, self.sut._CustomList__data)

    def test_count_should_return_element_occurrences_when_element_exists(self):
        # Arrange
        sut = CustomList(1, 2, 1, 2, 2)

        # Act
        count = sut.count(2)

        # Arrange
        self.assertEqual(3, count)

    def test_count_should_return_zero_when_element_does_not_exist(self):
        # Act
        count = self.sut.count(10)

        # Arrange
        self.assertEqual(0, count)

    def test_size_should_return_elements_number(self):
        # Act
        size = self.sut.size()

        # Assert
        self.assertEqual(2, size)

    def test_add_first_should_add_element_at_the_start_of_the_seq(self):
        # Act
        result = self.sut.add_first(0)

        # Assert
        self.assertEqual((0, 1, 2), result)
        self.assertEqual([0, 1, 2], self.sut._CustomList__data)

    def test_dictionize_should_return_empty_dict_when_lsit_is_empty(self):
        # Arrange
        sut = CustomList()

        # Act
        result = sut.dictionize()

        # Assert
        self.assertEqual({}, result)

    def test_dictionize_should_return_even_pairs_when_list_count_is_even_number(self):
        # Arrange
        sut = CustomList(1, 2, 3, 4, 5, 6)
        expected_result = {1: 2, 3: 4, 5: 6}

        # Act
        result = sut.dictionize()

        # Assert
        self.assertEqual(expected_result, result)

    def test_dictionize_should_return_default_value_for_last_key_when_list_length_is_odd(self):
        # Arrange
        sut = CustomList(1, 2, 3, 4, 5)
        expected_result = {1: 2, 3: 4, 5: ' '}

        # Act
        result = sut.dictionize()

        # Assert
        self.assertEqual(expected_result, result)

    def test_move_should_reposition_first_n_elements_at_the_end(self):
        # Arrange
        sut = CustomList(1, 2, 3, 4, 5)

        # Act
        result = sut.move(2)

        # Assert
        self.assertEqual((3, 4, 5, 1, 2), result)
        self.assertEqual([3, 4, 5, 1, 2], sut._CustomList__data)

    def test_sum_should_sum_all_elements(self):
        # Arrange
        sut = CustomList(1, 2, 3, 'abc', [1, 2])

        # Act
        result = sut.sum()

        # Assert
        self.assertEqual(11, result)

    def test_overbound_should_return_max_number_in_list(self):
        # Arrange
        sut = CustomList('abcd', 1, 2, 3)

        # Act
        result = sut.overbound()

        # Assert
        self.assertEqual(0, result)

    def test_underbound_should_return_min_number_in_list(self):
        sut = CustomList('abcd', 'a', 2, 3)

        # Act
        result = sut.underbound()

        # Assert
        self.assertEqual(1, result)

if __name__ == '__main__':
    main()
