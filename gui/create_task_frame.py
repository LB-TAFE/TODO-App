import tkinter

class CreateTaskFrame(tkinter.Frame):

    def __init__(self):
        super().__init__()
        self.background = "#141414"
        self.label_background = "#36454F"
        self.entry_background = "#3b3b3b"
        self.tk_setPalette(background=self.background)

        self.title_label = tkinter.Label(self, text="Title", background=self.label_background, highlightbackground=self.background, highlightcolor=self.background, border=1)
        self.title_label.place(x=100, y=50, width=100, height=50)
        self.title_entry = tkinter.Entry(self, background=self.entry_background, readonlybackground=self.entry_background)
        self.title_entry.place(x=100, y=100, width=100, height=50)

        self.content_label = tkinter.Label(self, text="Content", background=self.label_background, highlightbackground=self.background, highlightcolor=self.background, border=1)
        self.content_label.place(x=200, y=50, width=300, height=50)
        self.content_entry = tkinter.Text(self, background=self.entry_background, font=("Arial", 10))
        self.content_entry.place(x=200, y=100, width=300, height=50)

        self.due_by_label = tkinter.Label(self, text="Due By", background=self.label_background, border=1, highlightbackground=self.background, highlightcolor=self.background)
        self.due_by_label.place(x=450, y=50, width=100, height=50)
        self.due_by_entry = tkinter.Entry(self, background=self.entry_background, readonlybackground=self.entry_background)
        self.due_by_entry.place(x=450, y=100, width=100, height=50)

        self.create_button = tkinter.Button(self, command=self.create, text="Create", background="#AFE1AF")
        self.create_button.place(x=100, y=200, width=100, height=50)

    def render(self):

        self.master.view_frame.place_forget()
        self.master.edit_task_frame.place_forget()
        self.place(x=100, y=0, width=700, height=600)
        self.title_entry.config(state="normal")

    def create(self):
        title = self.title_entry.get()
        content = self.content_entry.get(1.0, tkinter.END)
        due_by = self.due_by_entry.get()
        self.master.database_handler.create_task(title, content, due_by)

        self.title_entry.delete(0, tkinter.END)
        self.content_entry.delete(1.0, tkinter.END)
        self.due_by_entry.delete(0, tkinter.END)
        self.master.sidebar.show_all_tasks_pressed()




