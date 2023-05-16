import ru_local as ru
import random

random_events = [ru.NEW_CHURCH, ru.HELP_CHURCH, ru.NEW_TAX_CHURCH, ru.CHURCH_POWER,
                 ru.CHURCH_REFORM, ru.PEACE, ru.DEMONS, ru.EMBASSY, ru.REFUGEE, ru.HOMELESS,
                 ru.AGROTECH, ru.FLOOD, ru.LIVESTOCK, ru.CORN, ru.GOLD, ru.FAMINE, ru.ATTACK,
                 ru.DEFEAT, ru.VICTORY, ru.BLACK_MARKET, ru.REBELLION, ru.WITCH_SHOP,
                 ru.FORBIDDEN_EXPERIMENTS, ru.EDUCATION, ru.MILITARY_RESEARCH,
                 ru.ALCHEMY_RESEARCH, ru.ARMY_HYGIENE, ru.HOSPITAL, ru.WAR_MARRY, ru.PRINCESS]
year = [600]
record = 0
actions = []
print(ru.RULES)


def choice(variants):
    print(variants)
    reply = input()
    while reply != "1" and reply != "2":
        print(ru.INCORRECT)
        reply = input()
    else:
        return reply


def accident(church, people, army, wealth):
    accident_act = [ru.act_1, ru.act_2, ru.act_3, ru.act_4, ru.act_5, ru.act_9, ru.act_7, ru.act_8]
    random_index = random.randint(0, len(accident_act) - 1)
    print(accident_act[random_index])
    act_rand = accident_act[random_index]
    if act_rand == ru.act_1:
        r1 = random.randint(10, 20)
        people -= r1
        print(f'Минус {r1} народа')
    if act_rand == ru.act_2:
        natural_phenomena = [ru.phenomenon_1, ru.phenomenon_2, ru.phenomenon_3]
        random_phenomena = random.randint(0, len(natural_phenomena) - 1)
        phenomena_rand = natural_phenomena[random_phenomena]
        if phenomena_rand == ru.phenomenon_1:
            print(ru.phenomenon_1)
            r2 = random.randint(5, 15)
            r3 = random.randint(10, 20)
            wealth -= r2
            people += r3
            print(f'Минус {r2} казны, плюс {r3} народа')
        if phenomena_rand == ru.phenomenon_2:
            print(ru.phenomenon_2)
            r7 = random.randint(15, 20)
            people -= r7
            wealth -= r7
            print(f'Минус {r7} народа, минус {r7} казны')
        if phenomena_rand == ru.phenomenon_3:
            print(ru.phenomenon_3)
            r8 = random.randint(1, 10)
            church -= r8
            print(f'Минус {r8} церкви')
    if act_rand == ru.act_3:
        r9 = random.randint(3, 8)
        r10 = random.randint(3, 10)
        people -= r9
        army -= r10
        print(f'Минус {r9} народа, минус {r10} армии')
    if act_rand == ru.act_4:
        r11 = random.randint(3, 10)
        church -= r11
        print(f'Минус {r11} церкви')
    if act_rand == ru.act_5:
        accident_seeds = [ru.seed_good, ru.seed_bad]
        rand_seeds = random.randint(0, len(accident_seeds) - 1)
        rand_seed = accident_seeds[rand_seeds]
        if rand_seed == ru.seed_good:
            print(ru.seed_good)
            r12 = random.randint(5, 17)
            r13 = random.randint(4, 13)
            r14 = random.randint(3, 10)
            people += r12
            army += r13
            wealth += r14
            print(f'Плюс {r12} народа, плюс {r13} армии, плюс {r14} казны')
        if rand_seed == ru.seed_bad:
            print(ru.seed_bad)
            r15 = random.randint(1, 8)
            people -= r15
            print(f'Минус {r15} людей')
    if act_rand == ru.act_7:
        r20 = random.randint(1, 8)
        church -= r20
        people -= r20
        print(f'Минус {r20} церкви, минус {r20} людей')
    if act_rand == ru.act_8:
        accident_animals = [ru.hamster, ru.rats]
        rand_animals = random.randint(0, len(accident_animals) - 1)
        rand_animal = accident_animals[rand_animals]
        if rand_animal == ru.hamster:
            print('К Вам пришел хомяк')
            wealth += 12
            print('Плюс 12 казны')
        if rand_animal == ru.rats:
            print('К Вам пришла крыса')
            people -= 14
            print('Минус 14 народа')
    if act_rand == ru.act_9:
        people -= 18
        wealth -= 5
    return church, people, army, wealth


def random_event(church, people, army, wealth, marry):
    global actions
    if marry:
        k = random.randint(0, 27)
        if len(actions) >= 2:
            while k == actions[-1] or k == actions[-2]:
                k = random.randint(0, 27)
    else:
        k = random.randint(0, 29)
        if len(actions) >= 2:
            while k == actions[-1] or k == actions[-2]:
                k = random.randint(0, 29)
    print(random_events[k])
    if k == 0:
        ans = choice(ru.ANS0)
        if ans == 1:
            church += 15
            wealth -= 10
        else:
            church -= 10
    elif k == 1:
        ans = choice(ru.ANS1)
        if ans == 1:
            church += 10
            wealth -= 15
        else:
            church -= 5
            people -= 5
    elif k == 2:
        ans = choice(ru.ANS2)
        if ans == 1:
            church += 15
            people -= 15
            wealth += 15
        else:
            church -= 12
    elif k == 3:
        ans = choice(ru.ANS3)
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
            church += 15
            people -= 5
        else:
            church -= 10
            people += 15
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
    elif k == 20:
        ans = choice(ru.ANS20)
        if ans == 1:
            people -= 10
            army += 30
            wealth -= 10
        else:
            church -= 10
            people += 5
            army -= 10
    elif k == 21:
        ans = choice(ru.ANS21)
        if ans == 1:
            church -= 25
            people += 5
        else:
            church += 5
            people -= 15
    elif k == 22:
        ans = choice(ru.ANS22)
        if ans == 1:
            church += 20
            people -= 5
        else:
            church -= 25
    elif k == 23:
        ans = choice(ru.ANS23)
        if ans == 1:
            church -= 5
            people += 15
            wealth -= 20
        else:
            church += 15
            people += 10
            wealth -= 15
    elif k == 24:
        ans = choice(ru.ANS24)
        if ans == 1:
            people -= 5
            army += 25
            wealth -= 15
        else:
            people += 5
            army -= 20
    elif k == 25:
        ans = choice(ru.ANS25)
        if ans == 1:
            church -= 15
            wealth += 5
        else:
            church += 10
    elif k == 26:
        ans = choice(ru.ANS26)
        if ans == 1:
            people += 5
            army += 15
            wealth -= 10
        else:
            people -= 10
            army -= 15
    elif k == 27:
        ans = choice(ru.ANS27)
        if ans == 1:
            people += 15
            wealth -= 10
        else:
            people -= 15
    elif k == 28:
        ans = choice(ru.ANS28)
        if ans == 1:
            marry = 1
            church += 10
            people += 10
            army += 10
            wealth += 10
        else:
            people -= 10
            wealth -= 15
    elif k == 29:
        ans = choice(ru.ANS29)
        if ans == 1:
            marry = 1
            church += 10
            people += 10
            army += 10
            wealth += 10
        else:
            church -= 15
            army -= 10
            wealth -= 15
    actions.append(k)
    return church, people, army, wealth, marry


def game():
    name = input(ru.NAME)
    current_year = year[-1]
    marry = 0
    church = 50
    people = 50
    army = 50
    wealth = 50
    print(ru.WELCOME)
    while 0 < church < 100 and 0 < people < 100 and 0 < army < 100 and 0 < wealth < 100:
        current_year += 1
        print(ru.CHURCH, f"= {church} / 100", end=' ')
        print(ru.PEOPLE, f"= {people} / 100", end=' ')
        print(ru.ARMY, f"= {army} / 100", end=' ')
        print(ru.WEALTH, f"= {wealth} / 100")
        n = random.randint(1, 100)
        if n % 3 == 1:
            church, people, army, wealth = accident(church, people, army, wealth)
        church, people, army, wealth, marry = random_event(church, people, army, wealth, marry)
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
        year.append(current_year)
        time = year[-1] - year[-2]
        global record
        if time > record:
            record = time
            print(ru.RECORD, end='')
        if time % 10 == 1 and time % 100 != 11:
            print(f"Король {name} ({year[-2]} - {year[-1]}) правил {time} год")
        elif 1 < time % 10 < 5 and (time % 100 > 14 or time % 100 < 12):
            print(f"Король {name} ({year[-2]} - {year[-1]}) правил {time} года")
        else:
            print(f"Король {name} ({year[-2]} - {year[-1]}) правил {time} лет")
        ans = input(ru.CONTINUE).lower()
        global actions
        actions = []
        if ans == "да":
            game()


game()
