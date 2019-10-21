#import read
class food(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=v
        self.calories=w

    def getValue(self):
        return self.value
    def getCalorie(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCalorie()
    def __str__(self):
        return self.name +':<' +str(self.value) +','+str(self.calories)+'>'

import tkinter.filedialog
food_file=tkinter.filedialog.askopenfilename()
foods=open(food_file,'r')
line=foods.readline()
foodAll=''
while line !='':
    foodAll+=line
    line=foods.readline()
print(foodAll)
foods.close()

def buildMenu(names,values,calories):
     """
    list of(str,integer,integer) ->list
    length of lists are same
    returns list of foods
    """
     
     menu=[]
     for i in range (len(values)):
         menu.append((names[i],values[i],calories[i]))
         i=i+1
     return menu
         
