#Readline approach(read line by line)
food_details=open('FOODS.txt','r')
food_details.close()
#readline approach full text/part text (with while loop)
food_menu=open('FOODS.txt','r')
line=food_menu.readline()
foodAll=''
while line !='':
    foodAll=foodAll+line
    line=food_menu.readline()

print(foodAll)
food_menu.close()
# readline approach full text (with for loop)
food_menu=open('FOODS.txt','r')
foodAll=''
for line in food_menu:
    foodAll+=line
#print(foodAll)
food_menu.close()

# read approach(read whole file as a single string)
food_menu=open('FOODS.txt','r')
foodAll=food_menu.read()
#print(foodAll)
food_menu.close()

# readlines approach(read whole file as a list)
food_details=open('FOODS.txt','r')
foodAll=''
food_list=food_details.readlines()
for line in food_list:
    foodAll+=line
#print(foodAll)
food_details.close()





