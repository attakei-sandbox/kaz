import click


@click.command()
def cmd():
    msg = 'Hello kaz!'
    click.echo(msg)


def main():
    cmd()
