import fileDB
import fileAccess
FILENAME = ''

if __name__ == '__main__':
	FILENAME = input('Enter name of text file: ')
	print('Choose database (Will create a new database if yours does not already exist)')
	database = input('Enter the name of the database: ')
	f1 = fileAccess.File(FILENAME)
	file_name = FILENAME[:-4]
	print('Total number of unique words in this file:',f1.get_words())
	fileDBIn = fileDB.FileDB(file_name, f1.get_words(), database)
	fileDBIn.dbInput()
