import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.connect()
        self.create_tasks_table()

    def connect(self):
        self.connection = sqlite3.connect("app.db")
        self.cursor = self.connection.cursor()

    def create_tasks_table(self):
        self.connect()
        sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            due_by TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.cursor.execute(sql)
        self.connection.commit()

    def create_task(self, title, content, due_by):
        self.connect()
        sql = f"""
        INSERT INTO tasks ('title', 'content', 'due_by')
        VALUES ('{title.replace("'", "''")}', '{content.replace("'", "''")}', '{due_by.replace("'", "''")}')
        """

        self.cursor.execute(sql)
        self.connection.commit()

    def delete_task(self, id):
        self.connect()
        sql = f"""
        DELETE FROM tasks
        WHERE id = {id}
        """

        self.cursor.execute(sql)
        self.connection.commit()

    def get_tasks(self):
        self.connect()
        sql = """
        SELECT * FROM tasks
        """

        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def edit_task(self, id, field, value):
        self.connect()
        sql = f"""
        UPDATE tasks
        SET '{field}' = '{value.replace("'", "''")}'
        WHERE id = {id}
        """

        self.cursor.execute(sql)
        self.connection.commit()

    def edit_full_task(self, id, title, content, due_by):
        self.connect()
        sql = f"""
        UPDATE tasks
        SET 'title' = '{title.replace("'", "''")}', 'content' = '{content.replace("'", "''")}', 'due_by' = '{due_by.replace("'", "''")}'
        WHERE id = {id}
        """

        self.cursor.execute(sql)
        self.connection.commit()



if __name__ == "__main__":
    handler = DatabaseHandler()
    print(handler.get_tasks())
    