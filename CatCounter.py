import time
import random
import winsound
import json
import os

SAVE_FILE = "catcounter.json"

def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("food", 0), data.get("sleep", 0), data.get("play", 0), data.get("fish", 0), data.get("name", "")
    return 0, 0, 0, 0, ""

def save_game(food, sleep, play, fish, name):
    data = {
        "food": food,
        "sleep": sleep,
        "play": play,
        "fish": fish,
        "name": name
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

food, sleep, play, fish, saved_name = load_save()
name = saved_name if saved_name else ""

print("Select a language/Выберите язык")
a = input('Eng=2/Рус=1: ')

if a == '1':
    print('Программа "CatCounter" =ω=')
    time.sleep(2)
    print('В данной программе вы сможете вести статистику вашего котика!')

    if saved_name:
        print(f'Загружено сохранение для котика {saved_name}')
        name = saved_name
    else:
        name = input('Введите имя вашего котика: ')

    print(f'Теперь вы можете записывать статистику своего питомца!')
    time.sleep(1)
    print('В неё входят: еда, сон и игры с котиком!')
    time.sleep(1)
    print('Еще в этой программе существует пару мини-игр!')

    while True:
        print(f'Статистика котика {name}! ')
        time.sleep(1)
        print(f'Котик поел {food} раз! ')
        time.sleep(1)
        print(f'Котик спал {sleep} раз! ')
        time.sleep(1)
        print(f'Вы играли с котиком {play} раз! ')
        time.sleep(1)
        print('Что вы хотите ввести?')
        time.sleep(1)
        score = input('Поел = 1, поспал = 2, поиграл = 3, мини-игры = 4, выход = 5, о программе = 6: ')

        if score == '1':
            food += 1
            save_game(food, sleep, play, fish, name)
        elif score == '2':
            sleep += 1
            save_game(food, sleep, play, fish, name)
        elif score == '3':
            play += 1
            save_game(food, sleep, play, fish, name)
        elif score == '4':
            print('В какую мини-игру вы хотите поиграть?')
            time.sleep(1)
            score1 = input('Рыбалка = 1, угадай число = 2: ')
            if score1 == '1':
                print(f'За всё время вы поймали {fish} очков!')
                print('Вам даётся 5 забросов. Случайная редкость рыбы')
                items = ["окунь", "щука", "карп", "ботинок", "водоросли", "золотая рыбка"]
                for _ in range(5):
                    ylov = random.choice(items)
                    schet = random.randint(1, 5)
                    print(f'Очки за эту рыбу: {schet}')
                    input("Нажми Enter, чтобы закинуть удочку...")
                    time.sleep(1)
                    print('Отдыхаем...')
                    time.sleep(1)
                    print('Пьём чай...')
                    time.sleep(3)
                    print('Бульк...')
                    time.sleep(2)
                    winsound.Beep(800, 500)
                    print('Клюет!')
                    for _ in range(3):
                        winsound.Beep(800, 100)
                    print(f'Вы поймали {ylov}!')
                    time.sleep(1)
                    if ylov in ["окунь", "щука", "карп", "золотая рыбка"]:
                        fish += schet
                        print(f"+{schet} очков к рыбе!")
                    else:
                        print("Мусор — очков не даёт")
                    save_game(food, sleep, play, fish, name)
                print(f"Рыбалка окончена. Всего очков: {fish}")
            elif score1 == '2':
                print("\n Угадай число от 1 до 3!")
                secret = random.randint(1, 3)
                try:
                    guess = int(input("Твой вариант: "))
                    if guess == secret:
                        print(" Кот мурчит! Ты угадал!")
                        fish += 1
                        save_game(food, sleep, play, fish, name)
                        print("+1 к играм с котиком!")
                    else:
                        print(f" Не угадал. Кот загадал {secret}. В следующий раз повезёт.")
                except:
                    print("Нужно ввести число 1, 2 или 3.")
                time.sleep(2)
        elif score == '5':
            save_game(food, sleep, play, fish, name)
            print(f"До свидания! {name} ждёт тебя завтра.")
            break
        elif score == '6':
            if score == '6':
                print("""
                ============================================================
                                      CatCounter v1.2
                ============================================================

                   Учёт ухода за котом в консоли.

                   Что умеет:
                   • Трекер кормления, сна, игр
                   • Две мини-игры (рыбалка, угадай число)
                   • Автосохранение в JSON
                   • Русский / English

                   Разработчик:   Xintov
                   Лицензия:      MIT

                   Спасибо, что пользуетесь!
                ============================================================
                """)
                input("Нажми Enter, чтобы вернуться в меню...")
                continue

elif a == '2':
    print('Program "CatCounter" =ω=')
    time.sleep(2)
    print('In this program, you can keep statistics for your cat!')

    if saved_name:
        print(f'Loaded save for cat {saved_name}')
        name = saved_name
    else:
        name = input('Enter your cat\'s name: ')

    print(f'Now you can record statistics for your pet!')
    time.sleep(1)
    print('Statistics include: food, sleep, and playtime with the cat!')
    time.sleep(1)
    print('There are also a few mini-games in this program!')

    while True:
        print(f'Statistics for cat {name}! ')
        time.sleep(1)
        print(f'Cat has eaten {food} times! ')
        time.sleep(1)
        print(f'Cat has slept {sleep} times! ')
        time.sleep(1)
        print(f'You played with the cat {play} times! ')
        time.sleep(1)
        print('What would you like to record?')
        time.sleep(1)
        score = input('Ate = 1, slept = 2, played = 3, mini-games = 4, exit = 5, about = 6: ')

        if score == '1':
            food += 1
            save_game(food, sleep, play, fish, name)
        elif score == '2':
            sleep += 1
            save_game(food, sleep, play, fish, name)
        elif score == '3':
            play += 1
            save_game(food, sleep, play, fish, name)
        elif score == '4':
            print('Which mini-game would you like to play?')
            time.sleep(1)
            score1 = input('Fishing = 1, guess the number = 2: ')
            if score1 == '1':
                print(f'You have earned {fish} points in total from fishing!')
                print('You get 5 casts. Random fish rarity')
                items = ["perch", "pike", "carp", "boot", "seaweed", "goldfish"]
                for _ in range(5):
                    catch = random.choice(items)
                    points = random.randint(1, 5)
                    print(f'Points for this fish: {points}')
                    input("Press Enter to cast the rod...")
                    time.sleep(1)
                    print('Resting...')
                    time.sleep(1)
                    print('Drinking tea...')
                    time.sleep(3)
                    print('Plop...')
                    time.sleep(2)
                    winsound.Beep(800, 500)
                    print('Something\'s biting!')
                    for _ in range(3):
                        winsound.Beep(800, 100)
                    print(f'You caught {catch}!')
                    time.sleep(1)
                    if catch in ["perch", "pike", "carp", "goldfish"]:
                        fish += points
                        print(f"+{points} points to fish!")
                    else:
                        print("Trash — no points awarded")
                    save_game(food, sleep, play, fish, name)
                print(f"Fishing complete. Total points: {fish}")
            elif score1 == '2':
                print("\n Guess the number from 1 to 3!")
                secret = random.randint(1, 3)
                try:
                    guess = int(input("Your guess: "))
                    if guess == secret:
                        print("The cat purrs! You guessed it!")
                        fish += 1
                        save_game(food, sleep, play, fish, name)
                        print("+1 to play sessions with the cat!")
                    else:
                        print(f"Wrong guess. The cat was thinking of {secret}. Better luck next time.")
                except:
                    print("You need to enter the number 1, 2, or 3.")
                time.sleep(2)
        elif score == '5':
            save_game(food, sleep, play, fish, name)
            print(f"Goodbye! {name} will be waiting for you tomorrow.")
            break
        elif score == '6':
            print("""
            ============================================================
                                  CatCounter v1.2
            ============================================================

               Cat care tracker in the console.

               Features:
               • Feeding, sleep, play tracker
               • Two mini-games (fishing, guess the number)
               • Auto-save to JSON
               • Russian / English

               Developer:     Xintov
               License:       MIT

               Thanks for using!
            ============================================================
            """)
            input("Press Enter to return to menu...")
            continue
