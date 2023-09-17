from player import Player


def gen_options(options):
    o_pairs = {}
    for i, option in enumerate(options):
        o_pairs[i] = option
        print()


def main():
    relationships = {"bob": 2, "not bob": 0}
    skills = {"gay": 4, "not gay": 0}

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


if __name__ == "__main__":
    main()
