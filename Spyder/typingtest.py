import time
import random

def generate_text(level):
    easy_text = "The quick brown fox jumps over the lazy dog."
    medium_text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    hard_text = "Sphinx of black quartz, judge my vow."
    
    if level == "easy":
        return easy_text
    elif level == "medium":
        return medium_text
    elif level == "hard":
        return hard_text
    else:
        raise ValueError("Invalid level choice. Please choose 'easy', 'medium', or 'hard'.")

def check_accuracy(original_text, typed_text):
    original_words = original_text.split()
    typed_words = typed_text.split()
    correct_words = [w1 for w1, w2 in zip(original_words, typed_words) if w1 == w2]
    accuracy = len(correct_words) / len(original_words) * 100
    return accuracy

def calculate_wpm(start_time, end_time, typed_text):
    words = typed_text.split()
    num_words = len(words)
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = num_words / minutes
    return wpm

def typing_game(level):
    print(f"Level: {level.capitalize()}")

    text = generate_text(level)
    print("Type the following text:")
    print(text)

    input("Press Enter when you are ready to start typing...")
    start_time = time.time()

    typed_text = input("Start typing here:\n")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed_text)
    accuracy = check_accuracy(text, typed_text)
    print(f"Your typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

def create_user_profile():
    name = input("Enter your name: ")
    profile = {"name": name, "easy": [], "medium": [], "hard": []}
    return profile

def save_user_profile(profile):
    # In a real application, you could save the user profile to a file or database.
    print(f"Profile for {profile['name']} saved!")

def load_user_profile():
    # In a real application, you could load the user profile from a file or database.
    # For now, let's use a dummy profile for demonstration purposes.
    return {
        "name": "John Doe",
        "easy": [(50, 80), (55, 90)],       # Format: (WPM, Accuracy)
        "medium": [(40, 75), (60, 85)],
        "hard": [(30, 60), (50, 70)]
    }

def display_progress(profile):
    print(f"Typing Progress for {profile['name']}:")
    print("Difficulty | Best WPM | Best Accuracy")
    print("-" * 36)
    for level in ["easy", "medium", "hard"]:
        best_wpm, best_accuracy = max(profile[level], default=(0, 0))
        print(f"{level.capitalize():<10} | {best_wpm:>8} | {best_accuracy:>13.2f}%")

def main():
    print("Welcome to the Typing Speed Test!")
    print("Choose your level: easy, medium, or hard.")
    level = input("Enter your choice: ").lower()

    try:
        user_profile = load_user_profile()
        print(f"Welcome back, {user_profile['name']}!")
    except FileNotFoundError:
        print("User profile not found. Let's create one!")
        user_profile = create_user_profile()
        save_user_profile(user_profile)

    while True:
        typing_game(level)

        # Update user profile with the latest results
        wpm, accuracy = calculate_wpm(start_time, end_time, typed_text), check_accuracy(text, typed_text)
        user_profile[level].append((wpm, accuracy))

        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != "y":
            break

    # Display user progress and save the updated profile
    display_progress(user_profile)
    save_user_profile(user_profile)

if __name__ == "__main__":
    main()