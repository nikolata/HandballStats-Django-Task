#collect_fractions_test

import unittest
from collect_fractions import validate_entry


class TestInputValidation(unittest.TestCase):
	def test_if_fraction_is_list_of_tuples_should_return_error(self):
		l = [(1),2]
		result = None
		try:
			validate_entry(l)
		except Exception as err:
			result = err

		self.assertIsNotNone(result)
		self.assertEqual(str(result), 'We need list of tuples!')


	def test_if_fraction_is_empty_should_return_error(self):
		l = [(1,2)]

		result = None
		try:
			validate_entry(l)
		except Exception as err:
			result = err

		self.assertIsNotNone(result)
		self.assertEqual(str(result), 'We need 2 tuples')

	def test_if_fractions_have_two_elements_should_return_error(self):
		l = [(1,),(3,2)]
		result = None

		try:
			validate_entry(l)
		except Exception as err:
			result = err
		self.assertIsNotNone(result)
		self.assertEqual(str(result), 'Tuples need 2 elements')






if __name__ == '__main__':
	unittest.main()