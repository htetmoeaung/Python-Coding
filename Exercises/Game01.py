import random

print('Welcome to Rock,Paper or Scissor Game \n Made by HtetMoeAung')


def display_score(score):
    print('Your win matches: ',score)
def check_rewards(score):
    if score >= 10:
        print('Winner!!!!!')

while True:

    item = ['rock', 'paper', 'scissor']
    computer = random.choice(item)
    player = None
    score = 0

    while player not in item:
        player = input('rock, paper, scissor: ').lower()
        if player == computer:
            print('Computer: ', computer)
            print('Player: ', player)
            print('Tie')
        elif player == 'rock':
            if computer == 'paper':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Computer Win')
            elif computer == 'scissor':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Player Win')
                score += 1
            else:
                print('Computer: ', computer)
                print('Player: ', player)
                print('Tie')
        elif player == 'paper':
            if computer == 'rock':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Player Win')
                score += 1
            elif computer == 'scissor':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Computer Win')
            else:
                print('Computer: ', computer)
                print('Player: ', player)
                print('Tie')
        elif player == 'scissor':
            if computer == 'paper':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Player Win')
                score += 1
            elif computer == 'rock':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Computer Win')
            else:
                print('Computer: ', computer)
                print('Player: ', player)
                print('Tie')
    display_score(score)
    playAgain = input('Play again? (yes/no): ').lower()
    if playAgain == 'no':
        break
print('Thank you for playing my game')

files = ['work','work','work','work','work']

