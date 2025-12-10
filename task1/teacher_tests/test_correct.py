import pytest



def test_student_tests_pass_on_correct_impl(monkeypatch):
    # Patch bank_rules with a correct implementation
    from task1 import club_rules
    def correct(age: int, balance: int) -> bool:
        # wrong: allows balance == 100? or wrong age range, etc.
        return 20 <= age <= 40 and balance >= 100
    
    monkeypatch.setattr(club_rules, "can_join_club", correct)
    # Run the student's tests as a subprocess or via pytest.main
    result = pytest.main(["student_tests/test_club_rules.py"])

    assert result == 0


