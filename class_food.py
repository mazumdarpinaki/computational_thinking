
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
