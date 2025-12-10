import subprocess
import sys
import inspect
import re


from task2.faulty import mysterious_function

def test_correct_function_behavior():
    assert mysterious_function([1,2,3,4,5], 3) == 1.8
    
def test_variable_names_correct():
    sig = inspect.signature(mysterious_function)
    params = list(sig.parameters.values())
    pattern = r"[a-z_][a-z0-9_]{2,30}$" 
    assert len(params) == 0
    for p in params:
        assert re.fullmatch(pattern, p.name) is not None



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

