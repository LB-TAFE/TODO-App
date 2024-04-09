import tkinter
from gui.view_frame import ViewFrame
from gui.sidebar import SideBar
from gui.edit_task_frame import EditTaskFrame
from  database_handler import DatabaseHandler

class ToDoApp(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)

        self.database_handler = DatabaseHandler()

        self.edit_task_frame = EditTaskFrame()

        self.view_frame = ViewFrame()

        self.sidebar = SideBar()
        self.sidebar.place(x=-3, y=-1, width=100, height=603)
        self.sidebar.focus()

