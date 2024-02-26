import sqlite3

class VocabularyDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS spanish_words (
                id INTEGER PRIMARY KEY,
                spanish TEXT,
                english TEXT
            )
        ''')
        self.conn.commit()

    def fetch_random_word(self):
        self.cursor.execute("SELECT spanish, english FROM spanish_words ORDER BY RANDOM() LIMIT 1")
        return self.cursor.fetchone()

    def insert_word(self, spanish, english):
        self.cursor.execute("INSERT INTO spanish_words (spanish, english) VALUES (?, ?)", (spanish, english))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#create an instance of vocabdatabase
db = VocabularyDatabase("test_database.db")

#insert a word into the database
db.insert_word("Hola", "Hello")
db.insert_word("Guapa", "Beautiful")

#Optionally, fetch and print a random word
random_word = db.fetch_random_word()

#cleanup (close database connection)
del db

