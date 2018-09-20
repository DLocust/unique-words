import MySQLdb
class FileDB:
	def __init__(self, FILENAME, words, database):
		self.__FILENAME = FILENAME
		self.__words = words
		self.__database = database
	
	def set_FILENAME(self, FILENAME):
		self.__FILENAME = FILENAME
	
	def set_words(self, words):
		self.__words = words
	
	def set_database(self, database):
		self.__database = database

	def dbInput(self):
		db = MySQLdb.connect(host="localhost", user="root", passwd="")
		sql = 'CREATE DATABASE IF NOT EXISTS ' + self.__database
		cursor = db.cursor()
		cursor.execute(sql)
		use = 'Use ' + self.__database
		cursor.execute(use)
		table = 'CREATE TABLE IF NOT EXISTS Words (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), words VARCHAR(10));'
		cursor.execute(table)
		cursor.execute("INSERT INTO `Words` (`id`, `name`, `words`) VALUES (NULL, %s, %s)", (self.__FILENAME, self.__words))
		data = cursor.fetchone()
		db.query("""SELECT * FROM Words""")
		r=db.store_result()
		while True:
			row = r.fetch_row()
			if row == ():
				break
			else:
				print(row)
		db.commit()
		db.close()
