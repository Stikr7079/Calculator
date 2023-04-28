#creating calculator windows based application

#for windows bases application we import tkinter module
import tkinter
def main():
    app=tkinter.Tk()
    app.title("calculator")
    app.geometry("220x220")
    l1=tkinter.Entry(app,width=21,font=15)
    l1.place(x=20, y=10)
    input1="" 
    input2=0

    #here we creating inner function which are called whenever number button along with operation button are clicked
    def calculator(x):

        '''
        here if non-operational buttons are clicked the this condition will worked and aganin call calculator function with argument x
        to insert the number or operational buttons 
        '''
        
        if x not in "+-=/X":
            l1.insert(tkinter.END,x)

        
        #this condition will run when any operational button are clicked by user 
        #then input1 variable store the first number and again call l1 variable to insert second data
            
        elif x in "+-/X":
            global input1,input2
            input1=x
            input2=int(l1.get())
            l1.delete(0,tkinter.END)
            l1.insert(tkinter.END,"")
        
        #this condition will run whe is equal to button clicked then operation is done between variable which stored 
        #in input2 and a new variable input3 and result is displayed in dial box. 
        
        
        elif x=="=":
            input3=int(l1.get())
            if input1=="+":
                result=input2+input3
                
            elif input1=="-":
                result=input2-input3
                
            elif input1=="/":
                result=input2/input3
                
            elif input1=="X":
                result=input2*input3
                
            l1.delete(0,tkinter.END)
            l1.insert(0,str(result))
    '''
    Here we are creating number button which are calling the inner function calculator and 
    after creating button we are placing in order
    '''   
    b1=tkinter.Button(app,text="7",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("7"))
    b2=tkinter.Button(app,text="8",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("8"))
    b3=tkinter.Button(app,text="9",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("9"))
    b4=tkinter.Button(app,text="+",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("+"))
    b1.place(x=20, y=35)
    b2.place(x=70, y=35)
    b3.place(x=120, y=35)
    b4.place(x=170, y=35)
    
    b5=tkinter.Button(app,text="4",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("4"))
    b6=tkinter.Button(app,text="5",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("5"))
    b7=tkinter.Button(app,text="6",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("6"))
    b8=tkinter.Button(app,text="-",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("-"))
    b5.place(x=20, y=80)
    b6.place(x=70, y=80)
    b7.place(x=120, y=80)
    b8.place(x=170, y=80)
    
    b9 =tkinter.Button(app,text="1",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("1"))
    b10=tkinter.Button(app,text="2",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("2"))
    b11=tkinter.Button(app,text="3",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("3"))
    b12=tkinter.Button(app,text="=",font=("Arial",15),width=3,height=3,bg="White",command=lambda:calculator("="))
    b9.place(x=20, y=125)
    b10.place(x=70, y=125)
    b11.place(x=120, y=125)
    b12.place(x=170, y=125)
    
    b13=tkinter.Button(app,text="/",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("/"))
    b14=tkinter.Button(app,text="0",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("0"))
    b15=tkinter.Button(app,text="X",font=("Arial",15),width=3,height=1,bg="White",command=lambda:calculator("X"))
    b13.place(x=20, y=170)
    b14.place(x=70, y=170)
    b15.place(x=120, y=170)
main()
