import random
import discord


# Rolls nDn
def basicRoll(number, sides):
    rTotal = 0
    i = 0
    while i < number:
        rTotal += random.randint(1, sides)
        i += 1
    return rTotal


# For when/if I implement another checking system that needs the EP handling system
async def cSwitch(ctx, target, roll):
    ones = int(str(roll)[1])  # These allow for crit checking
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
async def manCheck(ctx, target, mod):
    target += mod

    roll = basicRoll(1, 99)
    await cSwitch(ctx, target, roll)  # Passes everything onto cSwitch


# Checks if a value fed to it is a die or modifier
def dieOrInt(unsure):
    unsure = unsure.casefold()
    if 'd' in unsure:
        unsure = unsure.split('d')
        total = basicRoll(int(unsure[0]), int(unsure[1]))
        return total
    else:
        total = int(unsure)
        return total


# A proper nDn roller
async def ndnRoll(ctx, dice):
    inputStr = dice
    total = 0
    dice = dice.split('+')  # Breaks input along additions

    for item in dice:  # Checks each set of dice
        if '-' in item:  # Are any negative in the set?
            if item[0] == '-':  # If the first is, subtract them all from the total
                item = item.split('-')
                for value in item:
                    total -= dieOrInt(value)
            else:  # If the first value is not negative, add first value and subtract rest
                item = item.split('-')
                total += dieOrInt(item[0])  # Adds first value
                item.pop(0)  # Deletes it
                for value in item:
                    total -= dieOrInt(value)
            # The above works the way it does since if the split is along the + symbol
            # Then that means any dice/mods that are positive will be separated.
            # Therefore, only the first die/mod in a set can be a positive one.
            # All others that follow are negative
        else:
            total += dieOrInt(item)
    await ctx.respond('You rolled: ' + inputStr + '/n' + 'Result: ' + total)
