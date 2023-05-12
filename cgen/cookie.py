import os
from typing import List

import cookiecutter.main
from typer import echo
from cookiecutter.exceptions import RepositoryNotFound

from cgen.utils import DirHandler


class CookieWrapper:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.dir_handler = DirHandler(base_dir)

    def generate(self, template: str, dirs: List[str]):
        for dir_name in dirs:
            self.dir_handler.create_dir(dir_name)
            try:
                cookiecutter.main.cookiecutter(template, no_input=True, output_dir=self.dir_handler.get_path(dir_name))
            except RepositoryNotFound:
                echo(f"Error: Template {template} not found.")
                self.dir_handler.delete_dir(dir_name)

    def reverse_engineer(self, instance_dir: str, metadata_dir: str):
        try:
            cookiecutter.main.cookiecutter(
                self.dir_handler.get_path(instance_dir),
                output_dir=self.dir_handler.get_path(metadata_dir),
                replay=True,
                overwrite_if_exists=True,
            )
        except RepositoryNotFound:
            echo(f"Error: Instance {instance_dir} not found.")

    def get_cookiecutter_json(self, instance_dir: str):
        cookiecutter_json_path = self.dir_handler.get_path(instance_dir, "cookiecutter.json")
        if os.path.exists(cookiecutter_json_path):
            with open(cookiecutter_json_path, "r") as f:
                return f.read()
        else:
            echo(f"Error: {cookiecutter_json_path} not found.")
            return None
