import random
from .import drinks

random_val = ["1", "2"]


def getDrink(val1, val2, val3):
    if (val1 == "1"):
        drink = random.choice(random.choice(drinks.hot_drink))
        if (val2 == '1'):
            drink = random.choice(random.choice(drinks.hot_caf))
        elif (val2 == '2'):
            drink = random.choice(random.choice(drinks.hot_decaf))
        if (val3 == "1"):
            syrup = random.choice(drinks.hot_syrup)
            return drink + " with " + syrup + " Syrup"
    elif (val1 == "2"):
        drink = random.choice(random.choice(drinks.iced_drink))
        if (val2 == "1"):
            drink = random.choice(random.choice(drinks.iced_caf))
        elif (val2 == "2"):
            drink = random.choice(random.choice(drinks.iced_decaf))
            return drink
        if (val3 == "1"):
            syrup = random.choice(drinks.iced_syrup)
            return drink + " with " + syrup
    else:
        val1 = random.choice(random_val)
        val2 = random.choice(random_val)
        val3 = random.choice(random_val)
        drink = getDrink(val1, val2, val3)

    return drink
