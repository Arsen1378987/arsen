import random
import string
edjectives = ["sleepy","awful","free",'OLD','super']
print("привет,ты хочешь создать пароль?")

while True:
    nouns = ["apple","phone",'android','kakshka','password']
    prilagatelnoe = random.choice(edjectives)
    cuchestvitelnoe = random.choice(nouns)
    number = random.randrange(0,150)
    cimvol = random.choice(string.punctuation)
    passw0rd = prilagatelnoe + cuchestvitelnoe + str(number) + cimvol
    print(f"вот тебе и готов пароль {passw0rd}")
    AgreeOrNoteAgree = input("сгенерировать другой пароль?   ВВедите да или нет:")
    if AgreeOrNoteAgree == "нет":
        break