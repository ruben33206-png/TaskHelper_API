def add_xp_and_update_level(user, xp_amount):
    user.currentxp += xp_amount

    while user.currentxp >= 100:
        user.currentxp -= 100
        user.currentlvl += 1

def remove_xp_and_update_level(user, xp_amount):
    user.currentxp -= xp_amount

    while user.currentxp < 0 and user.currentlvl > 1:
        user.currentlvl -= 1
        user.currentxp += 100

    if user.currentxp < 0:
        user.currentxp = 0