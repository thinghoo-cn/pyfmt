"""Console script for pyfmt."""
import sys

import click

from .pyfmt import fmt


@click.command()
@click.argument("fmt_folder")
@click.option("--folder", help="The folder to format")
def main(folder: str, fmt_folder: str):
    """Console script for pyfmt."""
    click.echo("Formating ... ")
    click.echo("See click documentation at https://click.palletsprojects.com/")

    if fmt_folder:
        fmt(fmt_folder)
    else:
        fmt(folder)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
