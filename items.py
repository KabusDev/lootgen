import random, procedural

print("items init")
class Item:
    def __init__(self, item_name, min_dmg, max_dmg, str_bonus, int_bonus):
        self.item_name = item_name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.str_bonus = str_bonus
        self.int_bonus = int_bonus

 # remember that ints need to have one higher number to get the lower needed number, eg 0,2 should be 0,3

SwordClass = Item(
    item_name="Sword",
    min_dmg=(),
    max_dmg=(),
    str_bonus=(),
    int_bonus=()
)

StaffClass = Item(
    item_name="Staff",
    min_dmg=(),
    max_dmg=(),
    str_bonus=(),
    int_bonus=()
)

def NumGen():
    SwordClass.min_dmg = random.randint(2, 5)
    SwordClass.max_dmg = random.randint(8, 11)
    SwordClass.str_bonus = random.randint(2, 7)
    SwordClass.int_bonus = random.randint(0, 3)

    StaffClass.min_dmg = SwordClass.min_dmg # sane base stat
    StaffClass.max_dmg = random.randint(8, 11)
    StaffClass.str_bonus = SwordClass.int_bonus
    StaffClass.int_bonus = SwordClass.str_bonus # same as before

# try to migrate all random gen stuff to the procedural file in a while loop, make a number gen file?

# wierd issues when attempting to get variables from seperate files into a class, this will suffice

class Rarity:
    def __init__(self, name, prefix, suffix, rarity):
        self.name = name
        self.prefix = prefix
        self.suffix = suffix  # booleans to identify if it will have a certain modifier
        self.rarity = rarity  # use decimal of 0 and 1 to determine percentage of chance.

Common = Rarity(
    name = "Common",
    prefix=False,
    suffix=False,
    rarity=0.8 # not used but pycharm whines if variables in classes aren't used
)

Uncommon = Rarity(
    name="Uncommon",
    prefix=True,
    suffix=False,
    rarity=0.2 # factoring the rare chance, this is %15
)

Rare = Rarity(
    name="Rare",
    prefix=True,
    suffix=True,
    rarity=0.05
)

class ItemModifiers:
    def __init__(self, type_fix):
        self.type_fix = type_fix
# Define prefix and suffix in procedural file or here?
# How can I define it here without stray variables?

# do modifiers in procedural file to get random generations all in one file, inefficient but easier to work on

Warrior = ItemModifiers(
    type_fix="Warrior's",
)

Sage = ItemModifiers(
    type_fix="Sage's",
)

Assassin = ItemModifiers(
    type_fix="Assassin's",
)

Jack = ItemModifiers(
    type_fix="Jack's",)

Bear = ItemModifiers(
    type_fix="Of the Bear",)

Fox = ItemModifiers(
    type_fix="Of the Fox",)

Chance = ItemModifiers(
    type_fix="Of Chance",)


print("items loaded")
