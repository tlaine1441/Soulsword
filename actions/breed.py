
def bread(male, female):
    male_gen = male.get_gen()
    female_gen = female.get_gen()
    new_gen = None
    
    if male_gen != female_gen:
        if male_gen > female_gen:
            new_gen = male_gen + 1
        else:
            new_gen = female_gen + 1
    else:
        new_gen = male_gen + 1

    return {
        'new_gen': new_gen
    }