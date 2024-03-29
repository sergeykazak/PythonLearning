def check_alive(health: int) -> bool:
    """ Return `true` if the player's health is greater than 0 or `false` if it is 0 or below. """
    return health > 0


def check_alive(health):
    if health is None:
        return False
    elif isinstance(health, (int, float)) and 0 < health < 10:
        return True
    else:
        return False