import random, items, decimal
print("procedural init")

debug = False

item_name_var = None
item_type = None
item_stat_bonus = None
item_rarity = None

item_str = None
item_int = None
item_dmg_min = None
item_dmg_max = None
item_modifier_prefix = None
item_modifier_suffix = None

def RarityGen():
    global raritychance
    raritygen = random.uniform(0, 1)
    decimal.Decimal(raritygen)
    raritychance = round(raritygen, 2)

    global item_rarity
    if raritychance <= items.Rare.rarity:
        item_rarity = items.Rare
    if raritychance >= items.Rare.rarity:
        item_rarity = items.Uncommon
    if raritychance >= items.Uncommon.rarity:
        item_rarity = items.Common
    return
    # checking for the common's rarity value is redundant

def LootGen():
    global item_type
    while True:
        gen = random.randrange(1, 3)
        if gen == 1:
            # item_name = items.SwordClass.item_name
            # item_stat_dmg = (items.SwordClass.min_dmg, "-", items.SwordClass.max_dmg)
            # item_stat_bonus = ("Str Bonus:", items.SwordClass.str_bonus, "Int Bonus:", items.SwordClass.int_bonus)
            item_type = items.SwordClass
            break
        if gen == 2:
            # item_name = items.StaffClass.item_name
            # item_stat_dmg = (items.StaffClass.min_dmg, "-", items.StaffClass.max_dmg)
            # item_stat_bonus = ("Str Bonus:", items.SwordClass.str_bonus, "Int Bonus:", items.SwordClass.int_bonus)
            item_type = items.StaffClass
            break
        else:  # redundancy
            print("uh")
            break

def PrefixGen():
    global item_modifier_prefix, item_name_var
    while True:
        prefixgen = random.randrange(1, 5)
        if prefixgen == 1:
            item_modifier_prefix = items.Warrior
            break
        if prefixgen == 2:
            item_modifier_prefix = items.Sage
            break
        if prefixgen == 3:
            item_modifier_prefix = items.Assassin
            break
        if prefixgen == 4:
            item_modifier_prefix = items.Jack
            break
    item_name_var = item_modifier_prefix.type_fix, item_type.item_name

def BothGen():
    global item_modifier_prefix, item_modifier_suffix, item_name_var
    while True: # could be removed as gens are called into main loop but may cause weird issues, wont bother
        prefixgen = random.randrange(1, 5)
        if prefixgen == 1:
            item_modifier_prefix = items.Warrior
            break
        if prefixgen == 2:
            item_modifier_prefix = items.Sage
            break
        if prefixgen == 3:
            item_modifier_prefix = items.Assassin
            break
        if prefixgen == 4:
            item_modifier_prefix = items.Jack
            break

    while True:
        suffixgen = random.randrange(1,4)
        if suffixgen == 1:
            item_modifier_suffix = items.Bear
            break
        if suffixgen == 2:
            item_modifier_suffix = items.Fox
            break
        if suffixgen == 2:
            item_modifier_suffix = items.Chance
            break
        # get all modifiers and create them in this file
    item_name_var = item_modifier_prefix.type_fix, item_type.item_name, item_modifier_suffix.type_fix

def Modifier():
    global item_modifier_prefix, item_modifier_suffix, item_stat_bonus, item_str, item_int, item_dmg_min, item_dmg_max
    global prefix_bonus, suffix_bonus
    prefix_bonus = None
    suffix_bonus = None

    if item_modifier_prefix == items.Warrior: # removed while loops as this is triggered by the main base loop
        while True:
            modifiergen = random.uniform(1.5, 2.5)
            additional = random.randrange(1, 5)
            modifier = round(modifiergen, 2)
            if item_str > 0:
                item_str = round((item_str * modifier),2)
                prefix_bonus = ("x",modifier,"Strength")
                break
            else:
                item_str = additional
                prefix_bonus = ("+", additional, "Strength")
                break

    if item_modifier_prefix == items.Sage:
        while True:
            modifiergen = round((random.uniform(1.5, 2.5)),2)
            additional = random.randrange(1, 5)
            modifier = round(modifiergen, 2)
            if item_str > 0:
                item_int = round((item_int * modifier),2)
                prefix_bonus = ("x", modifier, "Intelligence")
                break
            else:
                item_int = additional
                prefix_bonus = ("+", additional, "Intelligence")
                break

    if item_modifier_prefix == items.Assassin:
        while True:
            min_additional = random.randrange(1, 3)
            max_additional = random.randrange(1, 3)
            item_dmg_min = item_dmg_min + min_additional
            item_dmg_max = item_dmg_max + max_additional
            prefix_bonus = ("+", min_additional, "to Min Dmg, +", max_additional, "to Max Dmg")
            break

    if item_modifier_prefix == items.Jack:
        item_dmg_min = item_dmg_min * 1.5
        item_dmg_max = item_dmg_max * 1.5
        item_int = item_int * 1.5
        item_str = item_str * 1.5
        prefix_bonus = ("x1.5 to all Stats","") # stops fullspace text due to * to parse text into normal string

    if item_modifier_suffix == items.Bear:
        item_str = item_str *2
        suffix_bonus = ("Double Strength.","")

    if item_modifier_suffix == items.Fox:
        item_int = item_int *2
        suffix_bonus = ("Double Intelligence.","")

    if item_modifier_suffix == items.Chance:
        item_dmg_min = item_dmg_max * 0.5
        item_dmg_max = item_dmg_max * 2
        suffix_bonus = ("Half Minimum Damage, Double Maximum Damage.","")

    # round all the modifiers to avoud recurring decimals from multiplication

    if prefix_bonus is None:

        item_stat_bonus = ("Bonus:","No Bonus")
    elif suffix_bonus is None:
        item_stat_bonus = ("Bonus:",*prefix_bonus)
    else:
        item_stat_bonus = ("Bonus:",*prefix_bonus,"and", *suffix_bonus)
    return

def LootBuild():
    global item_name_var, item_dmg_min, item_dmg_max, item_int, item_str, item_rarity, item_stat_bonus
    global item_modifier_prefix, item_modifier_suffix

    RarityGen()
    LootGen()

    item_dmg_min = item_type.min_dmg
    item_dmg_max = item_type.max_dmg
    item_int = item_type.int_bonus
    item_str = item_type.str_bonus
    item_modifier_prefix = None
    item_modifier_suffix = None


    if item_rarity == items.Rare:
        print("Rare Item")
        BothGen()
    elif item_rarity == items.Uncommon:
        PrefixGen()
        print("Uncommon Item")
    else:
        item_name_var = (item_type.item_name, "")

        # fixes issue that causes print to space the word out between characters
        print("Common Item")

    Modifier()
    
    # print the item here
    print(*item_name_var)
    print("Damage: ", item_dmg_min,"-", item_dmg_max)
    print("Stats: ", "Str:",item_str, "Int:",item_int)
    print(*item_stat_bonus)

    if debug is True:
        print("\nDebug Info:")
        print("Base DMG from Weapon:",item_type.item_name,"is:",item_type.min_dmg, "-",item_type.max_dmg)
        print("Base Str:",item_type.str_bonus, "Base Int:", item_type.int_bonus)
        print("Rarity Chance Modifier is:",raritychance)
    pass
print("procedural loaded")
