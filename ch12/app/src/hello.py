import click


@click.command()
@click.argument("name", required=False, default="World")
def main(name: str):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
