import ru_local as ru
import random

random_events = [ru.NEW_CHURCH, ru.HELP_CHURCH, ru.NEW_TAX_CHURCH, ru.CHURCH_POWER,
                 ru.CHURCH_REFORM, ru.PEACE, ru.DEMEANOR, ru.EMBASSY, ru.REFUGEE, ru.HOMELESS,
                 ru.AGROTECH, ru.FLOOD, ru.LIVESTOCK, ru.CORN, ru.GOLD, ru.FAMINE, ru.ATTACK,
                 ru.DEFEAT, ru.VICTORY, ru.BLACK_MARKET]


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
    k = random.randint(0, 19)
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
    elif k == 4:
        ans = choice(ru.ANS4)
        if ans == 1:
            church += 20
            people -= 10
            army -= 10
        else:
            church -= 10
    elif k == 5:
        ans = choice(ru.ANS5)
        if ans == 1:
            church += 6
            people += 6
            army += 6
            wealth += 6
        else:
            people -= 20
            army += 15
            wealth -= 15
    elif k == 6:
        ans = choice(ru.ANS6)
        if ans == 1:
            church += 10
            people -= 10
        else:
            people += 5
    elif k == 7:
        ans = choice(ru.ANS7)
        if ans == 1:
            people += 10
            army += 5
            wealth -= 15
        else:
            people -= 5
    elif k == 8:
        ans = choice(ru.ANS8)
        if ans == 1:
            church -= 5
            people -= 5
            army -= 5
            wealth += 20
        else:
            army += 20
            wealth -= 10
    elif k == 9:
        ans = choice(ru.ANS9)
        if ans == 1:
            church += 10
            people -= 5
            army += 5
        else:
            church -= 5
            people += 10
            army -= 5
    elif k == 10:
        ans = choice(ru.ANS10)
        if ans == 1:
            church += 8
            people += 8
            army += 8
        else:
            wealth += 20
    elif k == 11:
        ans = choice(ru.ANS11)
        if ans == 1:
            church -= 10
            people += 5
            army -= 15
            wealth -= 30
        else:
            people -= 40
    elif k == 12:
        ans = choice(ru.ANS12)
        if ans == 1:
            people += 5
            wealth -= 10
        else:
            people -= 5
            wealth += 5
    elif k == 13:
        ans = choice(ru.ANS13)
        if ans == 1:
            wealth += 5
        else:
            people -= 35
            wealth += 20
    elif k == 14:
        ans = choice(ru.ANS14)
        if ans == 1:
            church += 10
            people += 10
            army += 10
            wealth += 10
        else:
            wealth += 40
    elif k == 15:
        ans = choice(ru.ANS15)
        if ans == 1:
            people += 5
            wealth -= 15
        else:
            people += 20
            wealth -= 30
    elif k == 16:
        ans = choice(ru.ANS16)
        if ans == 1:
            church += 5
            people -= 10
            army -= 10
            wealth -= 10
        else:
            church -= 10
            army += 5
            wealth -= 5
    elif k == 17:
        ans = choice(ru.ANS17)
        if ans == 1:
            church -= 25
            people -= 25
            army -= 25
            wealth -= 25
        else:
            people -= 5
            army += 15
            wealth -= 35
    elif k == 18:
        ans = choice(ru.ANS18)
        if ans == 1:
            church += 5
            people += 5
            army += 5
            wealth += 15
        else:
            army -= 10
    elif k == 19:
        ans = choice(ru.ANS19)
        if ans == 1:
            people -= 20
            army -= 5
            wealth += 10
        else:
            people += 15
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
        if church >= 100:
            print(ru.MARTYR)
        elif church <= 0:
            print(ru.FATAL)
        elif people >= 100:
            print(ru.DISMISSAL)
        elif people <= 0:
            print(ru.NOTHING)
        elif army >= 100:
            print(ru.OVERTURN)
        elif army <= 0:
            print(ru.CAPTURE)
        elif wealth >= 100:
            print(ru.FEAST)
        elif wealth <= 100:
            print(ru.POVERTY)
        print("...")
        ans = input(ru.CONTINUE).lower()
        if ans == "да":
            game()


game()
