from player import Player


def gen_options(options):
    o_pairs = {}
    for i, option in enumerate(options):
        o_pairs[i + 1] = option

    for key, item in o_pairs.items():
        print(f"{key}. {item}")  # Add cost here later

    valid = False
    while not valid:
        try:
            useri = int(input(""))
            if useri in o_pairs.keys():
                valid = True
                return useri
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")


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

    options = ["be cool", "be uncool", "cry in corner"]

    gen_options(options)


if __name__ == "__main__":
    main()
