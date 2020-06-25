"""Console script for pyfmt."""
import sys

import click

from .pyfmt import fmt


@click.command()
@click.option("--folder", prompt="format folder", help="The folder to format")
def main(folder: str):
    """Console script for pyfmt."""
    click.echo("Formating ... ")
    click.echo("See click documentation at https://click.palletsprojects.com/")

    fmt(folder)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
