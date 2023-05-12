import os
from typing import List

import typer

from cgen.cookie import CookieWrapper

app = typer.Typer()


@app.command()
def generate(template: str, dirs: List[str]):
    cookie_wrapper = CookieWrapper(os.getcwd())
    cookie_wrapper.generate(template, dirs)


@app.command()
def reverse_engineer(instance_dir: str, metadata_dir: str):
    cookie_wrapper = CookieWrapper(os.getcwd())
    cookie_wrapper.reverse_engineer(instance_dir, metadata_dir)


@app.command()
def get_cookiecutter_json(instance_dir: str):
    cookie_wrapper = CookieWrapper(os.getcwd())
    cookiecutter_json = cookie_wrapper.get_cookiecutter_json(instance_dir)
    if cookiecutter_json:
        typer.echo(cookiecutter_json)


def entry_point() -> None:
    app()


if __name__ == "__main__":
    entry_point()
