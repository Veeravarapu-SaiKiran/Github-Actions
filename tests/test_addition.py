from addition import add

def test_add():
    # Test case 1: Adding positive numbers
    assert add(1, 2) == 3

    # Test case 2: Adding a positive and a negative number
    assert add(1, -1) == 0

    # Test case 3: Adding two negative numbers
    assert add(-2, -3) == -5

    # Test case 4: Adding zeros
    assert add(0, 0) == 0

    # Test case 5: Adding a large number and a small number
    assert add(1000, 1) == 1001