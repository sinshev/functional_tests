"""

"""

import requests
import sys
import os
from task_parser import ResponseParser

if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__) + '/../')

from config import API_URL, TASK_TAIL, TASKS_TAIL
from config import DEFAULT_PASSWORD as PASSWORD
from config import DEFAULT_USERNAME as USERNAME



class TaskHandler:
	"""
	docstring
	"""

	@classmethod
	def get_task(cls, task_id, username, password):
		raw_response = requests.get(url=API_URL+TASK_TAIL+str(task_id), 
									auth=(username, password))
		return ResponseParser.get_task(raw_response)


if __name__ == "__main__":
	task_1 = TaskHandler.get_task(1, USERNAME, PASSWORD)
	print(task_1)
