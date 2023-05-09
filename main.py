import ru_local as ru
import random

random_events = [ru.NEW_CHURCH, ru.HELP_CHURCH, ru.NEW_TAX_CHURCH, ru.CHURCH_POWER,
                 ru.CHURCH_REFORM, ru.MARRY, ru.PEACE, ru.CONSPIRACY, ru.CREDIT]


def choice(variants):
    print(variants)
    reply = input()
    while reply != "1" and reply != "2":
        print(ru.INCORRECT)
        reply = input()
    else:
        return reply


def accident():
    pass


def random_event(church, people, army, wealth):
    k = random.randint(0, 2)
    print(random_events[k])
    if k == 0:
        ans = choice(ru.ANS1)
        if ans == 1:
            church += 15
            wealth -= 10
        else:
            church -= 10
    elif k == 1:
        ans = choice(ru.ANS2)
        if ans == 1:
            church += 10
            wealth -= 15
        else:
            church -= 5
            people -= 5
    elif k == 2:
        ans = choice(ru.ANS3)
        if ans == 1:
            church += 15
            people -= 15
            wealth += 15
        else:
            church -= 12
    elif k == 3:
        ans = choice(ru.ANS4)
        if ans == 1:
            church += 40
            people -= 10
            army -= 10
            wealth += 20
        else:
            church -= 20
            people += 10
            army += 5
            wealth -= 5
    return church, people, army, wealth


def game():
    church = 50
    people = 50
    army = 50
    wealth = 50
    print(ru.WELCOME)
    print(ru.RULES)
    while 0 < church < 100 and 0 < people < 100 and 0 < army < 100 and 0 < wealth < 100:
        print(ru.CHURCH, f"= {church}", end=' ')
        print(ru.PEOPLE, f"= {people}", end=' ')
        print(ru.ARMY, f"= {army}", end=' ')
        print(ru.WEALTH, f"= {wealth}")
        n = random.randint(1, 100)
        if n % 2 == 1:
            accident()
        church, people, army, wealth = random_event(church, people, army, wealth)
    else:
        print("...")
        ans = input(ru.CONTINUE).lower()
        if ans == "да":
            game()


game()
