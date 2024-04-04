List = ["wow", "look", 13421, 0.0, "heya" "lol"]


#variables can be used both in global and in local in local yuou can only use it in code blocks


def hello(world):
    kev = ' '

    for i in range(len(world) -1, -1, -1):
        kev = kev + world[i]

    print(kev == world)

hello('nodododo')