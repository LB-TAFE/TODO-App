import tkinter
from datetime import datetime

class EditTaskFrame(tkinter.Frame):
    def __init__(self):
        super().__init__()
        self.background = "#141414"
        self.label_background = "#36454F"
        self.entry_background = "#3b3b3b"
        self.tk_setPalette(background=self.background)

        self.selected_task_id = 1

        self.title_label = tkinter.Label(self, text="Title", background=self.label_background, highlightbackground=self.background, highlightcolor=self.background, border=1)
        self.title_label.place(x=100, y=50, width=100, height=50)
        self.title_entry = tkinter.Entry(self, background=self.entry_background, readonlybackground=self.entry_background)
        self.title_entry.place(x=100, y=100, width=100, height=50)

        self.content_label = tkinter.Label(self, text="Content", background=self.label_background, highlightbackground=self.background, highlightcolor=self.background, border=1)
        self.content_label.place(x=200, y=50, width=300, height=50)
        self.content_entry = tkinter.Text(self, background=self.entry_background, font=("Arial", 10))
        self.content_entry.place(x=200, y=100, width=300, height=50)

        self.due_by_label = tkinter.Label(self, text="Due By", background=self.label_background, border=1, highlightbackground=self.background, highlightcolor=self.background)
        self.due_by_label.place(x=450, y=50, width=110, height=50)
        self.due_by_entry = tkinter.Entry(self, background=self.entry_background, readonlybackground=self.entry_background, font=("Arial", 8))
        self.due_by_entry.place(x=450, y=100, width=110, height=50)

        self.edit_button = tkinter.Button(self, command=self.enable_edit, text="Edit", background="#FFA500")
        self.edit_button.place(x=100, y=200, width=100, height=50)

        self.save_button = tkinter.Button(self, command=self.save, text="Save", background="#AFE1AF")
        self.save_button.place(x=200, y=200, width=100, height=50)

        self.delete_button = tkinter.Button(self, command=self.delete, text="Delete", background="#880808")
        self.delete_button.place(x=300, y=200, width=100, height=50)




    def render(self, id, title, content, due_by):
        self.selected_task_id = id
        self.title_entry.config(state="normal")
        self.content_entry.config(state="normal")
        self.due_by_entry.config(state="normal")
        
        self.title_entry.delete(0, tkinter.END)
        self.title_entry.insert(0, title)

        self.content_entry.delete(1.0, tkinter.END)
        self.content_entry.insert(1.0, content)

        self.due_by_entry.delete(0, tkinter.END)
        self.due_by_entry.insert(0, due_by)

        self.master.view_frame.place_forget()
        self.place(x=100, y=0, width=700, height=600)

        self.save_button.config(state="disabled")
        self.title_entry.config(state="readonly")
        self.content_entry.config(state="disabled")
        self.due_by_entry.config(state="readonly")
        self.edit_button.config(state="normal")
        self.edit_button.config(text="Edit")
        self.save_button.config(text="Save")
        
    
    def enable_edit(self):
        self.edit_button.config(text="Editing")
        self.edit_button.config(state="disabled")
        self.save_button.config(text="Save")
        self.save_button.config(state="normal")
        self.title_entry.config(state="normal")
        self.content_entry.config(state="normal")
        self.due_by_entry.config(state="normal")

    def save(self):
        title = self.title_entry.get()
        if title.strip(" ") == "":
            self.title_warning()
            return
        due_date = self.turn_into_date_string(self.due_by_entry.get())
        if not self.validate_date(self.turn_into_date_string(self.due_by_entry.get())):
            self.invalid_date_warning()
            return
        self.save_button.config(state="disabled")
        self.title_entry.config(state="readonly")
        self.content_entry.config(state="disabled")
        self.due_by_entry.config(state="readonly")
        self.save_button.config(text="Saved")
        self.edit_button.config(state="normal")
        self.edit_button.config(text="Edit")

        self.master.database_handler.edit_full_task(self.selected_task_id, title, self.content_entry.get(1.0, tkinter.END), due_date)

    def delete(self):
        self.master.database_handler.delete_task(self.selected_task_id)
        self.master.sidebar.show_all_tasks_pressed()

    def validate_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            return True
        except:
            return False
        
    def turn_into_date_string(self, date):
        split_date = date.split(" ")
        if len(split_date) == 1 or split_date[1] == "":
            return f"{date} 00:00:00"
        
        return date
    
    def invalid_date_warning(self):
        self.warning_label = tkinter.Label(self, text="Invalid Date", background=self.label_background, foreground="red")
        self.warning_label.place(x=200, y=200, width=100, height=50)
        self.warning_label.after(1200, self.warning_label.destroy)

    def title_warning(self):
        self.warning_label = tkinter.Label(self, text="A title is required", background=self.label_background, foreground="red")
        self.warning_label.place(x=200, y=200, width=100, height=50)
        self.warning_label.after(1200, self.warning_label.destroy)