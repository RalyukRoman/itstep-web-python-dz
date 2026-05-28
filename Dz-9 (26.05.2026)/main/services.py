from datetime import datetime

def get_multiplication_matrix():
    """Get the multiplication matrix for numbers from 1 to 10."""
    matrix = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        matrix.append(row)
    return matrix

def calculate_programmer_day(year: int) -> str:
    """Calculate the date of the Programmer's Day for a given year."""
    programmer_date = datetime.fromordinal(datetime(year, 1, 1).toordinal() + 255)
    return programmer_date.strftime("%d.%m.%Y")