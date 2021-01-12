from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar

#basic settings
window=Tk()
window.title("Sudoku Solver By Saksham")
window.configure(background='white')
window.geometry('1000x800')
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







grid[2][0]=DoubleVar()
cell_20= Entry(window,textvariable=grid[2][0],width=2)
cell_20.grid(column=2,row=3,pady=20,padx=20)
cell_20.delete(0,'end')





grid[2][1]=DoubleVar()
cell_21= Entry(window,textvariable=grid[2][1],width=2)
cell_21.grid(column=3,row=3,pady=20,padx=20)
cell_21.delete(0,'end')





grid[2][2]=DoubleVar()
cell_22= Entry(window,textvariable=grid[2][2],width=2)
cell_22.grid(column=4,row=3,pady=20,padx=20)
cell_22.delete(0,'end')





grid[2][3]=DoubleVar()
cell_23= Entry(window,textvariable=grid[2][3],width=2)
cell_23.grid(column=5,row=3,pady=20,padx=20)
cell_23.delete(0,'end')





grid[2][4]=DoubleVar()
cell_24= Entry(window,textvariable=grid[2][4],width=2)
cell_24.grid(column=6,row=3,pady=20,padx=20)
cell_24.delete(0,'end')





grid[2][5]=DoubleVar()
cell_25= Entry(window,textvariable=grid[2][5],width=2)
cell_25.grid(column=7,row=3,pady=20,padx=20)
cell_25.delete(0,'end')





grid[2][6]=DoubleVar()
cell_26= Entry(window,textvariable=grid[2][6],width=2)
cell_26.grid(column=8,row=3,pady=20,padx=20)
cell_26.delete(0,'end')





grid[2][7]=DoubleVar()
cell_27= Entry(window,textvariable=grid[2][7],width=2)
cell_27.grid(column=9,row=3,pady=20,padx=20)
cell_27.delete(0,'end')





grid[2][8]=DoubleVar()
cell_28= Entry(window,textvariable=grid[2][8],width=2)
cell_28.grid(column=10,row=3,pady=20,padx=20)
cell_28.delete(0,'end')





grid[3][0]=DoubleVar()
cell_30= Entry(window,textvariable=grid[3][0],width=2)
cell_30.grid(column=2,row=4,pady=20,padx=20)
cell_30.delete(0,'end')





grid[3][1]=DoubleVar()
cell_31= Entry(window,textvariable=grid[3][1],width=2)
cell_31.grid(column=3,row=4,pady=20,padx=20)
cell_31.delete(0,'end')





grid[3][2]=DoubleVar()
cell_32= Entry(window,textvariable=grid[3][2],width=2)
cell_32.grid(column=4,row=4,pady=20,padx=20)
cell_32.delete(0,'end')





grid[3][3]=DoubleVar()
cell_33= Entry(window,textvariable=grid[3][3],width=2)
cell_33.grid(column=5,row=4,pady=20,padx=20)
cell_33.delete(0,'end')





grid[3][4]=DoubleVar()
cell_34= Entry(window,textvariable=grid[3][4],width=2)
cell_34.grid(column=6,row=4,pady=20,padx=20)
cell_34.delete(0,'end')





grid[3][5]=DoubleVar()
cell_35= Entry(window,textvariable=grid[3][5],width=2)
cell_35.grid(column=7,row=4,pady=20,padx=20)
cell_35.delete(0,'end')





grid[3][6]=DoubleVar()
cell_36= Entry(window,textvariable=grid[3][6],width=2)
cell_36.grid(column=8,row=4,pady=20,padx=20)
cell_36.delete(0,'end')





grid[3][7]=DoubleVar()
cell_37= Entry(window,textvariable=grid[3][7],width=2)
cell_37.grid(column=9,row=4,pady=20,padx=20)
cell_37.delete(0,'end')





grid[3][8]=DoubleVar()
cell_38= Entry(window,textvariable=grid[3][8],width=2)
cell_38.grid(column=10,row=4,pady=20,padx=20)
cell_38.delete(0,'end')





grid[4][0]=DoubleVar()
cell_40= Entry(window,textvariable=grid[4][0],width=2)
cell_40.grid(column=2,row=5,pady=20,padx=20)
cell_40.delete(0,'end')





grid[4][1]=DoubleVar()
cell_41= Entry(window,textvariable=grid[4][1],width=2)
cell_41.grid(column=3,row=5,pady=20,padx=20)
cell_41.delete(0,'end')





grid[4][2]=DoubleVar()
cell_42= Entry(window,textvariable=grid[4][2],width=2)
cell_42.grid(column=4,row=5,pady=20,padx=20)
cell_42.delete(0,'end')





grid[4][3]=DoubleVar()
cell_43= Entry(window,textvariable=grid[4][3],width=2)
cell_43.grid(column=5,row=5,pady=20,padx=20)
cell_43.delete(0,'end')





grid[4][4]=DoubleVar()
cell_44= Entry(window,textvariable=grid[4][4],width=2)
cell_44.grid(column=6,row=5,pady=20,padx=20)
cell_44.delete(0,'end')





grid[4][5]=DoubleVar()
cell_45= Entry(window,textvariable=grid[4][5],width=2)
cell_45.grid(column=7,row=5,pady=20,padx=20)
cell_45.delete(0,'end')





grid[4][6]=DoubleVar()
cell_46= Entry(window,textvariable=grid[4][6],width=2)
cell_46.grid(column=8,row=5,pady=20,padx=20)
cell_46.delete(0,'end')





grid[4][7]=DoubleVar()
cell_47= Entry(window,textvariable=grid[4][7],width=2)
cell_47.grid(column=9,row=5,pady=20,padx=20)
cell_47.delete(0,'end')





grid[4][8]=DoubleVar()
cell_48= Entry(window,textvariable=grid[4][8],width=2)
cell_48.grid(column=10,row=5,pady=20,padx=20)
cell_48.delete(0,'end')





grid[5][0]=DoubleVar()
cell_50= Entry(window,textvariable=grid[5][0],width=2)
cell_50.grid(column=2,row=6,pady=20,padx=20)
cell_50.delete(0,'end')





grid[5][1]=DoubleVar()
cell_51= Entry(window,textvariable=grid[5][1],width=2)
cell_51.grid(column=3,row=6,pady=20,padx=20)
cell_51.delete(0,'end')





grid[5][2]=DoubleVar()
cell_52= Entry(window,textvariable=grid[5][2],width=2)
cell_52.grid(column=4,row=6,pady=20,padx=20)
cell_52.delete(0,'end')





grid[5][3]=DoubleVar()
cell_53= Entry(window,textvariable=grid[5][3],width=2)
cell_53.grid(column=5,row=6,pady=20,padx=20)
cell_53.delete(0,'end')





grid[5][4]=DoubleVar()
cell_54= Entry(window,textvariable=grid[5][4],width=2)
cell_54.grid(column=6,row=6,pady=20,padx=20)
cell_54.delete(0,'end')





grid[5][5]=DoubleVar()
cell_55= Entry(window,textvariable=grid[5][5],width=2)
cell_55.grid(column=7,row=6,pady=20,padx=20)
cell_55.delete(0,'end')





grid[5][6]=DoubleVar()
cell_56= Entry(window,textvariable=grid[5][6],width=2)
cell_56.grid(column=8,row=6,pady=20,padx=20)
cell_56.delete(0,'end')





grid[5][7]=DoubleVar()
cell_57= Entry(window,textvariable=grid[5][7],width=2)
cell_57.grid(column=9,row=6,pady=20,padx=20)
cell_57.delete(0,'end')





grid[5][8]=DoubleVar()
cell_58= Entry(window,textvariable=grid[5][8],width=2)
cell_58.grid(column=10,row=6,pady=20,padx=20)
cell_58.delete(0,'end')





grid[6][0]=DoubleVar()
cell_60= Entry(window,textvariable=grid[6][0],width=2)
cell_60.grid(column=2,row=7,pady=20,padx=20)
cell_60.delete(0,'end')





grid[6][1]=DoubleVar()
cell_61= Entry(window,textvariable=grid[6][1],width=2)
cell_61.grid(column=3,row=7,pady=20,padx=20)
cell_61.delete(0,'end')





grid[6][2]=DoubleVar()
cell_62= Entry(window,textvariable=grid[6][2],width=2)
cell_62.grid(column=4,row=7,pady=20,padx=20)
cell_62.delete(0,'end')





grid[6][3]=DoubleVar()
cell_63= Entry(window,textvariable=grid[6][3],width=2)
cell_63.grid(column=5,row=7,pady=20,padx=20)
cell_63.delete(0,'end')





grid[6][4]=DoubleVar()
cell_64= Entry(window,textvariable=grid[6][4],width=2)
cell_64.grid(column=6,row=7,pady=20,padx=20)
cell_64.delete(0,'end')





grid[6][5]=DoubleVar()
cell_65= Entry(window,textvariable=grid[6][5],width=2)
cell_65.grid(column=7,row=7,pady=20,padx=20)
cell_65.delete(0,'end')





grid[6][6]=DoubleVar()
cell_66= Entry(window,textvariable=grid[6][6],width=2)
cell_66.grid(column=8,row=7,pady=20,padx=20)
cell_66.delete(0,'end')





grid[6][7]=DoubleVar()
cell_67= Entry(window,textvariable=grid[6][7],width=2)
cell_67.grid(column=9,row=7,pady=20,padx=20)
cell_67.delete(0,'end')





grid[6][8]=DoubleVar()
cell_68= Entry(window,textvariable=grid[6][8],width=2)
cell_68.grid(column=10,row=7,pady=20,padx=20)
cell_68.delete(0,'end')





grid[7][0]=DoubleVar()
cell_70= Entry(window,textvariable=grid[7][0],width=2)
cell_70.grid(column=2,row=8,pady=20,padx=20)
cell_70.delete(0,'end')





grid[7][1]=DoubleVar()
cell_71= Entry(window,textvariable=grid[7][1],width=2)
cell_71.grid(column=3,row=8,pady=20,padx=20)
cell_71.delete(0,'end')





grid[7][2]=DoubleVar()
cell_72= Entry(window,textvariable=grid[7][2],width=2)
cell_72.grid(column=4,row=8,pady=20,padx=20)
cell_72.delete(0,'end')





grid[7][3]=DoubleVar()
cell_73= Entry(window,textvariable=grid[7][3],width=2)
cell_73.grid(column=5,row=8,pady=20,padx=20)
cell_73.delete(0,'end')





grid[7][4]=DoubleVar()
cell_74= Entry(window,textvariable=grid[7][4],width=2)
cell_74.grid(column=6,row=8,pady=20,padx=20)
cell_74.delete(0,'end')





grid[7][5]=DoubleVar()
cell_75= Entry(window,textvariable=grid[7][5],width=2)
cell_75.grid(column=7,row=8,pady=20,padx=20)
cell_75.delete(0,'end')





grid[7][6]=DoubleVar()
cell_76= Entry(window,textvariable=grid[7][6],width=2)
cell_76.grid(column=8,row=8,pady=20,padx=20)
cell_76.delete(0,'end')





grid[7][7]=DoubleVar()
cell_77= Entry(window,textvariable=grid[7][7],width=2)
cell_77.grid(column=9,row=8,pady=20,padx=20)
cell_77.delete(0,'end')





grid[7][8]=DoubleVar()
cell_78= Entry(window,textvariable=grid[7][8],width=2)
cell_78.grid(column=10,row=8,pady=20,padx=20)
cell_78.delete(0,'end')





grid[8][0]=DoubleVar()
cell_80= Entry(window,textvariable=grid[8][0],width=2)
cell_80.grid(column=2,row=9,pady=20,padx=20)
cell_80.delete(0,'end')





grid[8][1]=DoubleVar()
cell_81= Entry(window,textvariable=grid[8][1],width=2)
cell_81.grid(column=3,row=9,pady=20,padx=20)
cell_81.delete(0,'end')





grid[8][2]=DoubleVar()
cell_82= Entry(window,textvariable=grid[8][2],width=2)
cell_82.grid(column=4,row=9,pady=20,padx=20)
cell_82.delete(0,'end')





grid[8][3]=DoubleVar()
cell_83= Entry(window,textvariable=grid[8][3],width=2)
cell_83.grid(column=5,row=9,pady=20,padx=20)
cell_83.delete(0,'end')





grid[8][4]=DoubleVar()
cell_84= Entry(window,textvariable=grid[8][4],width=2)
cell_84.grid(column=6,row=9,pady=20,padx=20)
cell_84.delete(0,'end')





grid[8][5]=DoubleVar()
cell_85= Entry(window,textvariable=grid[8][5],width=2)
cell_85.grid(column=7,row=9,pady=20,padx=20)
cell_85.delete(0,'end')





grid[8][6]=DoubleVar()
cell_86= Entry(window,textvariable=grid[8][6],width=2)
cell_86.grid(column=8,row=9,pady=20,padx=20)
cell_86.delete(0,'end')





grid[8][7]=DoubleVar()
cell_87= Entry(window,textvariable=grid[8][7],width=2)
cell_87.grid(column=9,row=9,pady=20,padx=20)
cell_87.delete(0,'end')





grid[8][8]=DoubleVar()
cell_88= Entry(window,textvariable=grid[8][8],width=2)
cell_88.grid(column=10,row=9,pady=20,padx=20)
cell_88.delete(0,'end')



status=StringVar()
status_en=Entry(window,textvariable=status,width=20)
status_en.grid(column=1,row=10,pady=20,padx=20)
status_en.delete(0,'end')


errorMg=StringVar()
error= Entry(window,textvariable=errorMg,width=20)
# error.config(width=20,height=50)
error.grid(column=0,row=11,padx=20,pady=20)
error.delete(0,'end')




for i in range(9):
	for j in range(9):
		grid[i][j].set(0)

status.set("Solving")
errorMg.set("Wrong=Termination")
# for i in range(9):
# 	for j in range(9):
# 		print( int(grid[i][j].get()),end=' ')
# 	print()




# def pri():
# 	for i in range(3):
# 		print(int(grid[0][i].get())+1)



# clr=Button(window,text='RESTART',bg='red',fg='white',width=14,command=pri)
# clr.grid(column=3,row=2,padx=20,pady=20)






# window.mainloop()