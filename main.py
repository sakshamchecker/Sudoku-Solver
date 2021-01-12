from tkinter import Tk,Button,Label,StringVar,Entry,DoubleVar
import window as w


# for i in range(9):
# 	for j in range(9):
# 		print( int(w.grid[i][j].get()),end=' ')
# 	print()


# for i in range(9):
# 	for j in range(9):
# 		w.grid[i][j].set(1)
# grid=[]
# for i in range(9):
# 	grid.append([0,0,0,0,0,0,0,0,0])



def findUnassigned(l):
    for row in range(9):
        for col in range(9):
            if(int(w.grid[row][col].get())== 0):
                l[0]= row
                l[1]= col
                return True
    return False


def usedInRow(row,num):
	for j in range(9):
		if int(w.grid[row][j].get())==num:
			return True
	return False


def usedInCol(col,num):
	for i in range(9):
		if int(w.grid[i][col].get())==num:
			return True
	return False



def usedInBox(boxStartRow,boxStartCol,nu):
	for i in range(3):
		for j in range(3):
			if(int(w.grid[i+boxStartRow][j+boxStartCol].get())==int(nu)):
				return True
	return False


def isSafe(row,col,num):
	StartRow=row -( row % 3)
	StartCol=col-(col % 3)
	return (not usedInRow(row,num) and not usedInCol(col,num) and not usedInBox(StartRow,StartCol,num) and int(w.grid[row][col].get())==0)


def solve():
	
	l=[0,0]


	if not findUnassigned(l):
		return True
	row=l[0]
	col=l[1]
	for num in range(1,10):
		if isSafe(row,col,num):
			w.grid[row][col].set(num)

			if(solve()):
				return False
			w.grid[row][col].set(0)

	return False


def star():
	try:
		solve()
		w.status.set("Solved")
	except:
			w.status.set("ERROR!, Can't be solved")

start=Button(w.window,text='SOLVE',bg='red',fg='white',width=14,command=star)
start.grid(column=11,row=10,padx=20,pady=20)

w.window.mainloop()