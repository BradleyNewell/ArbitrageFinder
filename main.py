import tkinter as tk
from tkinter import messagebox


class ArbitrageFinder:
    def __init__(self, master):
        """Configuration of the main window and setting initial variables, labels and button for user input."""
        self.master = master
        self.frame = tk.Frame(self.master)

        self.wager = tk.IntVar()
        self.odds_1 = tk.DoubleVar()
        self.odds_2 = tk.DoubleVar()
        self.bet_1 = tk.DoubleVar()
        self.bet_2 = tk.DoubleVar()
        self.total = tk.StringVar(self.frame)
        self.percentage_increase = tk.StringVar(self.frame)
        self.wager_label = tk.Label(self.frame, text="Total Wager: ")
        self.odds_1_label = tk.Label(self.frame, text="First Odds: ")
        self.odds_2_label = tk.Label(self.frame, text="Second Odds: ")
        self.bet_1_label = tk.Label(self.frame, text="First Bet: ")
        self.bet_2_label = tk.Label(self.frame, text="Second Bet: ")
        self.total_label = tk.Label(self.frame, text="Gross return")
        self.total_percent_label = tk.Label(self.frame, text="Percentage Increase: ")
        self.display_total = tk.Entry(self.frame, textvariable=self.total, relief="raised", state="readonly")
        self.display_percentage = tk.Entry(self.frame, textvariable=self.percentage_increase, state="readonly")
        self.get_total_wager = tk.Entry(self.frame, textvariable=self.wager)
        self.get_odds_1 = tk.Entry(self.frame, textvariable=self.odds_1)
        self.get_odds_2 = tk.Entry(self.frame, textvariable=self.odds_2)
        self.get_bet_1 = tk.Entry(self.frame, textvariable=self.bet_1, state="readonly")
        self.get_bet_2 = tk.Entry(self.frame, textvariable=self.bet_2, state="readonly")
        self.submit_button = tk.Button(self.frame, command=lambda: self.find_arbitrage(), text="Submit")

        # Arranging objects to frame using grid

        self.wager_label.grid(row=0, column=2)
        self.get_total_wager.grid(row=1, column=2)
        self.odds_1_label.grid(row=2, column=1)
        self.get_odds_1.grid(row=3, column=1, padx=5)
        self.odds_2_label.grid(row=4, column=1)
        self.get_odds_2.grid(row=5, column=1, padx=5)
        self.bet_1_label.grid(row=2, column=3)
        self.get_bet_1.grid(row=3, column=3, padx=5)
        self.bet_2_label.grid(row=4, column=3)
        self.get_bet_2.grid(row=5, column=3, padx=5)
        self.total_percent_label.grid(row=6, column=2)
        self.display_percentage.grid(row=8, column=2)
        self.total_label.grid(row=9, column=2)
        self.display_total.grid(row=10, column=2)
        self.submit_button.grid(row=14, column=2)
        self.frame.grid()

    def show_percent_change(self):

        # Show the difference between the starting wager and the potential winnings as a percentage

        wager = float(self.wager.get())
        comb_odds = float(self.odds_1.get() * self.bet_1.get())
        final_percent = comb_odds - wager / wager * 100
        self.percentage_increase.set(format(final_percent, '.2f') + "%")

    def get_total_return(self):

        # Computes the total sum and formats it to two decimal places for readability

        formatted_total = self.bet_1.get() * self.odds_1.get()
        self.total.set("£" + format(formatted_total, '.2f'))

    def find_arbitrage(self):

        """ Main function, divides the wager by the 1st and second odds in order to find the most efficient way
        of dividing the sum the user wishes to place between the two options given, checks if values given are valid and
        also formats the output."""

        try:
            odds1 = self.odds_1.get()
            odds2 = self.odds_2.get()
            wager = self.wager.get()
            first_bet = wager / (float(odds1) / float(odds2) + 1)
            second_bet = wager / (float(odds2) / float(odds1) + 1)
            self.bet_1.set(format(first_bet, '.2f'))
            self.bet_2.set(format(second_bet, '.2f'))
            self.get_total_return()
            self.show_percent_change()
        except (ValueError, tk.TclError):
            tk.messagebox.showerror("Error", "Please enter a valid number")
            pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arbitrage Finder")
    root.geometry("392x250")
    ArbitrageFinder(root)
    root.mainloop()
