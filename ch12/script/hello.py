import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, default="World", nargs="?")
args = parser.parse_args()

print(f"Hello, {args.name}!")
