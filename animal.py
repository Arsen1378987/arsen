#def check_guess(guess , answer):
#    global score
 #   if guess == answer:
 #       print("молодец ответ правильный,даже младенцы знают ответ")
  #      score = score + 1
#score = 0
#print("Здравствуй,запускается игра животные")
#guess1 = input("Какой медведь живет за полярным кругом?")
#check_guess(guess1,",белый медведь")


guess1 = input("какое из животных рыба?\n \
1)кит\n 2)дельфин\n 3)акула\n 4)кальмар\n \
введите 1, 2, 3 или 4. ")
check_guess(guess, "3")
if guess1 == guess:
    print("молодец")
