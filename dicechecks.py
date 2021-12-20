import random
import discord


# Rolls nDn
# TODO: Is this basic dice command even necessary?
def dice(number, sides):
    rTotal = 0
    i = 0
    while i < number:
        rTotal += random.randint(1, sides)
        i += 1
    return rTotal


# For when/if I implement another checking system
async def cSwitch(ctx, target, roll):
    ones = int(str(roll)[1]) # These allow for crit checking
    tens = int(str(roll)[0])
    result = ('**Target:** ' + str(target) + ' **Roll:** ' + str(roll) + ',')  # Displays target vs roll

    if roll > target:
        state = False
    else:
        state = True

    if roll == 0:  # Guaranteed crits
        await ctx.respond(result + ' critical success!')
    elif roll == 99:
        await ctx.respond(result + ' critical failure!')
    elif ones == tens:  # Crits
        if state:
            await ctx.respond(result + ' critical success!')
        else:
            await ctx.respond(result + ' critical failure!')
    elif roll > 66:  # Double superior
        if state:
            await ctx.respond(result + ' 2 superior successes!')
        else:
            await ctx.respond(result + ' 2 superior failures!')
    elif roll > 33:  # Single superior
        if state:
            await ctx.respond(result + ' superior success!')
        else:
            await ctx.respond(result + ' superior failure!')
    else:
        if state:
            await ctx.respond(result + ' roll passed!')
        else:
            await ctx.respond(result + ' roll failed!')


# Check with manual input and modifier
async def mcheck(ctx, target, mod):
    target += mod

    roll = random.randint(0, 99)
    await cSwitch(ctx, target, roll)  # Passes everything onto cSwitch

