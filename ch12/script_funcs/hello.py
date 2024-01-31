import argparse


def parse_args(arg_list: list[str] | None):
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, default="World", nargs="?")
    return parser.parse_args(arg_list)


def main(arg_list: list[str] | None = None):
    args = parse_args(arg_list)
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
