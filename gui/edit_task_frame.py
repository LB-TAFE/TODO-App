import tkinter

class EditTaskFrame(tkinter.Frame):
    def __init__(self):
        super().__init__()
        self.tk_setPalette(background="#141414", foreground="#FFFFFF")

        self.selected_task_id = 1

        self.title_label = tkinter.Label(self, text="Title")
        self.title_label.pack()

        self.content_label = tkinter.Label(self, text="Content")
        self.content_label.pack()

        self.due_by_label = tkinter.Label(self, text="Due By")
        self.due_by_label.pack()

        self.edit_button = tkinter.Button(self, text="Edit")
        self.edit_button.pack()

        self.save_button = tkinter.Button(self, text="Save")
        self.save_button.pack()

        self.delete_button = tkinter.Button(self, text="Delete")
        self.delete_button.pack()


    def render(self, id, title, content, due_by):
        self.selected_task_id = id
        self.title_label.config(text=title)
        self.content_label.config(text=content)
        self.due_by_label.config(text=due_by)

        self.master.view_frame.place_forget()
        self.place(x=100, y=0, width=700, height=600)
    

