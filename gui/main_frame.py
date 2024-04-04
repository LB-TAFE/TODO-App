import tkinter


class MainFrame(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.create_widgets()
