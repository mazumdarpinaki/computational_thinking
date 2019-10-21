import tkinter.filedialog
from_filename=tkinter.filedialog.askopenfilename()
to_filename=tkinter.filedialog.asksaveasfilename()

from_file=open(from_filename,'r')
contents=from_file.read()
from_file.close()

to_file=open(to_filename,'w')
to_file.write('copy\n')
to_file.write(contents)
to_file.close()







