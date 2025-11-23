import unittest

from src.homework.i_dictionaries_sets.dictionary import (
	add_inventory,
	remove_inventory_widget,
	inventory_dictionary,
)


class Test_Config(unittest.TestCase):

	def setUp(self):
		# Ensure a clean inventory before each test
		inventory_dictionary.clear()

	def test_add_inventory(self):
		add_inventory(inventory_dictionary, "Widget1", 10)
		self.assertIn("Widget1", inventory_dictionary)
		self.assertEqual(10, inventory_dictionary["Widget1"])

		add_inventory(inventory_dictionary, "Widget1", 25)
		self.assertEqual(35, inventory_dictionary["Widget1"])  # 10 + 25

		add_inventory(inventory_dictionary, "Widget1", -10)
		self.assertEqual(25, inventory_dictionary["Widget1"])  # 35 - 10

	def test_remove_inventory_widget(self):
		add_inventory(inventory_dictionary, "widget1", 5)
		add_inventory(inventory_dictionary, "widget2", 7)

		result = remove_inventory_widget("widget1")
		self.assertEqual("Record deleted", result)
		self.assertEqual(1, len(inventory_dictionary))
		self.assertIn("widget2", inventory_dictionary)
