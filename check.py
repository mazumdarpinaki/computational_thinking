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

def buildMenu(names,values,calories):
     """
    list of(str,integer,integer) ->list
    length of lists are same
    returns list of foods
    """
     
     menu=[]
     for i in range (len(values)):
         menu.append(food(names[i],values[i],calories[i]))
     return menu
     
menu=buildMenu(names,values,calories)    
foods=[]
for food in menu:
    foods.append(str(food))
print (foods)
