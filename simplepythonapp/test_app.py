from app import add, subtract, multiply, divide

def test_calculator():
    assert add(10, 20) == 30
    assert subtract(20, 10) == 10
    assert multiply(5, 4) == 20
    assert divide(20, 5) == 4
    print("All tests passed!")

if __name__ == "__main__":
    test_calculator()
