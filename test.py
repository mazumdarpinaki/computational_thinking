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
