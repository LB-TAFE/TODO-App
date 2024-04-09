import tkinter


class ViewFrame(tkinter.Frame):
    def __init__(self):
        super().__init__()
        
        self.tk_setPalette(background="#141414", foreground="#FFFFFF")
        self.buttons = []
        self.render("all")

    def render(self, mode):
        for button in self.buttons:
            button.place_forget()
        self.buttons = []
        row = 0
        column = 0
        for task in self.master.database_handler.get_tasks():
            #print(task)
            def on_click(task):
                self.last_clicked = task[0]
                self.master.edit_task_frame.render(task[0], task[1], task[2], task[3])
                
            button = tkinter.Button(self, text=task[1], command=lambda record=task: on_click(record))
            button.grid(row=row, column=column, sticky="ew")
            column += 1
            if column > 5:
                column = 0
                row += 1
            self.buttons.append(button)
        self.place(x=200, y=0, width=600, height=600)

