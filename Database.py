import pymysql

import Constant

host = "193.200.74.36"
user = "sammy"
database = "rk"
password = "Yasenok202"

class Connect:
    def __init__(self, userid, chatid):
        self.conn = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.table_name = Constant.rk[chatid]
        self.userid = userid
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} (
                                                id INT AUTO_INCREMENT PRIMARY KEY,
                                                userid TEXT,
                                                role TEXT,
                                                count_preds TEXT
                                                )''')

    def __del__(self):
        self.conn.close()

    def AddUser(self, role):
        self.cursor.execute(f"INSERT INTO {self.table_name} (userid, role) VALUES (%s, %s)", (self.userid, role))
        self.conn.commit()

    def ReadRole(self):
        self.cursor.execute(f"SELECT role FROM {self.table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()
        if result is not None:
            result = result["role"]
        return result

    def IfUser(self):
        self.cursor.execute(f"SELECT userid FROM {self.table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()
        return result

    def DelRole(self):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE userid = %s", (self.userid,))
        self.conn.commit()

    def ReadCountPreds(self):
        self.cursor.execute(f"SELECT count_preds FROM {self.table_name} WHERE userid = %s", (self.userid,))
        result = self.cursor.fetchone()["count_preds"]
        if result is None:
            result = 0
        return result

    def AddPred(self, count):
        self.cursor.execute(f"UPDATE {self.table_name} SET count_preds = %s WHERE userid = %s", (count, self.userid,))
        self.conn.commit()

    def ReadAllId(self):
        self.cursor.execute(f"SELECT userid FROM {self.table_name}")
        res = self.cursor.fetchall()
        return res

    def DelRoleRole(self, role):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE role = %s", (role,))
        self.conn.commit()