from player import Player

def gen_options (options):
    o_pairs = {}
    for i, option in enumerate(options):
        o_pairs[i] = option
        print()

def main():
    user = Player(404, 909, 42, 242, 22, 99, 19, 12, 
                  9, 4, 9, 1, 2, 3, {"bob":2, "not bob":0}, 4, {"gay":4, "not gay":0}
                )
    print(user)

if __name__ == "__main__":
    main()