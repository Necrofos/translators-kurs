import argparse
import sys

from simple_python.runner import run_file


def build_parser():
    parser = argparse.ArgumentParser(
        prog="c-subset-translator",
        description="Translator/interpreter for a simplified subset of C built with ANTLR4."
    )
    parser.add_argument("source", nargs="?", help="Path to a source file written in the supported subset of C.")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.source:
        parser.print_help(sys.stderr)
        return 1

    try:
        run_file(args.source)
    except FileNotFoundError:
        print(f"File not found: {args.source}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Execution failed: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
