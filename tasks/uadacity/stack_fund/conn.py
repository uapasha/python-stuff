from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine ('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# import psycopg2

# class DB(object):
# 	"""Class for connection to DB"""
# 	def __init__(self, db_con_string = 'restaurantmenu'):
# 		"""Createes a database connection. Connection string 
# 			can be provided as a parameter
# 		:param str db_con_string: database connection string. 
# 			Default parameter is restaurant menu database"""
# 		self.connect = psycopg2.connect(db_con_string)
	
# 	def cursor(self):
# 		""" provides cursor for executing queries in DB"""
# 		return self.connect.cursor()

# 	def execute(self, sql_query_string, parameters_tuple = None, end_close = False):
# 		"""Executes sql queries on DB
# 		:param str sql_query_string: provides sql query as a string
# 		:param tup parameters_tuple: Optional. Contains tuple with parameters
# 			 as a python variables for sql query
# 		:param end_close bool: Optional. Boolean parameter that defines wheather 
# 			to close connection to DB after query is executed
# 		Returns dictionary with DB connection(connect) and cursor(cursor) """
# 		cursor = self.cursor()
# 		cursor.execute(sql_query_string, parameters_tuple)
		
# 		if end_close:
# 			self.connect.commit()
# 			self.connect.close()
		
# 		return {"connect": self.connect, "cursor":cursor if not end_close else None)