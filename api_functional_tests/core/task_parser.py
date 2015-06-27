import json
from task_model import Task

class ResponseParser:

	@classmethod
	def get_task(cls, raw_response):
		if raw_response.status_code != 200:
			raise AssertionError('Invalid status code {} != 200'
								.format(raw_response.status_code))
		try:
			_text = json.loads(raw_response.text)
			_description = _text['task']['description']
			_title = _text['task']['title']
			_status = _text['task']['status']
			_uri = _text['task']['uri']
			_id = _text['task']['uri'].split('/')[-1]
			return Task(title=_title, description=_description, task_id=_id, 
						status=_status, uri=_uri)

		except Exception:
			raise AssertionError('Parsing response failed.')