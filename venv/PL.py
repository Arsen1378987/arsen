# Игрок видит перед собой массив из пяти букв со знавками вопроса
# ['?','?','?','?','?']
# и слова осталось 9 жизней
# Угадай букву
#
# Если угадал, например,  ввел буку м, то видит следюущее
# ['м','?','?','?','?']
# если не угадал, то видит
# ['?','?','?','?','?']
# и слова осталось 8 жизней
# и так пока либо не сгорят жизни либо не угадает все буквы

def UpdateLives(li,word,finWords):
        while li > 0:
            i = 0
            player = input("введи букву если угшадаешь молорик")
            if word == player:
                print("молорик ты все угадал")
                break;
            if word.find(player) >= 0:
                print(f"ты нашёл букву,молодец {li} жизней ")
                findWords = finWords + 1
                if finWords == 6:
                    print("кросавчик ты все угадал ")
                    break;
            else:
                li = li - 1
                print(f"ты не аншёл букву,осталось {li} жизней")
                if li == 0:
                    print("Game over")
                    break;


anyWord = "какашка"
slohnoct = input("hard или easy")
if slohnoct == "hard":
    lives = 6
if slohnoct == "easy":
    lives = 12
findWords = 0
UpdateLives(lives,anyWord,findWords)

