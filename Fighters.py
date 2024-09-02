import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f"{self.name} attacks {other.name} and does {self.attack_power} damage!")
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero(name="Player")
        self.computer = Hero(name="Computer")

    def start(self):
        print("Game on!")
        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nRound {round_number}")
            # Игрок атакует
            self.player.attack(self.computer)
            print(f"By {self.computer.name} {self.computer.health} health left.")
            if not self.computer.is_alive():
                print(f"{self.computer.name} defeated! {self.player.name} won!")
                break

            # Компьютер атакует
            self.computer.attack(self.player)
            print(f"By {self.player.name} {self.player.health} health left.")
            if not self.player.is_alive():
                print(f"{self.player.name} defeated! {self.computer.name} won!")
                break

            round_number += 1


if __name__ == "__main__":
    game = Game()
    game.start()