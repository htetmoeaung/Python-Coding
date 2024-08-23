import random

print('Welcome to Rock,Paper or Scissor Game \n Made by HtetMoeAung')

while True:

    item = ['rock', 'paper', 'scissor']
    computer = random.choice(item)
    player = None

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
            else:
                print('Computer: ', computer)
                print('Player: ', player)
                print('Tie')
        elif player == 'paper':
            if computer == 'rock':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Player Win')
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
            elif computer == 'rock':
                print('Computer: ', computer)
                print('Player: ', player)
                print('Computer Win')
            else:
                print('Computer: ', computer)
                print('Player: ', player)
                print('Tie')
    playAgain = input('Play again? (yes/no): ').lower()
    if playAgain.__contains__('n'):
        break
print('Thank you for playing my game')