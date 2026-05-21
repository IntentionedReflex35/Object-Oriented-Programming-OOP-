class Player:
    def __init__(self, name, health, score=0):
        self.name = name
        self.health = health
        self.score = score

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health += amount


player1 = Player("Felix", 100)
player1.take_damage(100)
