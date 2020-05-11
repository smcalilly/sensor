import sqlite3

LOCATION = '../database.db'
# db = Database(LOCATION)

class Database:
    def __init__(self, location):
        self.location = self._set_location(location)
        self.connection = self._init_connection()


    def _set_location(self, location):
        if location:
            return location
        else:
            print('no location set')
            
            
    def _init_connection(self):
        try:
            return sqlite3.connect(self.location)
        except Exception as err:
            print(err)
            
            
    def _close_connection(self):
        return self.connection.close()
    
    def _commit(self):
        return self.connection.commit()
            
    
    def query(self, query):
        """ Queries the database and returns a list of items. """
        items = []
        
        cursor = self.connection.cursor()
        for row in cursor.execute(query):
            items.append(row)
            
        self._close_connection()
        
        return items
    
    def update(self, operation):
        """Inserts into the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execution(operation['operation'], operation['args'])
            self._commit()
            self._close_connection()
        except Exception as err:
            print(err)
        