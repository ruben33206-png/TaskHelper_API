def add_xp_and_update_level(user, xp_amount):
    user.currentxp += xp_amount

    while user.currentxp >= 100:
        user.currentxp -= 100
        user.currentlvl += 1
