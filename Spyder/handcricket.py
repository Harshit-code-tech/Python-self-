import random

def play_hand_cricket():
    print("Welcome to Hand Cricket!")
    score, wickets = 0, 0

    while wickets < 3:
        bowl_score = random.randint(1, 6)
        print(f"The bowler scores {bowl_score} runs")
        bat_score = int(input("Enter your score (1-6): "))
        if bat_score < 1 or bat_score > 6:
            print("Invalid input! Try again.")
            continue
        if bat_score == bowl_score:
            print("You're out!")
            wickets += 1
            if wickets == 3:
                break
        else:
            score += bat_score
            print(f"You score {bat_score} runs")

    print(f"Your final score is {score} runs")
    print("Thanks for playing!")

play_hand_cricket()
