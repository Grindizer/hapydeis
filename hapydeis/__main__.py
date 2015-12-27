#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import click

@click.command()
def main():
    click.secho("Hapydeis main command line invoked.", fg='green')


if __name__ == '__main__':
    main()