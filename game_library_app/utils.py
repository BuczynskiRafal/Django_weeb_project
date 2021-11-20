from .models import Game
from faker import Faker
from random import randint


def create_game(n=100):
    fake = Faker("pl_PL")
    for _ in range(n):
        created = fake.date_time()
        game = Game(
            title=fake.text(randint(15, 40)),
            description=fake.text(randint(300, 800)),
            creation_date=created,
            story=fake.text(randint(300, 800)),
            mechanics=fake.text(randint(300, 800)),
            technical_issues=fake.text(randint(300, 800)),
            sponsored=fake.boolean(),
        )

        game.save()
