from time import sleep
dice_sum = 0

spell_lv = int(input("Enter Spell level: "))

missiles = spell_lv + 2 # first level of magic missile have 3 missiles (2 additional)

for i in range(missiles):
    dice = int(input("Enter dice rolled: "))
    dice_sum += dice

total_damage = dice_sum + missiles


if dice_sum > missiles * 2:
    print("Damage above average!")

elif dice_sum == missiles * 2:
    print("Damage is average!")

else:
    print("Damage below average!")































print("Total damage is: {}".format(total_damage))
sleep(5)