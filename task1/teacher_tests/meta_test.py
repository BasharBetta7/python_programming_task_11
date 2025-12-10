import subprocess
import sys

cmd_1 = [sys.executable, "-m", "pytest", "-vv", "task1/teacher_tests/test_buggy.py"]
cmd_2 = [sys.executable, "-m", "pytest", "-vv", "task1/teacher_tests/test_correct.py"]

result_1 = subprocess.run(cmd_1,
    text=True,
    capture_output=True
)

result_2 = subprocess.run(cmd_2,
    text=True,
    capture_output=True
)

corrects = 0
if result_1.returncode == 0:
    print(f"test_buggy PASSED")
    corrects += 1
else:
    print(f"test_buggy FAILED")
if result_2.returncode == 0:
    print(f"test_correct PASSED")
    corrects += 1
else:
    print(f"test_correct FAILED")

print(f"Correctly passed tests {corrects}/2")

