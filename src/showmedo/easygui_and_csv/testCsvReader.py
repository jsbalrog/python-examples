import csvReader

def testIsJustNumbersOnNumbers():
    listOfStrings = ['22.4', '23.9']
    assert csvReader.isJustNumbers(listOfStrings)
    
def testIsJustNumbersOnBadNumbers():
    listOfStrings = ['abc', '23.9']
    assert csvReader.isJustNumbers(listOfStrings) == False
    
def testGetNumbers():
    listOfStrings = ['22.4', '23.9']
    assert csvReader.getNumbers(listOfStrings) == [22.4, 23.9]
    
def testAverage():
    listOfNumbers = [1,2.3]
    assert csvReader.average(listOfNumbers) == 2.0