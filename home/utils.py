from datetime import date

def get_age(birth_day: date) -> int:

    today = date.today()
    
    return today.year - birth_day.year - (
            (today.month, today.day) < (birth_day.month, birth_day.day)
    )

