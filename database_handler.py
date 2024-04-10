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
        VALUES ('{title}', '{content}', '{due_by}')
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
        SET '{field}' = '{value}'
        WHERE id = {id}
        """

        self.cursor.execute(sql)
        self.cursor.commit()

    def edit_full_task(self, id, title, content, due_by):
        self.connect()
        sql = f"""
        UPDATE tasks
        SET 'title' = '{title}', 'content' = '{content}', 'due_by' = '{due_by}'
        WHERE id = {id}
        """

        self.cursor.execute(sql)
        self.connection.commit()



if __name__ == "__main__":
    handler = DatabaseHandler()
    print(handler.get_tasks())
    handler.create_tasks_table()
    handler.create_task("Title", "Content", "2023-01-01 00:00:00")
    handler.create_task("Title Two", "Content Two", "2024-01-01 00:00:00")
    handler.create_task("Title Three", "Content Three", "2024-06-01 00:00:00")
    print(handler.get_tasks())
    