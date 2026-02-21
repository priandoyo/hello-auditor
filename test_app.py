from app import greet

# Scenario 1: Positive test (expected result)
def test_greet_positive():
    assert greet() == "Hello Auditor!"

# Scenario 2: Negative test (must NOT match wrong output)
def test_greet_negative():
    assert greet() != "Hello Consultant!"

# Scenario 3: Type check (control scenario)
def test_greet_type():
    assert isinstance(greet(), str)
