# Pokemon Attack Calculator

# Data source: https://niantic.helpshift.com/a/pokemon-go/?s=gyms-battle&f=type-effectiveness-in-battle&l=en&p=web

print(
    """
    In Pokemon Go there are 18 creature types, and this matters in battle
    strategy. For example, Fire attacking Grass is "super effective", or 2-fold
    damage, while on the flip side, Grass attacking Fire is "not very
    effective", or 0.5-fold damage. Most of the time the effect is "normal", or
    1-fold damage. However, there are special cases like Electric attacking
    Ground and Poison attacking Steel where the target is immune, so there is
    "no effect", or zero damage. Listed below are the 18 Pokemon types:

    - Normal
    - Fire
    - Water
    - Grass
    - Electric
    - Ice
    - Fighting
    - Poison
    - Ground
    - Flying
    - Psychic
    - Bug
    - Rock
    - Ghost
    - Dragon
    - Dark
    - Steel
    - Fairy
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

message1 = "From the list above, pick your attack type: "
message2 = "Now pick the type of the Pokemon that receives the attack: "
tryAgain = "\nInvalid input, please try again:"

while True:
    attack = input(message1).lower()
    if attack not in lookup:
        print(tryAgain)
    else:
        break

indexAttack = lookup[attack]

while True:
    target = input(message2).lower()
    if target not in lookup:
        print(tryAgain)
    else:
        break

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
    print(
        attack.capitalize()
        + " attacks "
        + target.capitalize()
        + ", it does regular damage."
    )
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
