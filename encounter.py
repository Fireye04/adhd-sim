from player import Player


class Encounter:
    def __init__(
        self,
        _prompt: str,
        _options: list[list[str, list[str], str, list[str]]],
        _player: Player,
    ):
        self.prompt = _prompt
        # list containing lists of [the option text, and a list of option pre-reqs]
        self.options = _options

        self.player = _player

    def run(self):
        print(self.prompt)

        self.gen_options(self)

    def gen_options(self):
        o_pairs = {}
        for i, option in enumerate(self.options):
            o_pairs[i + 1] = option

        for key, item in o_pairs.items():
            print(f"{key}. {item[0]} | {', '.join(member for member in item[1])}")  # Add cost here later

        # manages user input
        # add cost modifiers later
        valid = False
        while not valid:
            try:
                useri = int(input(""))
                if useri in o_pairs.keys():
                    if all(eval(item) for item in o_pairs[useri][1]):

                        print(o_pairs[useri][2])

                        exec(o_pairs[useri][3])
                        
                        valid = True
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input")
