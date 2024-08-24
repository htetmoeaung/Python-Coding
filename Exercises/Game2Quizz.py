def newGame():
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in questions:
        print('-------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)
        correct_guess += checkAnswer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guess, guesses)


def checkAnswer(answer, guess):
    score = 0
    if answer == guess:
        # print('CORRECT!!')
        return 1
    else:
        # print('WRONG!!')
        return 0


def display_score(correct_guesses, guesses):
    print('-------------------')
    print('RESULTS')
    print('-------------------')
    print('Answer: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()
    print('Guesses: ', end='')
    for i in guesses:
        print(i, end=' ')
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print('Your score is ', score, ' %')


def play_again():
    user = input('Want to play again? (yes/no): ').lower()
    if user == 'yes':
        return True
    else:
        return False


questions = {
    "Who created Python?: ": 'A',
    "What year was python created?: ": 'B',
    "Python is tribute to which group?: ": 'C',
    "Is the Earth round?: ": 'D'
}

options = [
    ['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerberg'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
    ['A. Ture', 'B. False', 'C. Sometimes', "D. What's Earth?"]
]

newGame()
while play_again():
    newGame()
print('Bye, Thank for using our services ')
