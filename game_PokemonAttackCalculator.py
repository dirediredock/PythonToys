# Pokemon Attack Calculator

# Source: https://niantic.helpshift.com/a/pokemon-go/?s=gyms-battle&f=type-effectiveness-in-battle&l=en&p=web

print(
    """
    In Pokemon Go there are 18 creature types, and this matters in battle
    strategy. For example, Fire attacking Grass is "super effective", or 2-fold
    damage, while on the flip side, Grass attacking Fire is "not very
    effective", or 0.5-fold damage. Most of the time the effect is "normal", or
    1-fold damage. However, there are special cases like Electric attacking
    Ground and Poison attacking Steel where the target is immune, so there is
    "no effect", or zero damage. Listed below are the 18 Pokemon types:

    01 Normal
    02 Fire
    03 Water
    04 Grass
    05 Electric
    06 Ice
    07 Fighting
    08 Poison
    09 Ground
    10 Flying
    11 Psychic
    12 Bug
    13 Rock
    14 Ghost
    15 Dragon
    16 Dark
    17 Steel
    18 Fairy
    """
)

array = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 1, 2],
    [2, 1, 1, 3, 2, 3, 2, 2, 2, 2, 2, 3, 1, 2, 1, 2, 3, 2],
    [2, 3, 1, 1, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 1, 2, 2, 2],
    [2, 1, 3, 1, 2, 2, 2, 1, 3, 1, 2, 1, 3, 2, 1, 2, 1, 2],
    [2, 2, 3, 1, 1, 2, 2, 2, 0, 3, 2, 2, 2, 2, 1, 2, 2, 2],
    [2, 1, 1, 3, 2, 1, 2, 2, 3, 3, 2, 2, 2, 2, 3, 2, 1, 2],
    [3, 2, 2, 2, 2, 3, 2, 1, 2, 1, 1, 1, 3, 0, 2, 3, 3, 1],
    [2, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 0, 3],
    [2, 3, 2, 1, 3, 2, 2, 3, 2, 0, 2, 1, 3, 2, 2, 2, 3, 2],
    [2, 2, 2, 3, 1, 2, 3, 2, 2, 2, 2, 3, 1, 2, 2, 2, 1, 2],
    [2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 1, 2, 2, 2, 2, 0, 1, 2],
    [2, 1, 2, 3, 2, 2, 1, 1, 2, 1, 3, 2, 2, 1, 2, 3, 1, 1],
    [2, 3, 2, 2, 2, 3, 1, 2, 1, 3, 2, 3, 2, 2, 2, 2, 1, 2],
    [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 1, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 1, 0],
    [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 3, 2, 2, 3, 2, 1, 2, 1],
    [2, 1, 1, 2, 1, 3, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 1, 3],
    [2, 1, 2, 2, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2, 3, 3, 1, 2],
]

attack = input("From the list above, pick your attack type: ")
target = input("Now pick the type of the Pokemon that receives the attack: ")

attack = attack.lower()
target = target.lower()

lookup = {
    "normal": 0,
    "fire": 1,
    "water": 2,
    "grass": 3,
    "electric": 4,
    "ice": 5,
    "fighting": 6,
    "poison": 7,
    "ground": 8,
    "flying": 9,
    "psychic": 1,
    "bug": 11,
    "rock": 12,
    "ghost": 13,
    "dragon": 14,
    "dark": 15,
    "steel": 16,
    "fairy": 17,
}

indexAttack = lookup[attack]
indexTarget = lookup[target]

list = array[indexAttack]
value = list[indexTarget]

print("\n")

if value == 3:
    print(
        attack.capitalize()
        + " attacks "
        + target.capitalize()
        + ", it is super effective."
    )

if value == 2:
    print(attack.capitalize() + " attacks " + target.capitalize() + ", regular damage.")

if value == 1:
    print(
        attack.capitalize()
        + " attacks "
        + target.capitalize()
        + ", it is not very effective."
    )

if value == 0:
    print(
        attack.capitalize()
        + " attacks "
        + target.capitalize()
        + ", there is no effect."
    )

print("\n")
