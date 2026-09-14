from main import calculate_percentage

def test_full_score():
    assert calculate_percentage(5, 5) == 100

def test_sixty_percent():
    assert calculate_percentage(3, 5) == 60

def test_failed_score():
    assert calculate_percentage(2, 5) == 40