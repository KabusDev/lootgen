import procedural, items
user_input = 0

while True:
    try:
        user_input = int(input("\nEnter 1 to run the loot generator, 2 to show instructions, 3 to exit the program."))
    except ValueError:
        print("That is not a valid input")
        user_input = 0
        continue
    else:
        if user_input == 4:
            if procedural.debug is False:
                print("Debug Mode Enabled.")
                procedural.debug = True
            else:
                print("Debug Mode Disabled.")
                procedural.debug = False

        if user_input == 3:
            print("Exiting")
            exit()

        if user_input == 2:
            print("""
            To generate an item, enter 1
            To get this help screen, enter 2
            To exit the program, enter 3
            To show debug prints, enter 4

            This program will procedurally generate 2 base items which have different statistics everytime it
            is generated, there are rarities which affect the name and the modifieres applied to the item.

            Common chances for items are 80%
            Uncommon chances for items are 15%
            Rare chances for items are 5%

            There are certain prefixes and suffixes for items which affect the modifiers on said item.

            Prefixes:

            Warrior’s: Multiply Strength by 1.5 – 2.5, or give 1-4 Strength if currently 0.
            Sage’s: Multiply Intelligence by 1.5 – 2.5, or give 1-4 Intelligence if currently 0.
            Assassin’s: Add 1-3 to both Minimum and Maximum damage.
            Jack’s: Multiply all stats by 1.5.

            Suffixes:
            Of the Bear: Double Strength.
            Of the Fox: Double Intelligence.
            Of Chance: Half Minimum Damage, Double Maximum Damage.

            Prefixes only occure on Uncommon and Rare items, Both fixes apply to Rare items
            No fixes apply to the Common items.""")
            # stupidly long help screen but that's what the specification wants

        if user_input != 1:
            if user_input == 2: # wont print invalid number if its the help screen number
                user_input = 0
                continue
            if user_input == 4: # there is probably a nicer way of doing this but this is only for a debug feature
                user_input = 0
                continue
            else:
                print("Invalid number")
                user_input = 0
                continue

    finally:
        if user_input == 1:
           print("Generating Item")
           items.NumGen()
           procedural.LootBuild()