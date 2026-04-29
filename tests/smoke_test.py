import io
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from simple_python.runner import run_source


def main():
    output = io.StringIO()
    program = """
int add(int a, int b) {
    return a + b;
}

int x = 2;
int y = 3;

if (x < y) {
    printf("%d\\n", add(x, y));
} else {
    printf("0\\n");
}
"""
    run_source(program, output_stream=output)
    result = output.getvalue()
    expected = "5\n"
    if result != expected:
        raise SystemExit(f"Unexpected output: {result!r}")
    print("Smoke test passed")


if __name__ == "__main__":
    main()
