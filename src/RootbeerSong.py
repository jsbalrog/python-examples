word = "bottles"
for number in reversed(range(1, 100)):

    print '%d %s of rootbeer on the wall.' % (number, word)
    print '%d %s of rootbeer.' % (number, word)
    print 'Take one down, pass it around.'
    if number-1 > 0:
        if number-1 == 1:
            word = "bottle"
        print '%d %s of rootbeer on the wall.' % (number-1, word)
    else:
        print 'No more bottles of rootbeer on the wall.'
