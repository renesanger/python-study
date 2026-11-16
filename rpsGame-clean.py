import random

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

moves = {
    'r': 'ROCK',
    'p': 'PAPER',
    's': 'SCISSORS'
}

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    player_move = input(
        'Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n> '
    ).lower()

    if player_move == 'q':
        break

    if player_move not in moves:
        print('Invalid move. Try again.')
        continue

    computer_move = random.choice(list(moves))

    print(f'{moves[player_move]} versus {moves[computer_move]}')

    if player_move == computer_move:
        print("It's a tie!")
        ties += 1

    elif (player_move, computer_move) in [
        ('r', 's'),
        ('p', 'r'),
        ('s', 'p')
    ]:
        print('You win!')
        wins += 1

    else:
        print('You lose!')
        losses += 1