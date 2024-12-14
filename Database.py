import pymysql
from pymysql.cursors import DictCursor

host = "193.200.74.36"
user = "sammy"
password = "Yasenok202"
db = "bunker"
table_name = "members"

class Connect:
    def __init__(self, userid):
        self.conn = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.userid = userid
        self.cursor = self.conn.cursor()
        self.cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        result = self.cursor.fetchone()
        if result is None:
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                                                   id INT AUTO_INCREMENT PRIMARY KEY,
                                                   userid TEXT,
                                                   role TEXT,
                                                   count_preds TEXT
                                                   )''')

    def __del__(self):
        self.conn.close()

    def AddUser(self, role):
        self.cursor.execute(f"INSERT INTO {table_name} (userid, role) VALUES (%s, %s)", (self.userid, role))
        self.conn.commit()

    def ReadRole(self):
        self.cursor.execute(f"SELECT role FROM {table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()
        if result is not None:
            result = result["role"]
        return result

    def IfUser(self):
        self.cursor.execute(f"SELECT userid FROM {table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()
        return result

    def DelRole(self):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE userid = %s", (self.userid,))
        self.conn.commit()

    def ReadCountPreds(self):
        self.cursor.execute(f"SELECT count_preds FROM {table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()["count_preds"]
        if result is None:
            result = 0
        return result

    def AddPred(self, count):
        self.cursor.execute("UPDATE members SET count_preds = %s WHERE userid = %s", (count, self.userid,))
        self.conn.commit()

    def ReadAllId(self):
        self.cursor.execute(f"SELECT userid FROM {table_name}")
        res = self.cursor.fetchall()
        return res

    def DelRoleRole(self, role):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE role = %s", (role,))
        self.conn.commit()