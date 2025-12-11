# task3/teacher_test/test_solution.py

import ast
import subprocess
import sys
from pathlib import Path


STUDENT_TEST_FILE = Path("./task3/test_notifications.py")


def run_pytest_on_student_tests() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "./task3/test_notifications.py"],
        text=True,
        capture_output=True,
    )

    return result.returncode


def analyze_ast_for_fixture_and_mocker(source: str) -> dict:
    tree = ast.parse(source)

    fixture_functions = set()
    has_fixture_usage = False
    has_mocker_usage = False


    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for dec in node.decorator_list:
                # @pytest.fixture
                if isinstance(dec, ast.Attribute):
                    if getattr(dec.value, "id", None) == "pytest" and dec.attr == "fixture":
                        fixture_functions.add(node.name)

    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            param_names = {arg.arg for arg in node.args.args}
            if fixture_functions & param_names:
                has_fixture_usage = True
            # Also check for mocker fixture via argument name
            if "mocker" in param_names:
                has_mocker_usage = True
    
    class MockerVisitor(ast.NodeVisitor):
        def __init__(self):
            self.found = False

        def visit_Attribute(self, node: ast.Attribute):
            # e.g. mocker.patch(...)
            if isinstance(node.value, ast.Name) and node.value.id == "mocker":
                if node.attr.startswith("patch"):
                    self.found = True
            self.generic_visit(node)

    mv = MockerVisitor()
    mv.visit(tree)
    if mv.found:
        has_mocker_usage = True

    return {
        "has_fixture_definition": bool(fixture_functions),
        "has_fixture_usage": has_fixture_usage,
        "has_mocker_usage": has_mocker_usage,
    }


def main() -> None:
    pytest_code = run_pytest_on_student_tests()
    if pytest_code != 0:
        print("test_student_tests: FAILED")
        sys.exit(1)

    print(STUDENT_TEST_FILE)
   

    source = STUDENT_TEST_FILE.read_text(encoding="utf-8")
    info = analyze_ast_for_fixture_and_mocker(source)

    print(f"Has fixture definition: {info['has_fixture_definition']}")
    print(f"Has fixture usage:      {info['has_fixture_usage']}")
    print(f"Has mocker usage:       {info['has_mocker_usage']}")

    score = 0

    # base condition: tests pass
    if pytest_code == 0:
        score += 2  # 2 points for correct behavior

    if info["has_fixture_definition"] and info["has_fixture_usage"]:
        score += 1  # 1 point for using at least one fixture properly

    if info["has_mocker_usage"]:
        score += 1  # 1 point for using mocker

    print(f"\nRESULT: Score: {score}/4")

    if score < 4:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
