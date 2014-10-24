address_book = {
		'Swaroop'   : 'swaroop@byteofpython.info',
		'Larry'     : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
		'Ted'       : 'buffalobillion@gmail.com'
		}

print "Swaroop's address is %s" % address_book['Swaroop']

# Adding a key/value pair
address_book['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del address_book['Ted']

print '\nThere are %d contacts in the address book\n' % len(address_book)

for name, address in address_book.items():
	print 'Contact %s at %s' % (name, address)

if 'Guido' in address_book:
	print "\nGuido's address is %s" % address_book['Guido']
