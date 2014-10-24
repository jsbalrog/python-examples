class Person:
    '''Represents a person.'''
    population = 0 #This is a class variable
    
    def __init__(self,name):
        self.name = name #This is an object variable
        print '(Initializing %s)' % self.name
        
        #When this person is created, the
        #population increases by one
        Person.population += 1
        
    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name
        
        Person.population -= 1
        
        if Person.population == 0:
            print 'No more people left'
        else:
            print 'There are still %d people left.' % Person.population
            
    def say_hi(self):
        '''Greeting by the person. Really, that's all it does. '''
        print 'Hi, my name is %s.' % self.name
        
    def how_many(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population
            
ted = Person('Ted')
ted.say_hi()
ted.how_many()
   
joe = Person('Joe')
joe.say_hi()
joe.how_many()
    
ted.say_hi()
ted.how_many()
    