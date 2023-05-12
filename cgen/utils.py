import os
from typing import List

# import typer
# import cookiecutter.main
# from cookiecutter.exceptions import RepositoryNotFound
from dotenv import load_dotenv

# from cgen.handlers.cookie import CookieWrapper


class DirHandler:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.load_config()

    def create_dir(self, dir_name: str):
        os.makedirs(self.get_path(dir_name), exist_ok=True)

    def delete_dir(self, dir_name: str):
        os.rmdir(self.get_path(dir_name))

    def get_path(self, *args):
        return os.path.join(self.base_dir, *args)

    def load_config(self):
        home_dir = os.path.expanduser("~")
        dotenv_path = os.path.join(home_dir, ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            self.default_dir = os.getenv("DEFAULT_DIR")
        else:
            self.default_dir = None
