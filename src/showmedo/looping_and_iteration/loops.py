# Loop over values in a list, use else, break, continue
l = ['a', 'b', 'c']
for i in l:
    #if i == 'b':
    #    # Jump out early, skip the else clause as well as the rest of the loop
    #    break
    if i == 'a':
        # Continue with the loop, don't execute the following code but continue with the loop
        continue
    print i
else:
    print "Done!"
