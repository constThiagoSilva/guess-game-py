from random import randint

def get_random_number(minimal_range: int ,maximum_range: int):
    if minimal_range < 0:
        raise 'mininum range cannot be negative'
    if maximum_range < 0:
        raise 'maximum range cannot be negative'
    if minimal_range > maximum_range:
        raise 'minimum range cannot be greater than maximum'

    return randint(minimal_range, maximum_range)