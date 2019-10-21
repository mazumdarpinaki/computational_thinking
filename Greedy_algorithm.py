class Food(object):
    def __init__(self,name,value,calorie):
        self.name=name
        self.value=value
        self.calorie=calorie
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calorie
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name +': <'+str(self.value)+','+str(self.calorie)+'>'

def buildMenu(names,values,calories):
        menu=[]
        for  i in range (len(values)):
            menu.append(Food(names[i],values[i],calories[i]))
        return menu
def greedy(foods,maxCost,keyFunction):
    foodscopy=sorted(foods,key=keyFunction,reverse=True)
    
    result =[]
    totalCost,totalValue=0.0,0.0
    for i in range (len(foodscopy)):
        if totalCost+foodscopy[i].getCost()<=maxCost:
            result.append(foodscopy[i])
            totalCost+=foodscopy[i].getCost()
            totalValue+=foodscopy[i].getValue()
    return (result,totalValue)
def testgreedy(foods,constraints,keyFunction):
    taken,value=greedy(foods,constraints,keyFunction)
    print('Total value of foods taken=',value)
    for foods in taken:
        print ('  ',foods)
def testgreedys(foods,maxUnits):
    print('use greedy by value to allocate',maxUnits,'calorie')
    testgreedy(foods,maxUnits,Food.getValue)
    print('\n use greedy by cost to allocate',maxUnits,'calorie')        
    testgreedy(foods,maxUnits,lambda x:1/Food.getCost(x))
    print('use greedy by density to allocate',maxUnits,'calorie')
    testgreedy(foods,maxUnits,Food.density)
def maxVal(toConsider,Avail):
    if toConsider==[] or Avail ==0:
        result=(0,())
    elif toConsider[0].getCost() > Avail:
        result = maxVal(toConsider[1:],Avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=maxVal(toConsider[1:],Avail-nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal,withoutToTake = maxVal(toConsider[1:],Avail)

        if withVal >withoutVal:
            result = (withVal,withToTake +(nextItem,))
        else:
            result =(withoutVal,withoutToTake)
    return result
def testmaxVal(foods,maxUnits,printItems=True):
    print('use search tree to allocate',maxUnits,'calorie')
    value,taken= maxVal(foods,maxUnits)
    print('Total value of foods taken=',value)
    if printItems:
        for item in taken:
            print ('  ',item)

names=['wine','beer','pizza','burger','fries','cola','apple','donut','cake']
values=[89,90,95,100,90,79,50,10]
calories=[123,154,258,354,365,150,95,195]
foods=buildMenu(names,values,calories)
testgreedys(foods,750)
testmaxVal(foods,750)


