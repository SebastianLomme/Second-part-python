# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if speed < 0 or speed > 1:
            raise ValueError
        if endurance < 0 or endurance > 1:
            raise ValueError
        if accuracy < 0 or accuracy > 1:
            raise ValueError

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        sorted_list = sorted([("speed", self.speed),("endurance", self.endurance), ("accuracy", self.accuracy)], key=lambda list: list[1], reverse=True)
        return sorted_list[0]


sebastian = Player("Sebastian", 0.8, 0.6, 0.8)
# print(sebastian.strength())
# print(sebastian.introduce())


# print(sebastian.speed)

class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy

    def compare_players(self, play_1, play_2, strength):
        player_one_strength = getattr(play_1,strength)
        player_two_strength = getattr(play_2,strength)
        if player_one_strength > player_two_strength:
            return play_1.name
        elif player_one_strength < player_two_strength:
            return play_2.name
        elif play_1.strength()[1] > play_2.strength()[1]:
            print("test")
            return play_1.name
        elif play_2.strength()[1] > play_1.strength()[1]:
            print("test")
            return play_2.name
        elif self.sum_player(play_1) > self.sum_player(play_2):
            print("test1")
            return play_1.name
        elif self.sum_player(play_2) > self.sum_player(play_1):
            print("test1")
            return play_2.name
        else:
            return 'These two players might as well be twins!'
        

ray = Commentator("Ray Hudson")
alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.8, 0.2, 0.6)
print(ray.compare_players(alice, bob, 'endurance'))
# print(ray.sum_player(bob))
# print(ray.name)
# print(sebastian.sum_player())