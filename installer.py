import os
import tkinter
import asyncio
import threading


class Installer:

    def __init__(self, install_path):

        self.install_path = install_path
        self.github_url = "https://api.github.com/repos/LB-TAFE/TODO-App/contents/"
        self.project_files = {}
        self.requests = __import__("requests")
        import requests

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

    def download_project(self):
        self.make_api_call(self.github_url)

    def make_api_call(self, url):
        req = self.requests.get(url)
        data = req.json()
        for reference in data:
            if reference["download_url"] != None:
                file_contents = self.requests.get(reference["download_url"]).text
                self.project_files[reference["path"]] = file_contents
                continue
            if "?ref" in reference["url"]:
                self.make_api_call(reference["url"].split("?ref")[0])
                continue
            self.make_api_call(reference["url"])


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

        threading.Thread(target=self.install_process).start()

    def confirm_dependancies(self):
        self.status.config(text="Checking dependencies...")
        missing = self.installer.get_missing_dependencies()
        if missing:
            self.status.config(text=f"Installing dependencies: {", ".join(missing)}")
            self.installer.install_modules(missing)
        else:
            self.status.config(text="No missing dependencies")

    def download_project(self):
        self.installer.download_project()

    def install_project(self):
        if os.name == "nt":
            for file, contents in self.installer.project_files.items():
                with open(rf"{self.installer.install_path}\{file}", "w+") as f:
                    f.write(contents)
        else:
            for file, contents in self.installer.project_files.items():
                with open(rf"{self.installer.install_path}/{file}", "w") as f:
                    f.write(contents)

    def install_process(self):
        self.confirm_dependancies()
        self.status.config(text="Downloading project files")
        self.download_project()
        self.install_project()


if __name__ == "__main__":
    confirm = ConfirmInstallApp()
    confirm.mainloop()
