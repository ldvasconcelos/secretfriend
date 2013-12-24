#coding: utf-8
class Person:
	def __init__(self, name, email, gifts, restrictions):
		self.name = name
		self.email = email
		self.gifts = gifts
		self.restrictions = restrictions

	def __repr__(self):
		return repr((self.name, self.email, self.gifts, self.restrictions))