import sqlite3

class Database:
    def __init__(self, location):
        self.location = self._set_location(location)
        self.connection = self._create_connection()


    def _set_location(self, location):
        if location:
            return location
        else:
            print('no location set')
            
            
    def _create_connection(self):
        try:
            return sqlite3.connect(self.location)
        except Exception as err:
            print(err)
            
    
    def _get_attributes(self, cursor):
        cursor = self._cursor()
        table = self.location
        print(table)
        cursor.execute("PRAGMA table_info('%s')" % self.location)
        headers = cursor.fetchall()
        print(headers)
            

    def _close_connection(self):
        return self.connection.close()
    
    
    def _commit(self):
        return self.connection.commit()
    
    
    def _cursor(self):
        return self.connection.cursor()
    

    def query(self, query):
        """ Queries the database and returns a list of items. """
        items = []
            
        cursor = self._cursor()
        for row in cursor.execute(query):
            items.append(row)
            
        self._commit()
        
        return items
    
    def update(self, operation):
        """Inserts into the database"""
        try:
            cursor = self._cursor()
            cursor.execute(operation['operation'], operation['args'])
            self._commit()
        except Exception as err:
            print(err)
        