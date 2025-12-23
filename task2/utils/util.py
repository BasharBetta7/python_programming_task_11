import subprocess
import sys
import inspect
import pytest
import re


from ..faulty import mysterious_function

def test_correct_function_behavior():
    return mysterious_function([1,2,3,4,5], 3) == 1.8
    
def test_variable_names_correct():
    sig = inspect.signature(mysterious_function)
    params = list(sig.parameters.values())
    pattern = r"[a-z_][a-z0-9_]{2,30}$" 
    for p in params:
        if re.fullmatch(pattern, p.name) is None:
            return False
    return True

        
     

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
  
    return result.returncode == 0


def test_mypy_clean():
    result =  _run_subprocess(
        [sys.executable,
          "-m", 
          "mypy",
          "--strict",
            "task2/faulty.py"])
   
    return result.returncode == 0


if __name__ == '__main__':
    score = 0
    if test_correct_function_behavior() :
        print("test_correct_function_behavior: PASSED")
        score += 1
    else:
        print(f"test_correct_function_behavior: FAILED")

    if test_variable_names_correct():
        print(f"test_variable_names_correct: PASSED")
        score += 1
    else:
        print(f"test_variable_names_correct: FAILED")
    
    if test_pylint_clean():
        print(f"test_pylint_clean: PASSED")
        score += 1
    else:
        print(f"test_pylint_clean: FAILED")
        print(f"run `pylint ./task2/faulty.py` to find errors in your code.")
    
    if test_mypy_clean():
        print(f"test_mypy_clean: PASSED")
        score += 1
    else:
        print(f"test_mypy_clean: FAILED")
        print(f"run `mypy --strict ./task2/faulty.py` to find and correct your function")
    
    print(f"total score: {score}/4")
    if score == 4:
        print("ALL TESTS PASSED CORRECTLY!")
