from typing import Optional

import click


@click.group()
@click.version_option()
def cli():
    # """Your app description goes here."""
    "{{ cookiecutter.description }}"


@cli.command("example")
@click.argument("required_argument")
@click.option("-o", "--option", help="An option for the 'example' command.")
def command(required_argument: str, option: Optional[str] = None):
    """Description for the 'example' command goes here."""
    click.echo(f"Received argument: {required_argument}")
    click.echo(f"Received option: {option}")
