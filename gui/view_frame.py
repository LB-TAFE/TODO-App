import tkinter
from datetime import datetime


class ViewFrame(tkinter.Frame):
    def __init__(self):
        super().__init__()
        
        self.tk_setPalette(background="#141414", foreground="#FFFFFF")
        self.buttons = []
        self.render_all()

    def render_all(self):
        for button in self.buttons:
            button.grid_forget()
        self.buttons = []
        row = 0
        column = 0
        for task in self.master.database_handler.get_tasks():
            colour = "#006400"
            if self.check_if_overdue(task):
                colour = "#DE3163"
            def on_click(task):
                self.last_clicked = task[0]
                self.master.edit_task_frame.render(task[0], task[1], task[2], task[3])
            
            button = tkinter.Button(self, text=f"{task[1]}\n\nDue by: {task[3]}", command=lambda record=task: on_click(record), background=colour)
            button.grid(row=row, column=column, sticky="ew")
            column += 1
            if column >= 4:
                column = 0
                row += 1
            self.buttons.append(button)
        self.place(x=150, y=0, width=650, height=600)

    def render_upcoming(self):
        for button in self.buttons:
            button.grid_forget()
        self.buttons = []
        row = 0
        column = 0
        for task in self.master.database_handler.get_tasks():
            if self.check_if_overdue(task):
                continue
            def on_click(task):
                self.last_clicked = task[0]
                self.master.edit_task_frame.render(task[0], task[1], task[2], task[3])
            
            button = tkinter.Button(self, text=f"{task[1]}\n\nDue by: {task[3]}", command=lambda record=task: on_click(record), background="#006400")
            button.grid(row=row, column=column, sticky="ew")
            column += 1
            if column >= 4:
                column = 0
                row += 1
            self.buttons.append(button)
        self.place(x=150, y=0, width=650, height=600)


    def render_overdue(self):
        for button in self.buttons:
            button.grid_forget()
        self.buttons = []
        row = 0
        column = 0
        for task in self.master.database_handler.get_tasks():
            if not self.check_if_overdue(task):
                continue
            def on_click(task):
                self.last_clicked = task[0]
                self.master.edit_task_frame.render(task[0], task[1], task[2], task[3])
            
            button = tkinter.Button(self, text=f"{task[1]}\n\nDue by: {task[3]}", command=lambda record=task: on_click(record), background="#DE3163")
            button.grid(row=row, column=column, sticky="ew")
            column += 1
            if column >= 4:
                column = 0
                row += 1
            self.buttons.append(button)
        self.place(x=150, y=0, width=650, height=600)



    
    def check_if_overdue(self, task):
        task_due_by = datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S")
        if task_due_by < datetime.now():
            return True
        return False