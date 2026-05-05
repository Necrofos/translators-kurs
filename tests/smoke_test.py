import io
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from simple_python.runner import run_source


def main():
    output = io.StringIO()
    program = """
struct Point {
    int x;
    int y;
};

struct Line {
    struct Point start;
    struct Point end;
};

int add(int a, int b) {
    return a + b;
}

int sum_point(struct Point point) {
    point.x = point.x + 1;
    return point.x + point.y;
}

struct Point make_point(int x, int y) {
    struct Point point;
    point.x = x;
    point.y = y;
    return point;
}

int x = 2;
int y = 3;

if (x < y) {
    printf("%d\\n", add(x, y));
} else {
    printf("0\\n");
}

struct Point first;
first.x = 2;
first.y = 3;

struct Point copy = first;
copy.x = 10;

struct Line line;
line.start = first;
line.end = copy;

printf("%d %d %d\\n", sum_point(first), first.x, line.end.x);

line.start.x = 4;
printf("%d %d\\n", line.start.x, first.x);

struct Point made = make_point(7, 8);
printf("%d %d\\n", made.x, made.y);
"""
    run_source(program, output_stream=output)
    result = output.getvalue()
    expected = "5\n6 2 10\n4 2\n7 8\n"
    if result != expected:
        raise SystemExit(f"Unexpected output: {result!r}")
    print("Smoke test passed")


if __name__ == "__main__":
    main()
