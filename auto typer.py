import pyautogui
import time

# comments = ["Hi","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome","I am a messy programmer"]
# comments=["Hi","This is Saksham",'And this is automated texting','using python','Just one click and BOOOOOM','BOOOOOM','Booooooooom']
comments=['KemPalty','yaha waha saare','jaahan me tera naam hai','Sir pe o jiske','Mohobat ka taaj hai',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad',"Jijaji",'oh','Jijaji','Zindabad']


#i=int(0)

time.sleep(5)

for i in range(0,9):
	pyautogui.typewrite(f"\n\n\ngrid[1][{i}]=DoubleVar()\ncell_1{i}= Entry(window,textvariable=grid[1][{i}],width=2)\ncell_1{i}.grid(column={i+2},row=2,pady=20,padx=20)\ncell_0{i}.delete(0,'end')\n\n\n")


# for i in range(1,125):
# 	pyautogui.typewrite("PKMKB")
# 	pyautogui.typewrite("\n")
	# time.sleep(1/2)
# while True:
# 	i+=1
# 	pyautogui.typewrite(f"Ram Ram Ram Ram Ram Ram {i}")
# 	pyautogui.typewrite("\n")
# 	if i==124:	break
# i=int(0)
# while True:
# 	i+=1
# 	pyautogui.typewrite("Jai SHree Ram <3")
# 	pyautogui.typewrite("\n")
# for i in range(10):
#     pyautogui.typewrite(comments[i%7])
#     pyautogui.typewrite("\n")
#     time.sleep(2)