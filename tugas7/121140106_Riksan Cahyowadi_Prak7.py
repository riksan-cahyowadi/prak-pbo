import tkinter as tk
from random import randint

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Tebak Angka")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        self.master.config(bg="gray")
        
        self.secret_number = randint(1, 100)
        self.guesses_left = 5
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Tebak angka antara 1-100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.master, text="Tebak !", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

        self.retry_button = tk.Button(self.master, text="Coba Lagi", command=self.reset_game, state=tk.DISABLED)
        self.retry_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid!")
            return

        if guess == self.secret_number:
            self.result_label.config(text="Anda benar!")
            self.submit_button.config(state=tk.DISABLED)
            self.retry_button.config(state=tk.NORMAL)
        elif guess < self.secret_number:
            self.result_label.config(text="Angka terlalu kecil. Tebakan tersisa: {}".format(self.guesses_left))
        else:
            self.result_label.config(text="Angka terlalu besar. Tebakan tersisa: {}".format(self.guesses_left))

        self.guesses_left -= 1

        if self.guesses_left == 0:
            self.result_label.config(text="Anda kalah! Angka yang benar adalah {}".format(self.secret_number))
            self.submit_button.config(state=tk.DISABLED)
            self.retry_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.secret_number = randint(1, 100)
        self.guesses_left = 5
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.retry_button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
