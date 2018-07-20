'''
CLI for CRT library
'''

import click
import crt


@click.command()
def cli():
    click.echo('Hello CRT version %s' % crt.__version__)


if __name__ == '__main__':
    cli()
