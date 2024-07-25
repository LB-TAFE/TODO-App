import tkinter

class SideBar(tkinter.Frame):

    def __init__(self):
        self.background = "#3b3b3b"
        self.label_background = "#36454F"
        self.pressed_colour = "#727272"
        super().__init__(highlightthickness=1, highlightbackground="#FFFFFF", highlightcolor="#FFFFFF", background=self.background, width=100, height=600)

        self.tasks_label = tkinter.Label(self, text="View", background=self.label_background, foreground="#FFFFFF", width=140, height=2, font=("Arial", 14))
        self.tasks_label.pack()

        self.show_upcoming_tasks_button = tkinter.Button(self, text="Upcoming", command=self.show_upcoming_tasks_pressed, width=100, height=2, background=self.background, foreground="#FFFFFF", border=0)
        self.show_upcoming_tasks_button.pack()
        
        self.show_overdue_tasks_button = tkinter.Button(self, text="Overdue", command=self.show_overdue_tasks_pressed, width=100, height=2, background=self.background, foreground="#FFFFFF", border=0)
        self.show_overdue_tasks_button.pack()

        self.show_all_tasks_button = tkinter.Button(self, text="All", command=self.show_all_tasks_pressed, width=100, height=2, background=self.background, foreground="#FFFFFF", border=0)
        self.show_all_tasks_button.pack()


        self.actions_label = tkinter.Label(self, text="Actions", background=self.label_background, foreground="#FFFFFF", width=140, height=2, font=("Arial", 14))
        self.actions_label.pack()

        self.create_task_button = tkinter.Button(self, text="Create Task", command=self.create_task_pressed, width=100, height=2, background=self.background, foreground="#FFFFFF", border=0)
        self.create_task_button.pack()

        self.quit_button = tkinter.Button(self, text="Quit", command=self.quit, width=100, height=2, background=self.background, foreground="#FFFFFF", border=0)
        self.quit_button.pack()

        self.selected_button = None
        self.button_pressed(self.show_all_tasks_button)


    def create_task_pressed(self):
        self.button_pressed(self.create_task_button)
        self.master.create_task_frame.render()

    def show_upcoming_tasks_pressed(self):
        self.button_pressed(self.show_upcoming_tasks_button)
        self.master.view_frame.render_upcoming()

    def show_overdue_tasks_pressed(self):
        self.button_pressed(self.show_overdue_tasks_button)
        self.master.view_frame.render_overdue()

    def show_all_tasks_pressed(self):
        self.button_pressed(self.show_all_tasks_button)
        self.master.view_frame.render_all()

    def button_pressed(self, button):
        self.master.edit_task_frame.place_forget()
        self.master.create_task_frame.place_forget()
        self.master.view_frame.place_forget()
        if self.selected_button:
            self.selected_button.config(background=self.background)
        self.selected_button = button
        self.selected_button.config(background=self.pressed_colour)
