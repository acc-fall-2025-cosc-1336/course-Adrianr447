"""Inventory dictionary utilities for HW09.

Provides a module-level `inventory_dictionary` and two functions:
- `add_inventory(widgets, widget_name, quantity)` modifies the provided
	dictionary in-place (no return value).
- `remove_inventory_widget(widget_name)` removes the named widget from the
	module-level `inventory_dictionary` and returns a status string.
"""

inventory_dictionary = {}


def add_inventory(widgets, widget_name, quantity):
		"""Add or update an inventory item.

		Parameters
		- widgets: dict mapping item name -> quantity
		- widget_name: str name of the widget to add/update
		- quantity: int amount to add (may be negative)

		This function mutates `widgets` in-place and returns None.
		"""
		if widget_name in widgets:
				widgets[widget_name] += quantity
		else:
				widgets[widget_name] = quantity


def remove_inventory_widget(widget_name):
		"""Remove `widget_name` from the module-level inventory.

		Returns 'Record deleted' if removed, otherwise 'Item not found'.
		"""
		if widget_name in inventory_dictionary:
				del inventory_dictionary[widget_name]
				return "Record deleted"
		return "Item not found"
