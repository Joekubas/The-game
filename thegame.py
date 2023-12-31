import tkinter as tk


class NumberGuessingGame:
    def __init__(self, root):
        self.guesses = []
        self.root = root
        self.root.title("Number Guessing Game")

        self.min_num_label = tk.Label(root, text="Enter the minimum number:")
        self.min_num_label.pack()

        self.min_num_entry = tk.Entry(root)
        self.min_num_entry.pack()

        self.max_num_label = tk.Label(root, text="Enter the maximum number:")
        self.max_num_label.pack()

        self.max_num_entry = tk.Entry(root)
        self.max_num_entry.pack()

        self.secret_number_label = tk.Label(root, text="Enter the secret number:")
        self.secret_number_label.pack()

        self.secret_number_entry = tk.Entry(root, show='****')
        self.secret_number_entry.pack()

        self.max_attempts_label = tk.Label(root, text="Enter the maximum number of guesses:")
        self.max_attempts_label.pack()

        self.max_attempts_entry = tk.Entry(root)
        self.max_attempts_entry.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        min_num = int(self.min_num_entry.get())
        max_num = int(self.max_num_entry.get())
        max_attempts = int(self.max_attempts_entry.get())
        secret_number = int(self.secret_number_entry.get())

        if secret_number < min_num:
            raise ValueError("Typed-in number is too low")
        if secret_number > max_num:
            raise ValueError("Typed-in number is too high")
        if min_num <= secret_number <= max_num:
            print("The typed-in number is correct!")

        attempts = 1  # Start from 1 (the first attempt)

        result_label = tk.Label(self.root, text="")
        result_label.pack()

        def check_guess():
            nonlocal attempts
            guess = int(guess_entry.get())
            # Append the user's guess to the list
            self.guesses.append(guess)

            if guess == secret_number:
                result_label.config(
                    text=f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            elif guess < secret_number:
                result_label.config(text="Too low. Try again.")
            else:
                result_label.config(text="Too high. Try again.")

            if attempts == max_attempts and guess != secret_number:
                result_label.config(text=f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

            # Display the guess attempt number alongside the guess
            show_guess = tk.Label(self.root, text=f"Attempt {attempts}: {guess}")
            show_guess.pack()

            attempts += 1

        guess_label = tk.Label(self.root, text="Enter your guess:")
        guess_label.pack()

        guess_entry = tk.Entry(self.root)  # Use 'show' option to hide input
        guess_entry.pack()

        guess_button = tk.Button(self.root, text="Guess", command=check_guess)
        guess_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
