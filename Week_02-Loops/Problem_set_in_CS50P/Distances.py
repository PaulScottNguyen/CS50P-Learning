Distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}

def main():
    for name in Distances.keys():
        print(f"{name} is {Distances[name]} AU from Earth")

main()