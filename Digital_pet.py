class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting from a mid-level for balance
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food! Hunger: {old_hunger} → {self.hunger}, Happiness increased to {self.happiness}.")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap! Energy: {old_energy} → {self.energy}.")

    def play(self):
        if self.energy >= 2:
            old_energy = self.energy
            old_happiness = self.happiness
            old_hunger = self.hunger

            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)

            print(f"{self.name} played around! Energy: {old_energy} → {self.energy}, "
                  f"Happiness: {old_happiness} → {self.happiness}, Hunger: {old_hunger} → {self.hunger}.")
        else:
            print(f"{self.name} is too tired to play. Let them sleep first!")

    def get_status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None yet!'}")
        print("----------------------------")

    def train(self, trick):
        if trick and isinstance(trick, str):
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: '{trick}'! Happiness increased to {self.happiness}.")
        else:
            print("Invalid trick name. Make sure it's a non-empty string!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")

# Example usage
if __name__ == "__main__":
    my_pet = Pet("Buddy")
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("Roll Over")
    my_pet.show_tricks()
    my_pet.get_status()
