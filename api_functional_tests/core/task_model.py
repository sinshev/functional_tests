"""
This module implements Task class
"""


import json

class Task:
	"""This class models 'tasks' from 'TASKS' API."""

	def __init__(self, title, description, task_id=None, status=False,
				uri=None):
		self.id = task_id
		self.title = title
		self.description = description
		self.status = status
		self.uri = uri

	def __str__(self):
		return json.dumps(self.__dict__)

	def __eq__(self, other):
		return self.title == other.title and \
				self.description == other.description

if __name__ == '__main__':
	pass