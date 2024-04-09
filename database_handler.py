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



if __name__ == "__main__":
    handler = DatabaseHandler()
    print(handler.get_tasks())
    handler.create_tasks_table()
    handler.create_task("Title", "Content", "Due By")
    handler.create_task("Title Two", "Content Two", "Due By Two")
    handler.create_task("Title Three", "Content Three", "Due By Three")
    handler.create_task("Title Four", "Content Four", "Due By Four")
    handler.create_task("Title Five", "Content Five", "Due By Five")
    handler.create_task("Title Six", "Content Six", "Due By Six")
    handler.create_task("Title Seven", "Content Seven", "Due By Seven")
    handler.create_task("Title Eight", "Content Eight", "Due By Eight")
    handler.create_task("Title Nine", "Content Nine", "Due By Nine")
    handler.create_task("Title Ten", "Content Ten", "Due By Ten")
    handler.create_task("Title Eleven", "Content Eleven", "Due By Eleven")
    print(handler.get_tasks())
    
