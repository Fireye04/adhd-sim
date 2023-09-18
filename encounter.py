from player import Player


class Encounter:
    def __init__(
        self,
        _prompt: str,
        _options: list[list[str, list[str], list[str]]],
        _player: Player,
    ):
        self.prompt = _prompt
        # list containing lists of [the option text, and a list of option pre-reqs]
        self.options = _options

        self.player = _player

    def run(self):
        print(self.prompt)

        self.gen_options(self)

    def gen_options(options):
        o_pairs = {}
        for i, option in enumerate(options):
            o_pairs[i + 1] = option

        for key, item in o_pairs.items():
            print(f"{key}. {item}")  # Add cost here later

        # manages user input
        # add cost modifiers later
        valid = False
        while not valid:
            try:
                useri = int(input(""))
                if useri in o_pairs.keys():
                    valid = True
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input")
