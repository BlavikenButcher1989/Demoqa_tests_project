from faker import Faker
from data.data import Person

faker_ru = Faker('Ru')

def generator_person():
    yield Person(
        full_name= faker_ru.name(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address()
    )