import sqlite3

from prettytable import from_db_cursor

from .people_class import People

from .__init__ import data, data_str

class DataBase:

  def __init__(self, db: str, table: str = 'users'):

    self.conn = sqlite3.connect(db)

    self.cur = self.conn.cursor()

    self.db = db

    self.table = table

  

  def append(self,values: list, name_table: str = 'users'):

    self.cur.execute(f"""INSERT INTO {name_table} VALUES({','.join(['"' + str(t) + '"' for t in values])});""")

    self.conn.commit()

  def append_column(self, name_column: str, type_column: str,  name_table: str = 'users'):

    

    self.cur.execute(f"alter table {name_table} add column {name_column} '{type_column}'")

    self.conn.commit()

  def new_people(self, msg):

    if not self.is_there(msg.from_user.id):

      self.append(eval(data_str))

  def delete_column(self, name_table: str = 'users', columns: list = ['userid','fname','money']):

    columns = ','.join(columns)

    for request in [f"CREATE TABLE new_table AS SELECT {columns} FROM {name_table};",f"INSERT INTO new_table SELECT {columns} FROM {name_table};",f"DROP TABLE {name_table};",f"ALTER TABLE new_table RENAME TO {name_table};"]:

     self.cur.execute(request)

     self.conn.commit()

  def delete(self, id: int, name_table: str = 'users'):

    self.cur.execute(f"""DELETE from {name_table} where id = {id}""")

    self.conn.commit()

  def is_there(self, id: int, name_table: str = 'users') -> bool:

    self.cur.execute(f'SELECT * FROM {name_table} WHERE id = ?',[id])

    return True if len(self.cur.fetchall()) > 0 else False

  def update(self, key1: str, value1: str, key2: str, value2: str, name_table: str = 'users'):

    self.cur.execute(f"UPDATE {name_table} SET {key2} = '{value2}' WHERE {key1} = '{value1}' ")

    self.conn.commit()

  def create_table(self, param: dict, name_table: str = 'users'):

    """Пример создания таблицы CREATE TABLE IF NOT EXISTS users(

    userid INT PRIMARY KEY,

    fname TEXT,

    lname TEXT,

    gender TEXT);

    """

    self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}({','.join([t + ' ' + param[t] for t in param])});""")

    self.conn.commit()

  def read_table(self, param = None, name_table: str = 'users') -> str:

    try:

        self.cur.execute(f"SELECT {','.join(param) if param else '*'} FROM {name_table}")

        mytable = from_db_cursor(self.cur)

        

        return str(mytable)

    except sqlite3.Error as error:

        return error

  def saw_tables(self):

    self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    return self.cur.fetchall()

  def select(self, id: int, param: str = '*', name_table: str = 'users') -> None:

    self.cur.execute(f'SELECT {param} FROM {name_table} WHERE id = {id}')

    

    return People(*self.cur.fetchall()[0])import sqlite3

from prettytable import from_db_cursor

from .people_class import People

from .__init__ import data, data_str

class DataBase:

  def __init__(self, db: str, table: str = 'users'):

    self.conn = sqlite3.connect(db)

    self.cur = self.conn.cursor()

    self.db = db

    self.table = table

  

  def append(self,values: list, name_table: str = 'users'):

    self.cur.execute(f"""INSERT INTO {name_table} VALUES({','.join(['"' + str(t) + '"' for t in values])});""")

    self.conn.commit()

  def append_column(self, name_column: str, type_column: str,  name_table: str = 'users'):

    

    self.cur.execute(f"alter table {name_table} add column {name_column} '{type_column}'")

    self.conn.commit()

  def new_people(self, msg):

    if not self.is_there(msg.from_user.id):

      self.append(eval(data_str))

  def delete_column(self, name_table: str = 'users', columns: list = ['userid','fname','money']):

    columns = ','.join(columns)

    for request in [f"CREATE TABLE new_table AS SELECT {columns} FROM {name_table};",f"INSERT INTO new_table SELECT {columns} FROM {name_table};",f"DROP TABLE {name_table};",f"ALTER TABLE new_table RENAME TO {name_table};"]:

     self.cur.execute(request)

     self.conn.commit()

  def delete(self, id: int, name_table: str = 'users'):

    self.cur.execute(f"""DELETE from {name_table} where id = {id}""")

    self.conn.commit()

  def is_there(self, id: int, name_table: str = 'users') -> bool:

    self.cur.execute(f'SELECT * FROM {name_table} WHERE id = ?',[id])

    return True if len(self.cur.fetchall()) > 0 else False

  def update(self, key1: str, value1: str, key2: str, value2: str, name_table: str = 'users'):

    self.cur.execute(f"UPDATE {name_table} SET {key2} = '{value2}' WHERE {key1} = '{value1}' ")

    self.conn.commit()

  def create_table(self, param: dict, name_table: str = 'users'):

    """Пример создания таблицы CREATE TABLE IF NOT EXISTS users(

    userid INT PRIMARY KEY,

    fname TEXT,

    lname TEXT,

    gender TEXT);

    """

    self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}({','.join([t + ' ' + param[t] for t in param])});""")

    self.conn.commit()

  def read_table(self, param = None, name_table: str = 'users') -> str:

    try:

        self.cur.execute(f"SELECT {','.join(param) if param else '*'} FROM {name_table}")

        mytable = from_db_cursor(self.cur)

        

        return str(mytable)

    except sqlite3.Error as error:

        return error

  def saw_tables(self):

    self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    return self.cur.fetchall()

  def select(self, id: int, param: str = '*', name_table: str = 'users') -> None:

    self.cur.execute(f'SELECT {param} FROM {name_table} WHERE id = {id}')

    

    return People(*self.cur.fetchall()[0])
