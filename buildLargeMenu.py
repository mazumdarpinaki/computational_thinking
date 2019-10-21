
import random
names=['wine','beer','pizza','burger','fries','cola','apple','donut','cake']
values=[85,90,95,100,90,79,50,10,60]
calories=[123,154,258,354,365,150,95,195,200]

class food(object):
    def __init__(self,name,value,calories):
        self.name=name
        self.value=value
        self.calories=calories

    def getValue(self):
        return self.value
    def getCalorie(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCalorie()
    def __str__(self):
        return self.name +':<' +str(self.value) +','+str(self.calories)+'>'

def buildLargeMenu(numItems,maxVal,maxCost):
     """
    list of(str,integer,integer) ->list
    length of lists are same
    returns list of foods
    """
     
     items=[]
     for i in range (numItems):
         items.append(food(str(i),random.randint(1,maxVal),random.randint(1,maxCost)))
     return (items)

def maxVal(toConsider,Avail):
    if toConsider==[] or Avail ==0:
        result=(0,())
    elif toConsider[0].getCalorie()>Avail:
        result = maxVal(toConsider[1:],Avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=maxVal(toConsider[1:],Avail-nextItem.getCalorie())
        withVal +=nextItem.getValue()
        withoutVal,withoutToTake=maxVal(toConsider[1:],Avail-nextItem.getCalorie())

        if withVal >withoutVal:
            result = (withVal,withToTake +(nextItem,))
        else:
            result =(withoutVal,withoutToTake)
    return result
def testMaxVal(foods,maxUnits,printItems=True):
    print('Use search tree to allocate',maxUnits,'calories')
    val,taken=maxVal(foods,maxUnits)
    print('Total value of items taken',val)
    if printItems:
        for item in taken:
            print(' ',item)

for numItems in [5,10,15,20,25,30,35,40,45]:
    items=buildLargeMenu(numItems,90,250)
    testMaxVal(items,750,False)
