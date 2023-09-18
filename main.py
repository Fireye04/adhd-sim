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

    o1 = [
        [
            "be cool",
            ["stress[0] < 60"],
            [
                "relationships2[0][bob] += 1",
            ],
        ],
        ["be uncool", []],
        [
            "cry in corner",
        ],
    ]

    relationships2: [relationships, 0]
    i = 0
    # EVAL IS FOR LOGIC EXEC IS FOR CODE

    exec("i+=1")

    # e1 = Encounter("you're at a party, what do you do?", o1, user)


if __name__ == "__main__":
    main()
