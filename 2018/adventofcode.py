'''
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()
'''

#DAY 12 A
#ANS:

'''
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()
'''















#DAY 11 A/B
#ANS: 243,27 / 284,172,12
'''
flhndl = open("adventofcode.txt", 'r')
data = int(flhndl.read())
flhndl.close()

cellsEnergy = []
for x in range(1,301):
	cellsRow = []
	for y in range(1,301):
		rackID = 10 + x
		power = rackID * y
		power += data
		power *= rackID
		power = int(str(power)[-3])
		power -= 5
		cellsRow.append(power)
	cellsEnergy.append(cellsRow)

mostPower = 0
gridSpot = [0,0,0]
powerGrids = [[1,cellsEnergy]]
print(powerGrids[-1][0],len(powerGrids[-1][1]))
for s in range(1,21):
	print(s)
	gridEnergy = []
	for xGrid in range(301-s):
		gridRow = []
		for yGrid in range(301-s):
			gridPower = 0
			for w in range(s):
				for h in range(s):
					gridPower += powerGrids[0][1][xGrid+w][yGrid+h]
			gridRow.append(gridPower)
		gridEnergy.append(gridRow)

	for i in range(len(gridEnergy)):
		for j in range(len(gridRow)):
			if gridEnergy[i][j] > mostPower:
				mostPower = gridEnergy[i][j]
				gridSpot = [i+1,j+1,s]
	powerGrids.append([s,gridEnergy])
	print(powerGrids[-1][0],len(powerGrids[-1][1]))
	print(gridSpot)
'''

#DAY 10 A
#ANS: RLEZNRAN / 10240
'''
import pygame

pygame.init()

flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()

for i in range(len(data)):
	data[i] = [int(data[i][10:16]),int(data[i][18:24]),int(data[i][36:38]),int(data[i][40:42])]

bigX = 0
bigY = 0
for i in data:
	if i[0] > bigX:
		bigX = i[0]
	if i[1] > bigY:
		bigY = i[1]

window = pygame.display.set_mode((bigX//50,bigY//200))

class light():

	def __init__(self,x,y,dx,dy):

		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

	def move(self):

		window.set_at((self.x,self.y), (0,0,0))

		self.x += self.dx
		self.y += self.dy

		window.set_at((self.x,self.y), (0,255,0))

	def moveBack(self):

		window.set_at((self.x,self.y), (0,0,0))

		self.x -= self.dx
		self.y -= self.dy

		window.set_at((self.x,self.y), (0,255,0))

lights = []
for i in data:
	lights.append(light(i[0],i[1],i[2],i[3]))

flag = False
flag2 = False
flag3 = False
seconds = 0
while True:

	for e in pygame.event.get():
		if e.type==pygame.KEYDOWN:
			if int(e.key)==100:
				flag = True
			if int(e.key)==115:
				flag2 = True
			if int(e.key)==102:
				flag3 = True
		elif e.type==pygame.KEYUP:
			if int(e.key)==100:
				flag = False
			if int(e.key)==115:
				flag2 = False

	if flag:
		if flag3:
			pygame.time.delay(5000)
			print(seconds)
			pygame.image.save(window,'img.bmp')
			flag3 = False
		else:
			pygame.time.delay(200)

	if flag2:
		seconds -= 1
		for l in lights:
			l.moveBack()
	else:
		seconds += 1
		for l in lights:
			l.move()

	pygame.display.update()

'''
#DAY 9 A/B(fail)
#ANS: 434674 / (don't know)
'''
import time

flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().split()
flhndl.close()

numPlayers = int(data[0])
#part A
numMarbles = int(data[6])
#part B
#numMarbles = int(data[6])*100

#WHAT KIND OF A FUCKING GAME IS THIS?!!?!?!??!?!
player = {}
for i in range(numPlayers):
	player[i+1] = 0

ringOfMarbles = [0,1]
curMarbleIndex = 1
popped = []
for m in range(2,numMarbles+1):

	if m%23==0:
		curMarbleIndex -= 7
		if curMarbleIndex < 0:
			curMarbleIndex = ringC + curMarbleIndex
		popped.append(ringOfMarbles.pop(curMarbleIndex))
		points = popped[-1] + m
		curPlayer = m%numPlayers
		if curPlayer==0:
			curPlayer = numPlayers
		player[curPlayer] += points
		continue
	ringC = len(ringOfMarbles)
	curMarbleIndex = (curMarbleIndex + 2) % ringC
	ringOfMarbles.insert(curMarbleIndex, m)

	#print(ringOfMarbles)

pattern = []
for i in range(len(popped)-1):
	pattern.append(popped[i+1]-popped[i])

start = 0
loop = []
for i in range(1,len(pattern)):
	if 1.0==pattern[start]/pattern[i]:
		loop.append(pattern[i-start])
		start += 1
	else:
		print(loop)
		start = 0
		loop = []

print(loop)

highScore = 0
for i in player:
	if player[i] > highScore:
		highScore = player[i]

print(highScore)
'''

#DAY 8 A/B
#ANS: 42768 / 34348
'''
import time

flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().split()
flhndl.close()
for i in range(len(data)):
	data[i] = int(data[i])

#part A
totalMeta = 0
meta = 0
skip = 0
children = [[1,0,-1]]
#part B
depth = len(children)-1
childrenOf = {-1:['n']}
metadataOf = {-1:[]}
ID = 0
flag = True
for i in range(len(data)):

	if skip > 0:
		skip -= 1
		continue

	if children[-1][0]==0:
		for j in range(children[-1][1]):
			totalMeta += data[i+j]
			meta += data[i+j]
			try:
				metadataOf[children[-1][2]].append(data[i+j])
			except:
				metadataOf[children[-1][2]] = [data[i+j]]
		skip += j
		if flag:
			childrenOf[children[-1][2]] = ['v',meta]
			#print('children of', children[-1][2], 'are', childrenOf[children[-1][2]])
		else:
			#print('metadata of', children[-1][2], 'is', metadataOf[children[-1][2]])
			pass
		children.pop()
		meta = 0
	else:
		children[-1][0] -= 1
		children.append([data[i],data[i+1],ID])
		skip += 1
		ID += 1

	if depth <= len(children)-1:
		flag = True
		depth = len(children)-1
		try:
			childrenOf[children[-2][2]].append(children[-1][2])
		except:
			childrenOf[children[-2][2]] = ['n',children[-1][2]]
		#print(depth, "DOWN")
		#print('children of', children[-2][2], 'are', childrenOf[children[-2][2]])
		#print('node', children[-1][2], 'is', children[-1])
	else:
		flag = False
		depth = len(children)-1
		#print(depth, "UP")

	#time.sleep(1)

def getScore(node):
	if childrenOf[node][0]=='v':
		#print(node)
		#print(metadataOf[node])
		#print(childrenOf[node])
		#print('value of node', node, 'is', childrenOf[node][1])
		#time.sleep(1)
		return childrenOf[node][1]
	else:
		ans = 0
		#print(node)
		#print(metadataOf[node])
		#print(childrenOf[node])
		for i in metadataOf[node]:
			try:
				score = getScore(childrenOf[node][i])
				ans += score
			except:
				ans += 0
		return ans

rootMeta = getScore(0)
print(rootMeta)
print(totalMeta)
'''

#DAY 7 A/B
#ANS: ADEFKLBVJQWUXCNGORTMYSIHPZ / 1120
'''
#part A
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()

stepsAfter = {}
for i in data:
	stepsAfter[i[5]] = []
for i in data:
	stepsAfter[i[5]].append(i[36])
stepsBefore = {}
for i in data:
	stepsBefore[i[36]] = []
for iADEFKLBVJQWUXCNGORTMYSIHPZ in data:
	stepsBefore[i[36]].append(i[5])

curSteps = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	try:
		stepsBefore[i]
	except:
		curSteps.append(i)

answer = ''
while len(answer) < 26:
	curSteps.sort()
	i = curSteps[0]
	curSteps.pop(0)
	answer += i
	if not(i in stepsAfter):
		continue
	for j in stepsAfter[i]:
		if i in stepsBefore[j]:
			stepsBefore[j].remove(i)
		if stepsBefore[j]==[]:
			curSteps.append(j)

stepsBefore = {}
for i in data:
	stepsBefore[i[36]] = []
for i in data:
	stepsBefore[i[36]].append(i[5])

print(answer)

#part B
workers = []
for i in range(5):
	#   [CURRENT STEP, TIME TAKEN SO FAR]
	workers.append(['.',0])
stepsDone = ''

availableSteps = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	try:
		stepsBefore[i]
	except:
		availableSteps.append(i)
availableSteps.sort()

stepsDone = []
seconds = 0
while True:

	for w in workers:
		if ord(w[0])-4==w[1]:
			finJob = w[0]
			w[0],w[1] = '.',0
			stepsDone.append(finJob)
			for i in stepsBefore:
				if finJob in stepsBefore[i]:
					stepsBefore[i].remove(finJob)
			print("finished",finJob)
			try:
				stepsAfter[finJob]
			except:
				break
			for i in stepsAfter[finJob]:
				print(i)
				if stepsBefore[i]==[]:
					availableSteps.append(i)
					for j in stepsAfter:
						if i in stepsAfter[j] and j!=finJob:
							stepsAfter[j].remove(i)
			availableSteps.sort()
	print(availableSteps)
	temp = availableSteps[:]
	for i in temp:
		foundWorker = False
		for w in workers:
			if w[0]=='.':
				w[0] = i
				w[1] = 0
				availableSteps.remove(i)
				foundWorker = True
				break
		if not foundWorker:
			print(i, "couldn't find a worker")
			break
	print(seconds,workers)
	flag = False
	for w in workers:
		if w[0]!='.':
			flag = True
			w[1] += 1
	if not flag:
		break
	seconds += 1

print(seconds)
'''

#DAY 6 A/B
#ANS: 5365 / 42513
'''
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()

import pygame
pygame.init()

w = 400
h = 400
window = pygame.display.set_mode((w,h))

for i in range(len(data)):
	data[i] = data[i].split(", ")
	data[i].append(i+1)

for i in data:
	window.set_at((int(i[0]),int(i[1])),(0,255,5*i[2]))
pygame.display.update()

areas = {}
for i in data:
	areas[(int(i[0]),int(i[1]))] = 0

allCoords = []
for i in range(w*h):
	allCoords.append(0)
coordNum = -1
safeSpots = 0
for x1 in range(w):
	for y1 in range(h):
		coordNum += 1
		smallestDist = 800
		closest = 0
		count = 0
		for i in areas:
			x2,y2 = i
			allCoords[coordNum] += (abs(x2-x1)+abs(y2-y1))
			if (abs(x2-x1)+abs(y2-y1)) < smallestDist:
				count = 1
				closest = i
				smallestDist = (abs(x2-x1)+abs(y2-y1))
			elif (abs(x2-x1)+abs(y2-y1))==smallestDist:
				count = 2
		if x1==0 or x1==w-1 or y1==0 or y1==h-1:
			areas[closest] = -99999
		elif count==1:
			areas[closest] += 1
			window.set_at((x1,y1),(smallestDist%255,0,0))
		else:
			window.set_at((x1,y1),(0,0,255))

		if allCoords[coordNum] < 10000:
			safeSpots += 1
			r,g,b,_ = window.get_at((x1,y1))
			window.set_at((x1,y1),(255-r,g,b))

for i in data:
	window.set_at((int(i[0]),int(i[1])),(0,255,5*i[2]))
pygame.display.update()

biggest = 0
for i in areas:
	if areas[i] > biggest:
		biggest = areas[i]
print(biggest, safeSpots)

while True:
	for e in pygame.event.get():
		if e.type==pygame.KEYDOWN:
			exit()

'''
#DAY 5 A/B
#ANS: 9822 / 5726
'''
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().strip()
flhndl.close()

#part A
j = 0
while True:
	if j%1000==0:
		print("still going...")
		j = 0
	j += 1
	flag = False
	for i in range(len(data)-1,0,-1):
		a = data[i]
		b = data[i-1]
		if ord(a)+32==ord(b) or ord(a)-32==ord(b):
			data = data[:i-1] + data[i+1:]
			flag = True
			break
	if not flag:
		break

print(data)
print(len(data))

#part B
minimum = 50000
badUnit = ''
for i in range(97,123):
	temp = data
	a = chr(i)
	b = chr(i-32)
	while a in temp:
		c = temp.find(a)
		temp = temp[:c] + temp[c+1:]
	while b in temp:
		c = temp.find(b)
		temp = temp[:c] + temp[c+1:]
	while True:
		flag = False
		for i in range(len(temp)-1,0,-1):
			a = temp[i]
			b = temp[i-1]
			if ord(a)+32==ord(b) or ord(a)-32==ord(b):
				temp = temp[:i-1] + temp[i+1:]
				flag = True
				break
		if not flag:
			break
	if len(temp) < minimum:
		minimum = len(temp)
		badUnit = a

print(minimum, badUnit)
'''

#DAY 4 A/B
#ANS: 67558 / 78990
'''
flhndl = open("adventofcode.txt", 'r')
data = flhndl.read().splitlines()
flhndl.close()
#First sorting
#flhndl = open("adventofcode.txt", 'w')
#data.sort()
#for i in data:
#	flhndl.write(i+"\n")

for i in range(len(data)):
	data[i] = data[i][12:]

elfList = {}
elf = 0
sleeping = False
minute = 0
for i in range(len(data)):
	l = data[i]
	if l[7]=='G':
		elf = int(l.split()[2].strip('#'))
		sleeping = False
		if not (elf in elfList):
			elfList[elf] = {}
			for i in range(60):
				elfList[elf][i] = 0
	else:
		sleep = l[7]
		if sleep=='f':
			sleeping==True
			minute = int(l[3:5])
		else:
			sleeping = False
			for i in range(minute,int(l[3:5])):
				elfList[elf][i] += 1

elfListMax = {}
maximum = 0
maxElf = 0
for e in elfList:

	e = int(e)
	elfListMax[e] = 0
	for i in range(60):
		elfListMax[e] += int(elfList[e][i])
		if elfListMax[e] > maximum:
			maximum = elfListMax[e]
			maxElf = e

maxMin = 0
maxSleep = 0
for i in range(60):

	if elfList[int(maxElf)][i] > maxSleep:
		maxMin = i
		maxSleep = elfList[int(maxElf)][i]

#part A
#print(int(maxElf)*int(maxMin))

#part B
maximum = 0
elfId = 0
minute = 0
for i in elfList:
	for j in elfList[i]:
		if elfList[i][j] > maximum:
			maximum = elfList[i][j]
			elfId = i
			minute = j

print(int(elfId)*int(minute))
'''

#DAY 3 A/B
#ANS: 107820 / 661
'''
import pygame
pygame.init()
window = pygame.display.set_mode((1000,1000))

flhndl = open("adventofcode.txt", 'r')
text = flhndl.read()
flhndl.close()
print("That's a lot of elves!")

text = text.split("#")
text.pop(0)

for i in range(len(text)):

	text[i] = text[i].strip()
	text[i] = text[i].split(" @ ")
	text[i][1] = text[i][1].split(": ")
	text[i][1][0] = text[i][1][0].split(",")
	text[i][1][1] = text[i][1][1].split("x")
#   0              1
#             0         1
#           0   1     0   1
# ['id', [['x','y'],['w','h']]]
space = 0
for i in text:
	x,y = int(i[1][0][0]),int(i[1][0][1])
	w,h = int(i[1][1][0]),int(i[1][1][1])

	pygame.draw.rect(window, (0,0,0), (0,0,1000,1000))

	#part B (very slow)
	for l in text:
		if l==i:
			continue
		xa,ya = int(l[1][0][0]),int(l[1][0][1])
		wa,ha = int(l[1][1][0]),int(l[1][1][1])
		pygame.draw.rect(window, (0,255,0), (xa,ya,wa,ha))
	pygame.display.update()
	flag = False
	for j in range(w):
		for k in range(h):
			_,g,_,_ = window.get_at((x+j,y+k))
			if g==255:
				flag = True
				break
		if flag:
			break
	if not flag:
		print(i[0])
	
for i in text:
	x,y = int(i[1][0][0]),int(i[1][0][1])
	w,h = int(i[1][1][0]),int(i[1][1][1])

	space += w*h
	pygame.draw.rect(window, (0,255,0), (x,y,w,h))

#part A
pygame.display.update()
for i in range(1000):
	for j in range(1000):
		_,g,_,_ = window.get_at((i,j))
		if g==255:             
			space -= 1
print(space)
'''

#DAY 2 B
#ANS: wugbihckpoymcpaxefotvdzns
'''
flhndl = open("adventofcode.txt", 'r')
text = flhndl.read()
flhndl.close()

text = text.split()

for i in range(len(text[:-1])):
	current = text[i]
	for j in range(len(text[i+1:])):
		new = text[j]
		flag = False
		for char in range(len(current)):
			if current[char]!=new[char]:
				if not flag:
					flag = True
					next = False
				else:
					k = char
					next = True
					break
		if not next:
			print(text[i],text[j])
			break
'''
