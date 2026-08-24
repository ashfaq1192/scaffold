import click


@click.command()
@click.option("--name", required=True, help="The name to greet.")
def greet(name):
    """A simple greeting CLI that prints a hello message for the given name."""
    click.echo(f"hi {name}")


if __name__ == "__main__":
    greet()
