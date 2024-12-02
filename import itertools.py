import itertools

l = ["R", "G", "B", "Y"]

color_map = {
    Color.BLUE: 'B',
    Color.BLUE: 'B',
    Color.BLUE: 'B',
    Color.BLUE: 'B',
    Color.BLUE: 'B',
}
x = input("enter letter")

colors = itertools.cycle(l)


# Advance list

while x != next(colors):
    pass

# Print advanced list
menu = [x]
for i in range(len(l)-1):
    menu.append(next(colors))
    # if color == target_letter:
    #     print(f"Stopped at {target_letter}.")
    #     break

print(*menu)
