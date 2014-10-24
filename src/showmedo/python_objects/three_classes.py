class NewClass:
    def show(self):
    #def show():
        print 'This is NewClass'
        

#Subclass of NewClass
class AnotherNewClass(NewClass):
    #pass
    def show(self):
        #print 'This is AnotherNewClass'
        super.show(self)

#Subclass of AnotherNewClass
class YetAnotherNewClass(AnotherNewClass):
    pass