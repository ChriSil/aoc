import sys

I = {(x, y): c for y, line in enumerate(open(sys.argv[1]).readlines())
     for x, c in enumerate(line.strip())}


def adjacent(xy):
    (x, y) = xy
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def is_possible_move(xy, nxy):
    return ord(I[nxy].replace("E", 'z')) - ord(I[xy].replace("S", "a")) <= 1 if nxy in I else False


def possible_adjecents(xy):
    return (nxy for nxy in adjacent(xy) if is_possible_move(xy, nxy))


def flood(dist, layers):
    edge = set(nxy for xy in layers[-1]
               for nxy in possible_adjecents(xy) if nxy not in dist)

    dist.update({xy: len(layers) for xy in edge})

    if edge:
        flood(dist, layers + [edge])


def distance(start, end):
    dist = {start: 0}
    flood(dist, [{start}])
    return dist[end] if end in dist else 9999


def find_all(values):
    return (xy for (xy, v) in I.items() if v in values)


def find(value):
    return next(find_all(value))


if __name__ == "__main__":
    print("1:", distance(find("S"), find("E")))
    print("2:", min(distance(start, find("E")) for start in find_all(['a', 'S'])))
