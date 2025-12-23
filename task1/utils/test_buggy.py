import importlib
import pytest




def test_student_tests_fail_on_buggy_impl(monkeypatch):
    # Use the buggy implementation from bank_rules
    from task1 import club_rules
    def buggy(age: int, balance: int) -> bool:
        # wrong: allows balance == 100? or wrong age range, etc.
        return age >= 18 and balance > 100

    monkeypatch.setattr(club_rules, "can_join_club", buggy)


    result = pytest.main(["task1/student_tests/test_club_rules.py"])
    print(result)
    # They should catch at least one bug
    assert result != 0

