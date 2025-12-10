import subprocess
import sys

from task2.faulty import mysterious_function

def test_correct_function_behavior():
    assert mysterious_function([1,2,3,4,5], 3) == 1.8

def _run_subprocess(cmd):
    return subprocess.run(
        cmd, 
        text=True,
        capture_output=True
    )


def test_pylint_clean():
    result =  _run_subprocess(
        [sys.executable,
          "-m", 
          "pylint",
            "task2/faulty.py"])
  

    assert result.returncode == 0


def test_mypy_clean():
    result =  _run_subprocess(
        [sys.executable,
          "-m", 
          "mypy",
          "--strict",
            "task2/faulty.py"])
   

    assert result.returncode == 0

