def genTest():
    yield 1
    yield 2
    yield 3
def genFib():
    Fib_1=1 #Fib(n-1)
    Fib_2=0 #Fib(n-2)

    while True:
        #Fib_n=Fib(n-1)+Fib(n-2)
        next=Fib_1 +Fib_2
        yield next
        Fib_1=next
        Fib_2=Fib_1
def allCombo(items):
    n=len(items)
    for i in range (3**n):
        bag_1=[]
        bag_2=[]
        for j in range (n):
            if (i//(3**j))%3 ==0:
                bag_1.append(items[j])
            elif (i//(3**j))%3==1:
                bag_2.append(items[j])
        yield bag_1,bag_2
            
