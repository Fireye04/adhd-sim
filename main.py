from player import Player
from encounter import Encounter


def main():
    relationships = {"bob": 0, "not bob": 0}
    skills = {"gay": 0, "not gay": 0}

    stats = {
        "stress": [50, 0],
        "happiness": [50, 0],
        "hunger": [50, 0],
        "hygiene": [50, 0],
        "sleep": [50, 0],
        "bananas": [50, 0],
        "grades": [50, 0],
        "relationships": [relationships, 0],
        "skills": [skills, 0],
    }

    user = Player(stats)
    print(user)

    # options: [option1, option2]
    # option1: [option prompt, pre-reqs, result prompt, results]
    o1 = [
        [
            "be cool",
            ["self.player.stress < 60", "self.player.happiness > 20", "sleep > 60"],
            "you socialize with bob and have yourself a bit of fun!",
            ["self.player.relationships2[bob] += 1", "self.player.happiness += 5"],
        ],
        [
            "be uncool",
            ["self.player.happiness > 10"],
            "you try to be cool but are too stressed.",
            ["self.player.stress += 5", "self.player.happiness -=5"],
        ],
        [
            "cry in corner",
            [],
            "you cry in the corner. not bob comes and comforts you.",
            ["self.player.stress+=5", "self.player.relationships[not bob] += 2"],
        ],
    ]

    relationships2: [relationships, 0]
    i = 0
    # EVAL IS FOR LOGIC EXEC IS FOR CODE

    exec("i+=1")

    e1 = Encounter("you're at a party, what do you do?", o1, user)
    e1.gen_options()


if __name__ == "__main__":
    main()
