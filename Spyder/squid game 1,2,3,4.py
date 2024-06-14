#without those import
#1
import time
import random

def red_light_green_light(players):
    print("Playing Red Light, Green Light...")
    time.sleep(1)
    leader = random.choice(players)
    print(f"The leader is {leader}")
    time.sleep(1)
    print("Red light, green light...")
    time.sleep(1)
    print("Green light!")
    time.sleep(1)
    for i in range(3):
        print("Red light!")
        time.sleep(1)
    print("Red light!")
    time.sleep(1)
    eliminated = []
    for player in players:
        if player != leader:
            print(f"{player} is moving...")
            time.sleep(0.5)
            if random.choice([True, False]):
                eliminated.append(player)
                print(f"{player} has been eliminated!")
    return [player for player in players if player not in eliminated]

#2
import time
import random

def honeycomb(players):
    print("Playing Honeycomb...")
    time.sleep(1)
    pattern = "umbrella"
    print("The pattern is:", pattern)
    time.sleep(1)
    eliminated = []
    for player in players:
        print(f"{player} is carving...")
        time.sleep(1)
        if random.choice([True, False]):
            eliminated.append(player)
            print(f"{player} broke the honeycomb and has been eliminated!")
        else:
            print(f"{player} finished carving the pattern and is safe!")
    return [player for player in players if player not in eliminated]
#3
import time
import random

def tug_of_war(players):
    print("Playing Tug of War...")
    time.sleep(1)
    team1 = players[:len(players)//2]
    team2 = players[len(players)//2:]
    print("Team 1:", team1)
    print("Team 2:", team2)
    time.sleep(1)
    winner = None
    while winner is None:
        print("Pull!")
        time.sleep(1)
        if random.choice([True, False]):
            team1, team2 = team2, team1
            print("Team 2 wins!")
        if len(team1) == 0:
            winner = team2
            print("Team 2 wins!")
        elif len(team2) == 0:
            winner = team1
            print("Team 1 wins!")
    eliminated = [player for player in players if player not in winner]
    return winner, eliminated

#4
import time
import random

def marbles(players):
    print("Playing Marbles...")
    time.sleep(1)
    player1 = random.choice(players)
    player2 = [player for player in players if player != player1][0]
    print(f"{player1} is playing against {player2}")
    time.sleep(1)
    marbles1 = random.randint(1, 5)
    marbles2 = random.randint(1, 5)
    print(f"{player1} has {marbles1} marbles")
    print(f"{player2} has {marbles2} marbles")
    time.sleep(1)
    if marbles1 > marbles2:
        winner = player1
        eliminated = player2
    elif marbles1 < marbles2:
        winner = player2
        eliminated = player1
    else:
        print("It's a tie! Playing again...")
        time.sleep(1)
        return marbles(players)
    print(f"{winner} has won the game and is safe!")
    return [player for player in players if player != eliminated]
#5
import time
import random

def glass_bridge(players):
    print("Playing Glass Bridge...")
    time.sleep(1)
    panels = ["safe"] * 18 + ["broken"]
    random.shuffle(panels)
    print("The panels are:")
    for i in range(0, len(panels), 3):
        print("  ".join(panels[i:i+3]))
    time.sleep(1)
    eliminated = []
    for player in players:
        print(f"{player} is crossing the bridge...")
        time.sleep(1)
        for panel in panels:
            if panel == "broken":
                eliminated.append(player)
                print(f"{player} fell through the bridge and has been eliminated!")
                break
            time.sleep(0.5)
        else:
            print(f"{player} has crossed the bridge and is safe!")
    return [player for player in players if player not in eliminated]
#6
import random
import time

def marble_game(players):
    print("Playing Marble Game...")
    time.sleep(1)
    print("Each player has to flick their marble to hit the target marble and get it outside the circle.")
    time.sleep(2)
    print("The last player to hit the target marble or the player whose marble is still inside the circle loses.")
    time.sleep(3)
    marbles = {}
    for player in players:
        marbles[player] = 1
    while len(players) > 1:
        for player in players:
            if marbles[player] == 0:
                continue
            input(f"{player}'s turn. Press enter to flick your marble.")
            if random.random() < 0.5:
                print(f"{player} missed the target marble.")
                continue
            print(f"{player} hit the target marble!")
            if random.random() < 0.5:
                print(f"{player} failed to get their marble outside the circle.")
                marbles[player] = 0
                players.remove(player)
                if len(players) == 1:
                    break
            else:
                print(f"{player} successfully got their marble outside the circle.")
    print(f"{players[0]} wins!")
    return players[0]


#with those functions
#1
import time
import cv2
import mediapipe as mp
import numpy as np

def red_light_green_light(players):
    print("Playing Red Light, Green Light...")
    time.sleep(1)
    print("Green light!")
    time.sleep(1)
    print("Red light!")
    eliminated = []
    while len(players) > 0:
        for player in players:
            print(f"{player} is moving...")
            time.sleep(0.5)
            cap = cv2.VideoCapture(0)
            with mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=1,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            ) as hands:
                success, image = cap.read()
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        if hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y < 0.5:
                            print(f"{player} has moved after the red light and has been eliminated!")
                            eliminated.append(player)
                            players.remove(player)
                            break
                if cv2.waitKey(5) & 0xFF == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
        print("Green light!")
        time.sleep(1)
        print("Red light!")
    print(f"The following players have been eliminated: {', '.join(eliminated)}")
    return [player for player in players if player not in eliminated]

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#2
import time
import cv2
import mediapipe as mp
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from cvzone.Utils import stackImages

def honeycomb(players):
    print("Playing Honeycomb...")
    time.sleep(1)
    print("Please draw a shape on the honeycomb.")
    time.sleep(1)
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        with SelfiSegmentation() as segmentor:
            while True:
                success, image = cap.read()
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                    hand_landmarks = results.multi_hand_landmarks[0]
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    points = []
                    for landmark in hand_landmarks.landmark:
                        x, y, z = landmark.x, landmark.y, landmark.z
                        points.append([x, y])
                    points = np.array(points)
                    shape = cv2.convexHull(points).astype(np.int32)
                    cv2.drawContours(image, [shape], -1, (0, 255, 0), 3)
                    mask = segmentor.removeBG(image, threshold=0.8)
                    inv_mask = cv2.bitwise_not(mask)
                    bg_image = cv2.imread("honeycomb.jpg")
                    bg_image = cv2.resize(bg_image, (image.shape[1], image.shape[0]))
                    fg_image = cv2.bitwise_and(image, image, mask=mask)
                    bg_image = cv2.bitwise_and(bg_image, bg_image, mask=inv_mask)
                    image = cv2.add(bg_image, fg_image)
                cv2.imshow('Squid Game', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
            return players
          
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

#3
import time
import cv2
import mediapipe as mp
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from cvzone.Utils import stackImages

def tug_of_war(players):
    print("Playing Tug of War...")
    time.sleep(1)
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as holistic:
        with SelfiSegmentation() as segmentor:
            while True:
                success, image = cap.read()
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = holistic.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.pose_landmarks:
                    pose_landmarks = results.pose_landmarks
                    mp_drawing.draw_landmarks(
                        image, pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                    left_hip = pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HIP].y
                    right_hip = pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HIP].y
                    distance = abs(left_hip - right_hip)
                    if distance < 0.05:
                        text = "It's a tie!"
                    elif left_hip > right_hip:
                        text = "Left team wins!"
                    else:
                        text = "Right team wins!"
                    cv2.putText(
                        image, text, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    mask = segmentor.removeBG(image, threshold=0.8)
                    inv_mask = cv2.bitwise_not(mask)
                    bg_image = cv2.imread("tug_of_war.jpg")
                    bg_image = cv2.resize(bg_image, (image.shape[1], image.shape[0]))
                    fg_image = cv2.bitwise_and(image, image, mask=mask)
                    bg_image = cv2.bitwise_and(bg_image, bg_image, mask=inv_mask)
                    image = cv2.add(bg_image, fg_image)
                cv2.imshow('Squid Game', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
            cv2.destroyAllWindows()
            cap.release()
            return players
          
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

#4
import time
import random
import cv2
import mediapipe as mp
import numpy as np

def marbles(players):
    print("Playing Marbles...")
    time.sleep(1)
    player1 = random.choice(players)
    player2 = [player for player in players if player != player1][0]
    print(f"{player1} is playing against {player2}")
    time.sleep(1)
    marbles1 = random.randint(1, 5)
    marbles2 = random.randint(1, 5)
    print(f"{player1} has {marbles1} marbles")
    print(f"{player2} has {marbles2} marbles")
    time.sleep(1)
    if marbles1 > marbles2:
        winner = player1
        eliminated = player2
    elif marbles1 < marbles2:
        winner = player2
        eliminated = player1
    else:
        print("It's a tie! Playing again...")
        time.sleep(1)
        return marbles(players)
    print(f"{winner} has won the game and is safe!")
    return [player for player in players if player != eliminated]

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def detect_hand_landmarks(cap):
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.imshow('Squid Game', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
detect_hand_landmarks(cap)

#5
import random
import time
import cv2
import mediapipe as mp
import numpy as np

def glass_bridge(players):
    print("Playing Glass Bridge...")
    time.sleep(1)
    panels = ["safe"] * 18 + ["broken"]
    random.shuffle(panels)
    print("The panels are:")
    for i in range(0, len(panels), 3):
        print("  ".join(panels[i:i+3]))
    time.sleep(1)
    eliminated = []
    for player in players:
        print(f"{player} is crossing the bridge...")
        time.sleep(1)
        for panel in panels:
            if panel == "broken":
                eliminated.append(player)
                print(f"{player} has fallen through the bridge and has been eliminated!")
                break
            time.sleep(0.5)
        else:
            print(f"{player} has safely crossed the bridge!")
    return [player for player in players if player not in eliminated]

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.h

