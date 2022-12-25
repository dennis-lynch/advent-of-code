"""
"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response:
X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round.
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

from path import Path

input_path = Path(__file__) / ".." / "input-2.txt"
input_path = input_path.abspath()

SCORE_AMOUNTS = {"X": 1, "Y": 2, "Z": 3}
PLAY_REMAP = {"X": "A", "Y": "B", "Z": "C"}


def check_win(player1, player2):
    if player1 == "A":
        if player2 == "Z":
            return False
        elif player2 == "Y":
            return True
    elif player1 == "B":
        if player2 == "Z":
            return True
        elif player2 == "X":
            return False
    elif player1 == "C":
        if player2 == "X":
            return True
        elif player2 == "Y":
            return False


point_total = 0
round = 0
with open(input_path, "r") as infile:
    for line in infile:
        round += 1
        if line in ['\n', '\r\n']:
            continue
        player1, player2 = line.strip().split(" ")
        point_total += SCORE_AMOUNTS[player2]
        if player1 == PLAY_REMAP[player2]:  # Draw
            point_total += 3
            continue
        if check_win(player1, player2):
            point_total += 6
        # print(f"{player1} - {player2} : {point_total}")


print(f"Point total: {point_total}")
