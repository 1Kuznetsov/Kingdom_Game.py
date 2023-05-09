import ru_local as ru
import random

random_events = [ru.NEW_CHURCH, ru.HELP_CHURCH, ru.NEW_TAX_CHURCH, ru.CHURCH_POWER,
                 ru.MARRY, ru.PEACE, ru.CONSPIRACY, ru.CREDIT]


def accident():
    pass


def random_event():
    k = random.randint(0, 50)


def game():
    church = 50
    people = 50
    army = 50
    wealth = 50
    print(ru.WELCOME)
    print(ru.RULES)
    while church > 0 and people > 0 and army > 0 and wealth > 0:
        print(ru.CHURCH, f"= {church}")
        print(ru.PEOPLE, f"= {people}")
        print(ru.ARMY, f"= {army}")
        print(ru.WEALTH, f"= {wealth}")
        n = random.randint(1, 100)
        if n % 2 == 1:
            accident()
        random_event()
    else:
        print("...")
        ans = input(ru.CONTINUE).lower()
        if ans == "да":
            game()


game()
