#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
	def __init__(self):
		"""Instantiate a new object with a
		unique id and the time of creation or
		update"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()


	def __str__(self):
		"""String method for object"""
		return '[{}] ({}) {}'.format(
			self.__class__.__name__,
			self.id,
			self.__dict__)
