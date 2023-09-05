
from data.data import Person
from faker import Faker
faker_en = Faker()
Faker.seed()


def generated_person():
    yield Person(
        email=faker_en.email(),
    )
