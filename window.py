from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar

#basic settings
window=Tk()
window.title("Sudoku Solver By Saksham")
window.configure(background='white')
window.geometry('1000x480')
window.resizable(width=False,height=False)


grid=[]
for i in range(9):
	grid.append([0,0,0,0,0,0,0,0,0])


#UI Setting
#Name box

namelb=Label(window,text='Enter your name',width=14,bg='black',fg='white')
namelb.grid(column=0,row=0,padx=20,pady=20)
name=StringVar()
name_en=Entry(window,textvariable=name,width=20)
name_en.grid(column=1,row=0,pady=20,padx=20)
name_en.delete(0,'end')


grid[0][0]=DoubleVar()
cell00_get= Entry(window,textvariable=grid[0][0],width=2)
cell00_get.grid(column=2,row=1,pady=20,padx=20)
cell00_get.delete(0,'end')

grid[0][1]=DoubleVar()
cell01_get= Entry(window,textvariable=grid[0][1],width=2)
cell01_get.grid(column=3,row=1,pady=20,padx=20)
cell01_get.delete(0,'end')





grid[0][2]=DoubleVar()
cell02_get= Entry(window,textvariable=grid[0][2],width=2)
cell02_get.grid(column=4,row=1,pady=20,padx=20)
cell02_get.delete(0,'end')


grid[0][3]=DoubleVar()
cell_03= Entry(window,textvariable=grid[0][3],width=2)
cell_03.grid(column=5,row=1,pady=20,padx=20)
cell_03.delete(0,'end')





grid[0][4]=DoubleVar()
cell_04= Entry(window,textvariable=grid[0][4],width=2)
cell_04.grid(column=6,row=1,pady=20,padx=20)
cell_04.delete(0,'end')





grid[0][5]=DoubleVar()
cell_05= Entry(window,textvariable=grid[0][5],width=2)
cell_05.grid(column=7,row=1,pady=20,padx=20)
cell_05.delete(0,'end')





grid[0][6]=DoubleVar()
cell_06= Entry(window,textvariable=grid[0][6],width=2)
cell_06.grid(column=8,row=1,pady=20,padx=20)
cell_06.delete(0,'end')





grid[0][7]=DoubleVar()
cell_07= Entry(window,textvariable=grid[0][7],width=2)
cell_07.grid(column=9,row=1,pady=20,padx=20)
cell_07.delete(0,'end')





grid[0][8]=DoubleVar()
cell_08= Entry(window,textvariable=grid[0][8],width=2)
cell_08.grid(column=10,row=1,pady=20,padx=20)
cell_08.delete(0,'end')



grid[1][0]=DoubleVar()
cell_10= Entry(window,textvariable=grid[1][0],width=2)
cell_10.grid(column=2,row=2,pady=20,padx=20)
cell_10.delete(0,'end')





grid[1][1]=DoubleVar()
cell_11= Entry(window,textvariable=grid[1][1],width=2)
cell_11.grid(column=3,row=2,pady=20,padx=20)
cell_11.delete(0,'end')





grid[1][2]=DoubleVar()
cell_12= Entry(window,textvariable=grid[1][2],width=2)
cell_12.grid(column=4,row=2,pady=20,padx=20)
cell_12.delete(0,'end')





grid[1][3]=DoubleVar()
cell_13= Entry(window,textvariable=grid[1][3],width=2)
cell_13.grid(column=5,row=2,pady=20,padx=20)
cell_13.delete(0,'end')





grid[1][4]=DoubleVar()
cell_14= Entry(window,textvariable=grid[1][4],width=2)
cell_14.grid(column=6,row=2,pady=20,padx=20)
cell_14.delete(0,'end')





grid[1][5]=DoubleVar()
cell_15= Entry(window,textvariable=grid[1][5],width=2)
cell_15.grid(column=7,row=2,pady=20,padx=20)
cell_15.delete(0,'end')





grid[1][6]=DoubleVar()
cell_16= Entry(window,textvariable=grid[1][6],width=2)
cell_16.grid(column=8,row=2,pady=20,padx=20)
cell_16.delete(0,'end')





grid[1][7]=DoubleVar()
cell_17= Entry(window,textvariable=grid[1][7],width=2)
cell_17.grid(column=9,row=2,pady=20,padx=20)
cell_17.delete(0,'end')





grid[1][8]=DoubleVar()
cell_18= Entry(window,textvariable=grid[1][8],width=2)
cell_18.grid(column=10,row=2,pady=20,padx=20)
cell_18.delete(0,'end')










# def pri():
# 	for i in range(3):
# 		print(int(grid[0][i].get())+1)



# clr=Button(window,text='RESTART',bg='red',fg='white',width=14,command=pri)
# clr.grid(column=3,row=2,padx=20,pady=20)






window.mainloop()