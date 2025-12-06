def main(rotations):
    current = 50
    onzero = 0
    for r in rotations:
        dir, amt = r[0], int(r[1:])
        if dir == "L":
            current = (current - amt) % 100
        else:
            current = (current + amt) % 100
        if current == 0:
            onzero += 1

    return onzero


if __name__ == "__main__":
    with open("./input.txt") as f:
        print(main(f.read().split("\n")[:-1]))
