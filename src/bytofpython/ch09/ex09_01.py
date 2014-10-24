# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

def print_list(list):
    for item in list:
        print item,

print 'I have', len(shoplist), 'items to purchase.'

print 'These items are:', # Notice the comma at the end of the line
print_list(shoplist)

print '\nI also have to buy rice.'
shoplist.append('rice')

print 'My shopping list is now',
print_list(shoplist)

print 'I will sort my list now'
shoplist.sort()

print 'Sorted shopping list is',
print_list(shoplist)

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now',
print_list(shoplist)