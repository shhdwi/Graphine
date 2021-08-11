import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt



def graphs():                                                                  
#Function for graph app
    rootgr=tk.Tk()                                                       
#Top level is used to create a new window  
    x=0                                                                        
#variable for x axis                                                           
    rootgr.title('Graphine: A Python Graph Plotting Algorithm')                                                     
#Title of window             
    def functions():                                                           
#Function to equate the function   
        global x 
        x=np.linspace(int(ra1.get()),int(ra2.get()),10000)                  
#breaks the range into 10000 equal parts 
        eq1= Xentry.get()                                                      
#takes the equation 
        try:                                                                   
#tries and then replaces wherever needed to make the program user friendly
           string1=eq1.replace('cos','np.cos')                                 
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('sin','np.sin')                             
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('^','**')                                   
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('log','np.log10')                           
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('ln','np.log')                              
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('tan','np.tan')                             
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('floor','np.floor')                         
#replaces the code with a numpy part to execute as per the user wants 
           string1=string1.replace('ceil','np.ceil')                           
#replaces the code with a numpy part to execute as per the user wants
           string1=string1.replace('x','(x)')                                  
#replaces the code with a numpy part to execute as per the user wants
           y=eval(string1) 
           plt.plot(x,y) 
           plt.xlim(int(ra1.get()),int(ra2.get())) 
           plt.savefig(r'graph.png')                                           
#save the graph
           plt.show() 
                                                       
# #Top level is used to create a new window 
#            root2gr.title('graph')                                              
# #Title of window 
#            photo8=tk.PhotoImage(file=r'graph.png')                             
# #Photo imported for using as graph                 
#            ph=tk.Label(root2gr,image=photo8)                                  
#  #Label to show the graph 
#            ph.grid(row=2,column=5)                                             
# #grid used for arranging graph
#            root2gr.mainloop()                                                  
# #To execute the window in mainloop
        except :                                                 
#checking for errors
            c1=eq1.count('(') 
            c2=eq1.count(')') 
            if c1 != c2: 
                    tkinter.messagebox.showerror('ERROR!', 'close the brackets! or try using "*" sign')
#Error message
            if 'sin' or'cos' or 'tan' or'log'or 'ln'or 'floor'or'ceil'or'^'in eq1 and '(' not in eq1: 
                tkinter.messagebox.showerror('ERROR!', 'Use brackets \nFor example:\nsin(x+1)\n'+'Or\n'+'Use "*" while Multiplying' )
#Error message 
            elif '*'not in eq1: 
                    tkinter.messagebox.showerror('ERROR!', 'Use "*" while Multiplying' )
#Error message 
            else: 
                    tkinter.messagebox.showerror('ERROR!', 'Enter a valid input' )
#Error message 
    tk.Label(rootgr,text="Enter the equation: ").grid(row=0,column=0)          
#Label for showing where to type the equation 
    Xentry=tk.Entry(rootgr,width=35,borderwidth=5)                             
#Entry to give a box to enter equation 
    Xentry.grid(row=1,column=0,columnspan=3,padx=10,pady=10)                   
#grid used for arranging items on the graph screen 
    tk.Label(rootgr,text="Enter Starting Limit: ").grid(row=2,column=0)        
#Label for showing where to type starting limit
    ra1=tk.Entry(rootgr)                                                       
#Entry to give a box to enter starting limit
    ra1.grid(row=2,column=1)                                                   
#grid used for arranging items on the calculator screen 
    tk.Label(rootgr,text="Enter Ending Limit: ").grid(row=3,column=0)          
#Label for showing where to type ending limit 
    ra2=tk.Entry(rootgr)                                                       
#Entry to give a box to enter ending limit   
    ra2.grid(row=3,column=1)                                                   
#grid used for arranging items on the calculator screen 
    tk.Button(rootgr,text='plot',command=functions).grid(row=4,column=1)       
#Button for plotting
    rootgr.mainloop()                                                          
#To execute the window in mainloop 

graphs()