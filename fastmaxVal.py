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


def testmaxVal(foods,maxUnits,algorithm):
    
    print ('Use search tree for allocation of',maxUnits,'calories')
            
    value,taken=maxVal(foods,maxUnits)
    print ('Total value of items taken',value)
    for items in taken:
        print(' ',items)

def buildMenu(names,values,calories):
     """
    list of(str,integer,integer) ->list
    length of lists are same
    returns list of foods
    """
     
     menu=[]
     for i in range (len(values)):
         menu.append(food(names[i],values[i],calories[i]))
         i=i+1
     return menu
def buildLargeMenu(numItems,Maxval,Maxcal):
    LargeMenu=[]
    for i in range(numItems):
        LargeMenu.append(food(str(i),random.randint(1,Maxval),random.randint(1,Maxcal)))
    return LargeMenu
for numItems in [5,10,15,20,25,30,35,40,45]:
    foods=buildLargeMenu(numItems,90,200)
    
def fastmaxVal(toConsider,Avail,memo={}):
    try:
        if memo[len(toConsider),Avail] in memo:
              result=memo[len(toConsider),Avail]
        
    except KeyError:
            if toConsider==[] or Avail==0:
                result= (0,())
            elif toConsider[0].getCalorie()> Avail:
                result=maxVal(toConsider[1:],Avail)
            else:
                nextItem=toConsider[0]
                withVal,withtoTake=maxVal(toConsider[1:],Avail-nextItem.getCalorie())
                withVal +=nextItem.getValue()
                withoutVal,withouttoTake=maxVal(toConsider[1:],Avail)
            if withVal > withoutVal:
                result=(withVal,withtoTake+(nextItem,))
            else:
                result=(withoutVal,withouttoTake)
    memo[len(toConsider),Avail]=result
    return result

        
testmaxVal(foods,750,fastmaxVal,print='fastmaxVal')
            
