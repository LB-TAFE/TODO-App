import os
import tkinter


class Installer:

    def __init__(self, install_path):
        self.install_path = install_path
        self.github_api_url = "https://api.github.com/repos/"

    def get_missing_dependencies(self):
        with open("requirements.txt") as f:
            requirements = f.read().splitlines()

        missing = []
        for requirement in requirements:
            try:
                __import__(requirement)
            except ImportError:
                missing.append(requirement)

        return missing

    def install_modules(self, modules):
        for module in modules:
            os.system(f"pip install {module}")

    def ensure_dependencies(self):
        missing = self.get_missing_dependencies()
        if missing:
            self.install_modules(missing)

    def download_project(self, project_url):
        self.project_files = []

    def make_api_call(self, url):
        pass


class ConfirmInstallApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Installer")
        self.geometry("400x210")
        self.eval("tk::PlaceWindow . center")
        self.resizable(False, False)
        self.focus()

        self.install_prompt = tkinter.Label(
            self, text="Enter the path to install the project:"
        )

        self.install_button = tkinter.Button(
            self, text="Install", command=self.install_button_pressed
        )
        self.cancel_button = tkinter.Button(
            self, text="Cancel", command=self.cancel_button_pressed
        )
        self.install_path_prompt = tkinter.Entry(self, width=50)

        self.install_prompt.place(relx=0.5, rely=0.3, anchor="center")
        self.install_path_prompt.insert(0, os.getcwd())
        self.install_path_prompt.place(relx=0.5, rely=0.4, anchor="center")
        self.install_button.place(relx=0.4, rely=0.55, anchor="center")
        self.cancel_button.place(relx=0.6, rely=0.55, anchor="center")

    def install_button_pressed(self):
        installer = InstallerApp(self.install_path_prompt.get())
        self.destroy()
        installer.mainloop()

    def cancel_button_pressed(self):
        self.destroy()
        exit()

    def close_button_pressed():
        pass


class InstallerApp(tkinter.Tk):
    def __init__(self, install_path):
        super().__init__()
        self.title("Installer")
        self.geometry("400x400")
        self.eval("tk::PlaceWindow . center")
        self.resizable(False, False)
        self.focus()

        self.installer = Installer(install_path)

        self.status = tkinter.Label(self, text="Checking dependencies...")
        self.status.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    confirm = ConfirmInstallApp()
    confirm.mainloop()
