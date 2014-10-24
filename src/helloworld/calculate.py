def calculate_change(quarters, dimes, nickels, pennies):
    quarter_tot = quarters * .25
    dimes_tot = dimes * .10
    nickels_tot = nickels * .05
    pennies_tot = pennies * .01
    return quarter_tot + dimes_tot + nickels_tot + pennies_tot
    
change_tot = calculate_change(8, 2, 1, 3)
print change_tot