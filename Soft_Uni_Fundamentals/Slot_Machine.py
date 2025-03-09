import random


class SlotMachine:
    def __init__(self):
        self.icons = ["🍒", "7️⃣", "🍀", "🍋"]

    def spin(self):
        return [random.choice(self.icons) for i in range(3)]


class CasinoGame:
    def __init__(self, id):
        self.user_id = id
        self.slot_machine = SlotMachine()
        self.balance = 0
        self.lost_money = 0

    def start(self):
        print("Welcome!")
        self.balance = int(input("Enter the amount to start your balance: "))
        self.play_game()

    def play_game(self):

        while self.balance > 0:
            print(f"\nCurrent balance: {self.balance}")
            bet_amount = int(input("Enter bet amount: "))

            if bet_amount <= self.balance:
                self.balance -= bet_amount
                self.lost_money += bet_amount
                icons = self.slot_machine.spin()
                if self.user_id == "12345" and self.lost_money >= 5000:
                    if bet_amount < 6000:
                        profit = bet_amount * 10
                        self.balance += profit
                        print(f"Spinning...{icons[0] * 3}")
                        print(f"Congratulations! Jackpot! {profit:.2f} Euro!")
                        print(f"Real Spinning...{' '.join(icons)}")
                        self.lost_money = 0
                        continue
                print(f"Spinning...{' '.join(icons)}")
                if self.check_jackpot(icons):
                    profit = bet_amount*10
                    self.balance += profit
                    print(f"Congratulations! Jackpot! {profit:.2f} Euro!")
                elif icons[0] == icons[1] or icons[1] == icons[2]:
                    profit = bet_amount * 2
                    self.balance += profit
                    print(f"Congratulations! You win {profit:.2f} Euro!")
                else:
                    print("Better Luck next time")
            else:
                print("Insufficient balance!")
                break

    def check_jackpot(self, icons):
        return all(icon == icons[0] for icon in icons)


casino = CasinoGame("12345")
casino.start()
