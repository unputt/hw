from .models import Person


def create(f_name: str, f_last: str, age: int) -> Person:
    person = Person(
        name=f_name,
        last=f_last,
        age=age
    )
    return person
