import time

def main():
    puzzleInput = ""
    while True:
        try:
            puzzleInput += input("") + "\n"
        except:
            puzzleInput = puzzleInput[:-1]
            break

    startTime = time.time()

    #print(day1part1(puzzleInput))
    #print(day1part2(puzzleInput))
    #print(day2part1(puzzleInput))
    #print(day2part2(puzzleInput))
    #print(day3part1(puzzleInput))
    #print(day3part2(puzzleInput))
    #print(day4part1(puzzleInput))
    #print(day4part2(puzzleInput))
    #print(day5part1(puzzleInput))
    #print(day5part2(puzzleInput))
    #print(day6part1(puzzleInput))
    #print(day6part2(puzzleInput))
    #print(day7part1(puzzleInput))
    #print(day7part2(puzzleInput))
    #print(day8part1(puzzleInput))
    #print(day8part2(puzzleInput))
    #print(day9part1and2(puzzleInput, 1))
    #print(day9part1and2(puzzleInput, 2))
    #print(day10part1(puzzleInput))
    #print(day10part2(puzzleInput))
    #print(day11part1(puzzleInput))
    #print(day11part2(puzzleInput))
    #print(day12part1())
    #print(day12part2())
    #print(day13part1(puzzleInput))
    #print(day13part2(puzzleInput)) # Fun to watch!!
    #print(day14part1(puzzleInput))
    #print(day14part2(puzzleInput))
    print(day15part1(puzzleInput)) # Fun to watch!!
    #print(day15part2(puzzleInput))
    #print(day16part1(puzzleInput))
    #print(day16part2(puzzleInput))

    print("That took " + "{:.5f}".format(time.time() - startTime) + " seconds")

#
def day16part2(puzzleInput):
    
    def FFT(inputNum):
        return inputNum

    messageOffset = int(puzzleInput[:7])

    for _ in range(100):
        puzzleInput = FFT(puzzleInput)

    return puzzleInput[messageOffset:messageOffset + 8]

# 61149209
def day16part1(puzzleInput):

    def FFT(d):
        outputNum = ""
        n = len(d)
        for i in range(n):
            sum = 0
            #print(i)
            i += 1
            m = int(2*i)
            for j in range(int((n-i)/(4*i)) + 1):
                for k in range(i):
                    if (4*i*j)+i+k-1 >= n:
                        break
                    sum += int(d[(4*i*j)+i+k-1])
                    #print("+{}, ".format(d[(4*i*j)+i+k-1]), end="")
                    if (4*i*j)+m+i+k-1 >= n:
                        continue
                    sum -= int(d[(4*i*j)+m+i+k-1])
                    #print("-{}, ".format(d[(4*i*j)+m+i+k-1]), end="")
            #print(sum)
            outputNum += str(abs(sum) % 10)
        return outputNum

    for _ in range(100):
        puzzleInput = FFT(puzzleInput)
        #print(puzzleInput)

    return puzzleInput[:8]

# 384
def day15part2(puzzleInput):

    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    puzzleInput = [int(x) for x in puzzleInput.split(",")]

    ic = intcode(puzzleInput)

    droid = (0,0)
    end = None
    walls = set()
    visited = set()
    visited.add(droid)
    size = 10

    import pygame, random

    s = pygame.display.set_mode((600,600))
    offset = 300

    def dirToMove(direct):
        return [(0,-1), (0,1), (-1,0), (1,0)][direct - 1]

    result = -1
    directions = [1,4,3,2]
    i = 0
    movesPast = []
    farthestFromEnd = 0
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return None
        s.fill((0,0,0))

        #pygame.time.delay(50)

        possibleMoves = []
        directions = [1,3,2,4]
        for i in range(4):
            direct = directions[i]
            move = dirToMove(direct)
            result = ic.continueProgram(direct)

            if result == 0:
                walls.add((droid[0] + move[0], droid[1] + move[1]))
            elif result == 1:
                if (droid[0] + move[0], droid[1] + move[1]) in visited:
                    ic.continueProgram(directions[(i + 2) % 4])
                    continue
                possibleMoves.append(direct)
                ic.continueProgram(directions[(i + 2) % 4])
            elif result == 2:
                if end == None:
                    end = (droid[0] + move[0], droid[1] + move[1])
                    walls = set()
                    visited = set()
                    movesPast = []
                    visited.add(droid)
                    possibleMoves.append(direct)
                ic.continueProgram(directions[(i + 2) % 4])

        if len(possibleMoves) == 1:
            result = ic.continueProgram(possibleMoves[0])
            move = dirToMove(possibleMoves[0])
            droid = (droid[0] + move[0], droid[1] + move[1])
            movesPast.append(possibleMoves[0])
        elif len(possibleMoves) >= 2:
            n = random.randint(0,len(possibleMoves) - 1)
            ic.continueProgram(possibleMoves[n])
            movesPast.append(possibleMoves[n])
            move = dirToMove(possibleMoves[n])
            droid = (droid[0] + move[0], droid[1] + move[1])
        elif len(possibleMoves) == 0:
            if len(movesPast) == 0:
                return farthestFromEnd
            else:
                n = movesPast.pop()
                n = directions[(directions.index(n) + 2) % 4]
                ic.continueProgram(n)
                move = dirToMove(n)
                droid = (droid[0] + move[0], droid[1] + move[1])

        visited.add(droid)
        if end != None:
            if (len(movesPast) + 1) > farthestFromEnd:
                farthestFromEnd = len(movesPast) + 1
            s.fill((255,0,0), rect=(offset + end[0] * size, offset + end[1] * size, size, size))    
        for wall in walls:
            s.fill((255,255,255), rect=(offset + wall[0] * size, offset + wall[1] * size, size, size))
        s.fill((0,0,200), rect=(offset + droid[0] * size, offset + droid[1] * size, size, size))
        pygame.display.update()
    return farthestFromEnd

# 366
def day15part1(puzzleInput):
    
    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    puzzleInput = [int(x) for x in puzzleInput.split(",")]

    ic = intcode(puzzleInput)

    droid = (0,0)
    end = None
    walls = set()
    visited = set()
    visited.add(droid)
    size = 17

    import pygame, random

    WH = 1000

    s = pygame.display.set_mode((WH,WH))
    offset = WH // 2

    def dirToMove(direct):
        return [(0,-1), (0,1), (-1,0), (1,0)][direct - 1]

    directions = [1,4,3,2]
    movesPast = []
    answer = None
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return answer
        s.fill((0,0,0))

        pygame.time.delay(50)

        #determine direction

        possibleMoves = []
        directions = [1,3,2,4]
        for i in range(4):
            direct = directions[i]
            move = dirToMove(direct)
            result = ic.continueProgram(direct)

            #handle result
            if result == 0:
                walls.add((droid[0] + move[0], droid[1] + move[1]))
            elif result == 1:
                if (droid[0] + move[0], droid[1] + move[1]) in visited:
                    ic.continueProgram(directions[(i + 2) % 4])
                    continue
                possibleMoves.append(direct)
                ic.continueProgram(directions[(i + 2) % 4])
            elif result == 2:
                answer = str(len(movesPast) + 1)
                print("Answer is " + answer + " but I'm still gonna do this again yayy!")
                end = (droid[0] + move[0], droid[1] + move[1])
                ic.continueProgram(directions[(i + 2) % 4])

        if len(possibleMoves) == 1:
            result = ic.continueProgram(possibleMoves[0])
            move = dirToMove(possibleMoves[0])
            droid = (droid[0] + move[0], droid[1] + move[1])
            movesPast.append(possibleMoves[0])
        elif len(possibleMoves) >= 2:
            n = random.randint(0,len(possibleMoves) - 1)
            ic.continueProgram(possibleMoves[n])
            movesPast.append(possibleMoves[n])
            move = dirToMove(possibleMoves[n])
            droid = (droid[0] + move[0], droid[1] + move[1])
        elif len(possibleMoves) == 0:
            if len(movesPast) == 0:
                end = None
                walls = set()
                visited = set()
                visited.add(droid)
            else:
                n = movesPast.pop()
                n = directions[(directions.index(n) + 2) % 4]
                ic.continueProgram(n)
                move = dirToMove(n)
                droid = (droid[0] + move[0], droid[1] + move[1])

        visited.add(droid)
        if end != None:
            s.fill((255,0,0), rect=(offset + end[0] * size, offset + end[1] * size, size, size))    
        for wall in walls:
            s.fill((255 - random.randint(0,100),255 - random.randint(0,100),255 - random.randint(0,100)), rect=(offset + wall[0] * size, offset + wall[1] * size, size, size))
        s.fill((0,255,0), rect=(offset + droid[0] * size, offset + droid[1] * size, size, size))
        pygame.display.update()
    return len(movesPast)

# 12039407
def day14part2(puzzleInput):

    puzzleInput = puzzleInput.split("\n")

    recipes = {}
    # {"NAME": {"quantity": 17, "ingredients: [("NAME2", 12), ("NAME3", 8)]"}}

    for recipe in puzzleInput:
        recipe = recipe.split(" => ")

        recipe[1] = recipe[1].split(" ")
        recipes[recipe[1][1]] = {"quantity": int(recipe[1][0])}
        recipes[recipe[1][1]]["ingredients"] = []

        recipe[0] = recipe[0].split(", ")
        for ing in recipe[0]:
            ing = ing.split(" ")
            recipes[recipe[1][1]]["ingredients"].append((ing[1], int(ing[0])))

    import math

    made = {}
    for c in recipes:
        made[c] = 0

    def make(c, n):
        if c == "ORE":
            return n
        totalOre = 0
        toMake = math.ceil(n / recipes[c]["quantity"])
        for ing in recipes[c]["ingredients"]:
            if ing[0] == "ORE":
                totalOre += make(ing[0], ing[1] * toMake)
                continue
            needed = ing[1] * toMake - made[ing[0]]
            made[ing[0]] = 0
            if needed > 0:
                #print("need to make " + str(needed) + " " + ing[0])
                totalOre += make(ing[0], needed)
                remainder = math.ceil(needed / recipes[ing[0]]["quantity"]) * recipes[ing[0]]["quantity"] - needed
                if remainder > 0:
                    pass
                    #print("made an excess of " + str(remainder) + " " + ing[0])
                made[ing[0]] += remainder
            else:
                made[ing[0]] = abs(needed)
                #print("now have " + str(made[ing[0]]) + " " + ing[0])
        return totalOre

    numFuel = 0
    ORE = 1000000000000
    i = ORE
    for d in [10**x for x in range(13, -1, -1)]:
        while True:
            for c in made:
                made[c] = 0
            if (make("FUEL", i) <= ORE):
                numFuel = i
                i += d
            else:
                i -= d
                break

    return numFuel

# 114125
def day14part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n")

    recipes = {}
    # {"NAME": {"quantity": 17, "ingredients: [("NAME2", 12), ("NAME3", 8)]"}}

    for recipe in puzzleInput:
        recipe = recipe.split(" => ")

        recipe[1] = recipe[1].split(" ")
        recipes[recipe[1][1]] = {"quantity": int(recipe[1][0])}
        recipes[recipe[1][1]]["ingredients"] = []

        recipe[0] = recipe[0].split(", ")
        for ing in recipe[0]:
            ing = ing.split(" ")
            recipes[recipe[1][1]]["ingredients"].append((ing[1], int(ing[0])))

    import math

    made = {}
    for c in recipes:
        made[c] = 0

    def make(c, n):
        if c == "ORE":
            return n
        totalOre = 0
        for _ in range(math.ceil(n / recipes[c]["quantity"])):
            for ing in recipes[c]["ingredients"]:
                if ing[0] == "ORE":
                    totalOre += make(ing[0], ing[1])
                    continue
                needed = ing[1] - made[ing[0]]
                made[ing[0]] = 0
                if needed > 0:
                    #print("need to make " + str(needed) + " " + ing[0])
                    totalOre += make(ing[0], needed)
                    remainder = math.ceil(needed / recipes[ing[0]]["quantity"]) * recipes[ing[0]]["quantity"] - needed
                    if remainder > 0:
                        pass
                        #print("made an excess of " + str(remainder) + " " + ing[0])
                    made[ing[0]] += remainder
                elif needed <= 0:
                    made[ing[0]] = abs(needed)
                    #print("now have " + str(made[ing[0]]) + " " + ing[0])
        return totalOre

    return make("FUEL", 1)

# 20940
def day13part2(puzzleInput):

    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput, ballx, boardx):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = ballx - boardx
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    import pygame

    puzzleInput = [int(x) for x in puzzleInput.split(",")]
    puzzleInput[0] = 2
    ic = intcode(puzzleInput)

    size = 30
    tiles = [(0, 0, 0), (107, 48, 0), (153, 46, 44), (224, 195, 47), (47, 91, 22)]

    s = pygame.display.set_mode((44 * size, 24 * size))

    score = 0

    ballx = 0
    boardx = 0

    while True:
        pygame.event.get()
        x = ic.continueProgram(None, ballx, boardx)
        if x == "done":
            return score
        y = ic.continueProgram(None, ballx, boardx)
        tile_id = ic.continueProgram(None, ballx, boardx)

        if x == -1 and y == 0:
            score = tile_id
            continue

        if tile_id == 4:
            ballx = x

        if tile_id == 3:
            boardx = x

        pygame.draw.rect(s, tiles[tile_id], (x*size, y*size, size, size))
        pygame.display.update()

    return None

# 412
def day13part1(puzzleInput):
    
    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    puzzleInput = [int(x) for x in puzzleInput.split(",")]

    ic = intcode(puzzleInput)

    blockTiles = set()

    while True:
        x = ic.continueProgram(None)
        if x == "done":
            return len(blockTiles)
        y = ic.continueProgram(None)
        tile_id = ic.continueProgram(None)

        if tile_id == 2:
            blockTiles.add((x,y))
        elif (x,y) in blockTiles:
            blockTiles.remove((x,y))

    return None

# 295693702908636
def day12part2():
    return "DONE IN C!"

# 12082
def day12part1():
    
    class moon:

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
            self.dx = 0
            self.dy = 0
            self.dz = 0
            self.pot = 0
            self.kin = 0
            self.energy = 0

        def updateVelocity(self, moon2):
            if self.x > moon2.x:
                self.dx -= 1
            elif self.x < moon2.x:
                self.dx += 1

            if self.y > moon2.y:
                self.dy -= 1
            elif self.y < moon2.y:
                self.dy += 1

            if self.z > moon2.z:
                self.dz -= 1
            elif self.z < moon2.z:
                self.dz += 1

        def updatePosition(self):
            self.x += self.dx
            self.y += self.dy
            self.z += self.dz

        def updateEnergy(self):
            self.pot = abs(self.x) + abs(self.y) + abs(self.z)
            self.kin = abs(self.dx) + abs(self.dy) + abs(self.dz)
            self.energy = self.pot * self.kin

    moons = []
    moons.append(moon(13,-13,-2))
    moons.append(moon(16,2,-15))
    moons.append(moon(7,-18,-12))
    moons.append(moon(-3,-8,-8))

    totalSteps = 1000

    for step in range(totalSteps):
        for moon in moons:
            for moon2 in moons:
                if moon == moon2:
                    continue
                moon.updateVelocity(moon2)

        for moon in moons:
            moon.updatePosition()

        for moon in moons:
            moon.updateEnergy()

    totalEnergy = 0
    for moon in moons:
        totalEnergy += moon.energy

    return totalEnergy

# APUGURFH
def day11part2(puzzleInput):
    
    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    TURNLEFT = BLACK = 0
    TURNRIGHT = WHITE = 1

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    panels = {}
    EHPRpos = (0,0)
    EHPRdir = UP
    panels[EHPRpos] = WHITE

    icprogram = intcode([int(x) for x in puzzleInput.split(",")])

    while True:
        if EHPRpos not in panels.keys():
            panels[EHPRpos] = BLACK
        output = icprogram.continueProgram(panels[EHPRpos])
        if output == "done":
            break
        panels[EHPRpos] = output
        output = icprogram.continueProgram(None)
        if output == TURNLEFT:
            EHPRdir -= 1
            EHPRdir %= 4
        else:
            EHPRdir += 1
            EHPRdir %= 4
        EHPRpos = (EHPRpos[0] + (1 if EHPRdir == RIGHT else -1 if EHPRdir == LEFT else 0), EHPRpos[1] + (1 if EHPRdir == UP else -1 if EHPRdir == DOWN else 0))

    from pygame import display, event, QUIT

    SIZE = 50

    #             TOP          BOTTOM      LEFT        RIGHT
    windowWalls = [EHPRpos[0], EHPRpos[1], EHPRpos[0], EHPRpos[1]]

    for panel in panels.keys():
        windowWalls[0] = panel[1] if panel[1] < windowWalls[0] else windowWalls[0]
        windowWalls[1] = panel[1] if panel[1] > windowWalls[1] else windowWalls[1]
        windowWalls[2] = panel[0] if panel[0] < windowWalls[2] else windowWalls[2]
        windowWalls[3] = panel[0] if panel[0] > windowWalls[3] else windowWalls[3]

    w = windowWalls[3] - windowWalls[2]
    h = windowWalls[1] - windowWalls[0]
    s = display.set_mode((w * SIZE, h * SIZE))

    for x in range(w * SIZE):
        for y in range(h * SIZE):
            if (x // SIZE,-1 * y // SIZE) not in panels:
                continue
            colour = (0,0,0) if panels[(x // SIZE,-1 * y // SIZE)] == BLACK else (255,255,255)
            s.set_at((x,y), colour)

    display.update()

    while True:
        for e in event.get():
            if e.type == QUIT:
                return "AS DISPLAYED"

# 1883
def day11part1(puzzleInput):
    
    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.puzzleInput1 += [0 for _ in range(len(puzzleInput1))]
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            if newInput != None:
                self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    return a
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return "done"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    TURNLEFT = BLACK = 0
    TURNRIGHT = WHITE = 1

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    panels = {}
    EHPRpos = (0,0)
    EHPRdir = UP
    panels[EHPRpos] = BLACK

    icprogram = intcode([int(x) for x in puzzleInput.split(",")])

    while True:
        if EHPRpos not in panels.keys():
            panels[EHPRpos] = BLACK
        output = icprogram.continueProgram(panels[EHPRpos])
        if output == "done":
            break
        panels[EHPRpos] = output
        output = icprogram.continueProgram(None)
        if output == TURNLEFT:
            EHPRdir -= 1
            EHPRdir %= 4
        else:
            EHPRdir += 1
            EHPRdir %= 4
        EHPRpos = (EHPRpos[0] + (1 if EHPRdir == RIGHT else -1 if EHPRdir == LEFT else 0), EHPRpos[1] + (1 if EHPRdir == UP else -1 if EHPRdir == DOWN else 0))

    return len(panels)

# 517
def day10part2(puzzleInput):

    def gcm(a,b):
        if b != 0:
            return gcm(b, a % b)
        return abs(a)

    puzzleInput = [[x for x in y] for y in puzzleInput.split("\n")]

    asteroids = []

    numAsteroids = 0
    for x in range(len(puzzleInput)):
        for y in range(len(puzzleInput[x])):
            if puzzleInput[x][y] == '#':
                numAsteroids += 1
                asteroids.append([x,y,0,[]])

    for cur in range(numAsteroids):
        curAsteroid = asteroids[cur]
        for i in range(cur + 1, numAsteroids):
            iAsteroid = asteroids[i]
            distance = (iAsteroid[0] - curAsteroid[0], iAsteroid[1] - curAsteroid[1])
            shrinkFactor = 0
            if distance[0] == 0:
                shrinkFactor = distance[1]
            elif distance[1] == 0:
                shrinkFactor = distance[0]
            else:
                shrinkFactor = gcm(distance[0], distance[1])
            gcDistance = (distance[0] // shrinkFactor, distance[1] // shrinkFactor)
            flag = True
            tempDistance = (curAsteroid[0] + gcDistance[0], curAsteroid[1] + gcDistance[1])
            while tempDistance != (iAsteroid[0], iAsteroid[1]):
                if puzzleInput[tempDistance[0]][tempDistance[1]] == '#':
                    flag = False
                    break
                tempDistance = (tempDistance[0] + gcDistance[0], tempDistance[1] + gcDistance[1])
            if flag:
                curAsteroid[3].append(distance)
                curAsteroid[2] += 1
                iAsteroid[3].append((distance[0] * -1, distance[1] * -1))
                iAsteroid[2] += 1

    maxSight = 0
    maxSightAsteroid = []
    for a in asteroids:
        maxSightAsteroid = a if a[2] >= maxSight else maxSightAsteroid
        maxSight = a[2] if a[2] >= maxSight else maxSight

    from math import atan2, pi

    def compareDistances(a, b):
        aAngle = atan2(-1 * a[0],a[1])/pi*180 - 90
        while aAngle >= 360:
            aAngle -= 360
        while aAngle <= 0:
            aAngle += 360
        bAngle = atan2(-1 * b[0],b[1])/pi*180 - 90
        while bAngle >= 360:
            bAngle -= 360
        while bAngle <= 0:
            bAngle += 360
        return bAngle - aAngle

    sortedDistances = []
    unsortedDistances = maxSightAsteroid[3]
    for _ in range(len(unsortedDistances)):
        smallest = unsortedDistances[0]
        for i in unsortedDistances:
            smallest = i if compareDistances(smallest, i) > 0 else smallest
        sortedDistances.append(smallest)
        unsortedDistances.remove(smallest)

    asteroid200 = []
    curPos = (maxSightAsteroid[0] + sortedDistances[199][0], maxSightAsteroid[1] + sortedDistances[199][1])
    for a in asteroids:
        if a[0] == curPos[0] and a[1] == curPos[1]:
            asteroid200 = a
            break

    return (asteroid200[1] * 100) + asteroid200[0]

# 319
def day10part1(puzzleInput):

    def gcm(a,b):
        if b != 0:
            return gcm(b, a % b)
        return abs(a)

    puzzleInput = [[x for x in y] for y in puzzleInput.split("\n")]

    asteroids = []

    numAsteroids = 0
    for x in range(len(puzzleInput)):
        for y in range(len(puzzleInput[x])):
            if puzzleInput[x][y] == '#':
                numAsteroids += 1
                asteroids.append([x,y,0])

    for cur in range(numAsteroids):
        curAsteroid = asteroids[cur]
        for i in range(cur + 1, numAsteroids):
            iAsteroid = asteroids[i]
            distance = (iAsteroid[0] - curAsteroid[0], iAsteroid[1] - curAsteroid[1])
            shrinkFactor = 0
            if distance[0] == 0:
                shrinkFactor = distance[1]
            elif distance[1] == 0:
                shrinkFactor = distance[0]
            else:
                shrinkFactor = gcm(distance[0], distance[1])
            gcDistance = (distance[0] // shrinkFactor, distance[1] // shrinkFactor)
            flag = True
            distance = (curAsteroid[0] + gcDistance[0], curAsteroid[1] + gcDistance[1])
            while distance != (iAsteroid[0], iAsteroid[1]):
                if puzzleInput[distance[0]][distance[1]] == '#':
                    flag = False
                    break
                distance = (distance[0] + gcDistance[0], distance[1] + gcDistance[1])
            if flag:
                curAsteroid[2] += 1
                iAsteroid[2] += 1

    maxSight = 0
    for a in asteroids:
        maxSight = a[2] if a[2] >= maxSight else maxSight

    return maxSight

# part1: 2890527621, part2: 66772
def day9part1and2(puzzleInput, part):
    
    class intcode():

        def __init__(self, puzzleInput1):
            self.puzzleInput1 = puzzleInput1
            self.i = 0
            self.input3 = []
            self.output4 = []
            self.relativeBase = 0

        def continueProgram(self, newInput):
            self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000,
                    instruction // 10000
                ]
                if opcode == 1:
                    a = b = 0
                    if paramaterModes[0] == 1: # immediate
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0: # positional
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else: # paramaterModes[0] == 2 # relative
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a + b
                    self.i += 4
                elif opcode == 2:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = a * b
                    self.i += 4
                elif opcode == 3:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.i + 1
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.i + 1]
                    else:
                        a = self.puzzleInput1[self.i + 1] + self.relativeBase

                    self.puzzleInput1[a] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.i += 2
                    self.output4.append(a)
                elif opcode == 5:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a != 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 6:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == 0:
                        self.i = b
                    else:
                        self.i += 3
                elif opcode == 7:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a < b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 8:
                    a = b = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]
                    if paramaterModes[1] == 1:
                        b = self.puzzleInput1[self.i + 2]
                    elif paramaterModes[1] == 0:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2]]
                    else:
                        b = self.puzzleInput1[self.puzzleInput1[self.i + 2] + self.relativeBase]

                    if a == b:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3] + (self.relativeBase if paramaterModes[2] == 2 else 0)] = 0
                    self.i += 4
                elif opcode == 9:
                    a = 0
                    if paramaterModes[0] == 1:
                        a = self.puzzleInput1[self.i + 1]
                    elif paramaterModes[0] == 0:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1]]
                    else:
                        a = self.puzzleInput1[self.puzzleInput1[self.i + 1] + self.relativeBase]

                    self.relativeBase += a
                    self.i += 2
                elif opcode == 99:
                    return self.output4[-1]
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return "error"
                    
            return "error"

    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]
    puzzleInput += [0 for _ in range(len(puzzleInput))]

    return intcode([x for x in puzzleInput]).continueProgram(part)

# PFCAK
def day8part2(puzzleInput):

    puzzleInput = [int(x) for x in str(puzzleInput)]

    width = 25
    height = 6
    size = 50

    layers = []
    while len(puzzleInput) >= 1:
        layer = []
        for row in range(height):
            layerRow = []
            for dig in range(width):
                layerRow.append(puzzleInput.pop(0))
            layer.append(layerRow)
        layers.append(layer)

    resultImage = []
    for row in range(height):
        resultRow = []
        for dig in range(width):
            for layer in layers:
                if layer[row][dig] != 2:
                    resultRow.append(layer[row][dig])
                    break
        resultImage.append(resultRow)

    from pygame import display, event, QUIT

    s = display.set_mode((width * size,height * size))

    for row in range(height * size):
        for dig in range(width * size):
            s.set_at((dig, row), (0,0,0) if resultImage[row // size][dig // size] == 0 else (255,255,255))

    display.update()

    while True:
        for e in event.get():
            if e.type == QUIT:
                return "AS DISPLAYED"

# 1064
def day8part1(puzzleInput):

    puzzleInput = [int(x) for x in str(puzzleInput)]

    layers = []
    while len(puzzleInput) >= 1:
        layer = []
        for row in range(6):
            layerRow = []
            for col in range(25):
                layerRow.append(puzzleInput.pop(0))
            layer.append(layerRow)
        layers.append(layer)

    leastZeros = 25*6
    leastZerosLayer = []
    for l in layers:
        numZeros = 0
        for r in l:
            for d in r:
                numZeros += 1 if d == 0 else 0

        if numZeros < leastZeros:
            leastZeros = numZeros
            leastZerosLayer = l

    numOnes = numTwos = 0
    for r in leastZerosLayer:
        for d in r:
            numOnes += 1 if d == 1 else 0
            numTwos += 1 if d == 2 else 0

    return numOnes * numTwos

# 4931744
def day7part2(puzzleInput):

    class intcode():

        def __init__(self, puzzleInput1, phaseNumber):
            self.puzzleInput1 = puzzleInput1
            self.i = 0
            self.input3 = [phaseNumber]

        def continueProgram(self, newInput):
            self.input3.append(newInput)
            while self.i < len(self.puzzleInput1):
                instruction = self.puzzleInput1[self.i]
                opcode = instruction % 100
                paramaterModes = [
                    (instruction % 1000) // 100,
                    (instruction % 10000) // 1000
                ]
                if opcode == 1:
                    self.puzzleInput1[self.puzzleInput1[self.i + 3]] = (self.puzzleInput1[self.i + 1] if paramaterModes[0] == 1 else self.puzzleInput1[self.puzzleInput1[self.i + 1]]) + (self.puzzleInput1[self.i + 2] if paramaterModes[1] == 1 else self.puzzleInput1[self.puzzleInput1[self.i + 2]])
                    self.i += 4
                elif opcode == 2:
                    self.puzzleInput1[self.puzzleInput1[self.i + 3]] = (self.puzzleInput1[self.i + 1] if paramaterModes[0] == 1 else self.puzzleInput1[self.puzzleInput1[self.i + 1]]) * (self.puzzleInput1[self.i + 2] if paramaterModes[1] == 1 else self.puzzleInput1[self.puzzleInput1[self.i + 2]])
                    self.i += 4
                elif opcode == 3:
                    self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]] = self.input3.pop(0)
                    self.i += 2
                elif opcode == 4:
                    temp = self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]]
                    self.i += 2
                    return temp
                elif opcode == 5:
                    if self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]] != 0:
                        self.i = self.puzzleInput1[self.i + 2 if paramaterModes[1] == 1 else self.puzzleInput1[self.i + 2]]
                    else:
                        self.i += 3
                elif opcode == 6:
                    if self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]] == 0:
                        self.i = self.puzzleInput1[self.i + 2 if paramaterModes[1] == 1 else self.puzzleInput1[self.i + 2]]
                    else:
                        self.i += 3
                elif opcode == 7:
                    if self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]] < self.puzzleInput1[self.i + 2 if paramaterModes[1] == 1 else self.puzzleInput1[self.i + 2]]:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3]] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3]] = 0
                    self.i += 4
                elif opcode == 8:
                    if self.puzzleInput1[self.i + 1 if paramaterModes[0] == 1 else self.puzzleInput1[self.i + 1]] == self.puzzleInput1[self.i + 2 if paramaterModes[1] == 1 else self.puzzleInput1[self.i + 2]]:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3]] = 1
                    else:
                        self.puzzleInput1[self.puzzleInput1[self.i + 3]] = 0
                    self.i += 4
                elif opcode == 99:
                    return "stop"
                else:
                    print(i, instruction, opcode)
                    print("invalid opcode")
                    return -1
                    
            return self.output4[-1]

    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    maxoutput = 0
    for phaselist in [[a,b,c,d,e] for a in range(5,10) for b in range(5,10) for c in range(5,10) for d in range(5,10) for e in range(5,10)]:

        if 5 not in phaselist or 6 not in phaselist or 7 not in phaselist or 8 not in phaselist or 9 not in phaselist:
            continue

        ampA = intcode([x for x in puzzleInput], phaselist[0])
        ampB = intcode([x for x in puzzleInput], phaselist[1])
        ampC = intcode([x for x in puzzleInput], phaselist[2])
        ampD = intcode([x for x in puzzleInput], phaselist[3])
        ampE = intcode([x for x in puzzleInput], phaselist[4])

        output = 0

        while True:

            outputTemp = ampA.continueProgram(output)
            if outputTemp == "stop":
                break
            outputTemp = ampB.continueProgram(outputTemp)
            if outputTemp == "stop":
                break
            outputTemp = ampC.continueProgram(outputTemp)
            if outputTemp == "stop":
                break
            outputTemp = ampD.continueProgram(outputTemp)
            if outputTemp == "stop":
                break
            outputTemp = ampE.continueProgram(outputTemp)
            if outputTemp == "stop":
                break
            output = outputTemp

        if output > maxoutput:
            maxoutput = output

    return maxoutput

# 880726
def day7part1(puzzleInput):

    def intcode(puzzleInput1, input3):
        output4 = []
        i = 0
        while i < len(puzzleInput1):
            instruction = puzzleInput1[i]
            opcode = instruction % 100
            paramaterModes = [
                (instruction % 1000) // 100,
                (instruction % 10000) // 1000
            ]
            if opcode == 1:
                puzzleInput1[puzzleInput1[i + 3]] = (puzzleInput1[i + 1] if paramaterModes[0] == 1 else puzzleInput1[puzzleInput1[i + 1]]) + (puzzleInput1[i + 2] if paramaterModes[1] == 1 else puzzleInput1[puzzleInput1[i + 2]])
                i += 4
            elif opcode == 2:
                puzzleInput1[puzzleInput1[i + 3]] = (puzzleInput1[i + 1] if paramaterModes[0] == 1 else puzzleInput1[puzzleInput1[i + 1]]) * (puzzleInput1[i + 2] if paramaterModes[1] == 1 else puzzleInput1[puzzleInput1[i + 2]])
                i += 4
            elif opcode == 3:
                puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]] = input3.pop(0)
                i += 2
            elif opcode == 4:
                output4.append(puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]])
                i += 2
            elif opcode == 5:
                if puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]] != 0:
                    i = puzzleInput1[i + 2 if paramaterModes[1] == 1 else puzzleInput1[i + 2]]
                else:
                    i += 3
            elif opcode == 6:
                if puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]] == 0:
                    i = puzzleInput1[i + 2 if paramaterModes[1] == 1 else puzzleInput1[i + 2]]
                else:
                    i += 3
            elif opcode == 7:
                if puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]] < puzzleInput1[i + 2 if paramaterModes[1] == 1 else puzzleInput1[i + 2]]:
                    puzzleInput1[puzzleInput1[i + 3]] = 1
                else:
                    puzzleInput1[puzzleInput1[i + 3]] = 0
                i += 4
            elif opcode == 8:
                if puzzleInput1[i + 1 if paramaterModes[0] == 1 else puzzleInput1[i + 1]] == puzzleInput1[i + 2 if paramaterModes[1] == 1 else puzzleInput1[i + 2]]:
                    puzzleInput1[puzzleInput1[i + 3]] = 1
                else:
                    puzzleInput1[puzzleInput1[i + 3]] = 0
                i += 4
            elif opcode == 99:
                return output4[-1]
            else:
                print(i, instruction, opcode)
                print("invalid opcode")
                return -1
                
        return output4[-1]

    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    maxoutput = 0
    for phaselist in [[a,b,c,d,e] for a in range(0,5) for b in range(0,5) for c in range(0,5) for d in range(0,5) for e in range(0,5)]:

        if 0 not in phaselist or 1 not in phaselist or 2 not in phaselist or 3 not in phaselist or 4 not in phaselist:
            continue

        output = 0
        input3 = []

        # Amp A
        input3.append(phaselist[0])
        input3.append(0)
        
        output = intcode([x for x in puzzleInput], input3)

        # Amp B
        input3.append(phaselist[1])
        input3.append(output)

        output = intcode([x for x in puzzleInput], input3)

        # Amp C
        input3.append(phaselist[2])
        input3.append(output)

        output = intcode([x for x in puzzleInput], input3)

        # Amp D
        input3.append(phaselist[3])
        input3.append(output)

        output = intcode([x for x in puzzleInput], input3)

        # Amp E
        input3.append(phaselist[4])
        input3.append(output)

        output = intcode([x for x in puzzleInput], input3)

        if output > maxoutput:
            maxoutput = output

    return maxoutput

# 379
def day6part2(puzzleInput):

    class spaceObject:

        def __init__(self, name, parent):
            self.orbitees = []
            self.name = name
            self.parent = parent

        def addOrbitee(self, orbitee):
            self.orbitees.append(orbitee)

        def __str__(self):
            return self.name

    puzzleInput = [(e[:e.find(')')],e[e.find(')')+1:]) for e in puzzleInput.split("\n")]

    def getSpaceObject(root, name, transfers = 0):
        if (root.name == name):
            return (root, transfers - 1)
        for orbitee in root.orbitees:
            result = getSpaceObject(orbitee, name, transfers + 1)
            if result != None:
                return result
        return None

    def calculateOrbits(root, numOrbits = 0):
        root.orbits = numOrbits
        for orbitee in root.orbitees:
            calculateOrbits(orbitee, numOrbits + 1)

    spaceObjects = {}

    for e in puzzleInput:
        spaceObjects[e[0]] = None
        spaceObjects[e[1]] = None

    for e in puzzleInput:
        root = spaceObjects[e[0]]
        child = spaceObjects[e[1]]

        if root == None:
            root = spaceObject(e[0], None)
            spaceObjects[e[0]] = root
        if child == None:
            child = spaceObject(e[1], root)
            spaceObjects[e[1]] = child
        else:
            child.parent = root

        root.addOrbitee(child)

    root = spaceObjects["COM"]

    YOU = getSpaceObject(root, "YOU")[0]
    parent = YOU.parent
    numTransfers = 0

    SAN = getSpaceObject(root, "SAN")[0]

    while getSpaceObject(parent, SAN.name) == None:
        parent = parent.parent
        numTransfers += 1

    return numTransfers + getSpaceObject(parent, SAN.name)[1]

# 200001
def day6part1(puzzleInput):

    class spaceObject:

        def __init__(self, name, parent):
            self.orbitees = []
            self.orbits = 0
            self.name = name
            self.parent = parent

        def addOrbitee(self, orbitee):
            self.orbitees.append(orbitee)

        def __str__(self):
            return self.name

    puzzleInput = [(e[:3],e[4:]) for e in puzzleInput.split("\n")]

    def getSpaceObject(root, name):
        if (root.name == name):
            return root
        for orbitee in root.orbitees:
            result = getSpaceObject(orbitee, name)
            if result != None:
                return result
        return None

    def calculateOrbits(root, numOrbits = 0):
        root.orbits = numOrbits
        for orbitee in root.orbitees:
            calculateOrbits(orbitee, numOrbits + 1)

    spaceObjects = {}

    for e in puzzleInput:
        spaceObjects[e[0]] = None
        spaceObjects[e[1]] = None

    for e in puzzleInput:
        root = spaceObjects[e[0]]
        child = spaceObjects[e[1]]

        if root == None:
            root = spaceObject(e[0], None)
            spaceObjects[e[0]] = root
        if child == None:
            child = spaceObject(e[1], root)
            spaceObjects[e[1]] = child

        root.addOrbitee(child)

    calculateOrbits(spaceObjects["COM"])

    checksum = 0
    for k in spaceObjects.keys():
        checksum += spaceObjects[k].orbits

    return checksum

# 8834787
def day5part2(puzzleInput):

    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    input3 = [5]
    output4 = []

    i = 0
    while i < len(puzzleInput):
        instruction = puzzleInput[i]
        opcode = instruction % 100
        paramaterModes = [
            (instruction % 1000) // 100,
            (instruction % 10000) // 1000
        ]
        if opcode == 1:
            puzzleInput[puzzleInput[i + 3]] = (puzzleInput[i + 1] if paramaterModes[0] == 1 else puzzleInput[puzzleInput[i + 1]]) + (puzzleInput[i + 2] if paramaterModes[1] == 1 else puzzleInput[puzzleInput[i + 2]])
            i += 4
        elif opcode == 2:
            puzzleInput[puzzleInput[i + 3]] = (puzzleInput[i + 1] if paramaterModes[0] == 1 else puzzleInput[puzzleInput[i + 1]]) * (puzzleInput[i + 2] if paramaterModes[1] == 1 else puzzleInput[puzzleInput[i + 2]])
            i += 4
        elif opcode == 3:
            puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] = input3.pop(0)
            i += 2
        elif opcode == 4:
            output4.append(puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]])
            i += 2
        elif opcode == 5:
            if puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] != 0:
                i = puzzleInput[i + 2 if paramaterModes[1] == 1 else puzzleInput[i + 2]]
            else:
                i += 3
        elif opcode == 6:
            if puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] == 0:
                i = puzzleInput[i + 2 if paramaterModes[1] == 1 else puzzleInput[i + 2]]
            else:
                i += 3
        elif opcode == 7:
            if puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] < puzzleInput[i + 2 if paramaterModes[1] == 1 else puzzleInput[i + 2]]:
                puzzleInput[puzzleInput[i + 3]] = 1
            else:
                puzzleInput[puzzleInput[i + 3]] = 0
            i += 4
        elif opcode == 8:
            if puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] == puzzleInput[i + 2 if paramaterModes[1] == 1 else puzzleInput[i + 2]]:
                puzzleInput[puzzleInput[i + 3]] = 1
            else:
                puzzleInput[puzzleInput[i + 3]] = 0
            i += 4
        elif opcode == 99:
            return output4[-1]
        else:
            print(i, instruction, opcode)
            print("invalid opcode")
            return -1
            
    return output4[-1]

# 16209841
def day5part1(puzzleInput):

    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    input3 = [1]
    output4 = []

    i = 0
    while i < len(puzzleInput):
        instruction = puzzleInput[i]
        opcode = instruction % 100
        paramaterModes = [
            (instruction % 1000) // 100,
            (instruction % 10000) // 1000
        ]
        if opcode == 1:
            puzzleInput[puzzleInput[i + 3]] = (puzzleInput[i + 1] if paramaterModes[0] == 1 else puzzleInput[puzzleInput[i + 1]]) + (puzzleInput[i + 2] if paramaterModes[1] == 1 else puzzleInput[puzzleInput[i + 2]])
            i += 4
        elif opcode == 2:
            puzzleInput[puzzleInput[i + 3]] = (puzzleInput[i + 1] if paramaterModes[0] == 1 else puzzleInput[puzzleInput[i + 1]]) * (puzzleInput[i + 2] if paramaterModes[1] == 1 else puzzleInput[puzzleInput[i + 2]])
            i += 4
        elif opcode == 3:
            puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]] = input3.pop(0)
            i += 2
        elif opcode == 4:
            output4.append(puzzleInput[i + 1 if paramaterModes[0] == 1 else puzzleInput[i + 1]])
            i += 2
        elif opcode == 99:
            return output4[-1]
        else:
            print(i, instruction, opcode)
            print("invalid opcode")
            return -1
            
    return output4[-1]

# 324
def day4part2(puzzleInput):

    numPasswords = 0

    for i in range(357253,892943):
        adj_flag = False
        dec_flag = False
        i = str(i)
        for d in range(1,6):
            if int(i[d - 1]) > int(i[d]):
                dec_flag = True
                break
            if d == 1:
                if int(i[d]) == int(i[d - 1]) and int(i[d]) != int(i[d + 1]):
                    adj_flag = True
            elif d == 5:
                if int(i[d]) != int(i[d - 2]) and int(i[d]) == int(i[d - 1]):
                    adj_flag = True
            else:
                if int(i[d]) != int(i[d - 2]) and int(i[d]) == int(i[d - 1]) and int(i[d]) != int(i[d + 1]):
                    adj_flag = True

        if adj_flag and not dec_flag:
            print(i)
            numPasswords += 1

    return numPasswords

# 530
def day4part1(puzzleInput):

    numPasswords = 0

    for i in range(357253,892943):
        adj_flag = False
        dec_flag = False
        i = str(i)
        for d in range(1,6):
            if int(i[d - 1]) > int(i[d]):
                dec_flag = True
                break
            if int(i[d - 1]) == int(i[d]):
                adj_flag = True

        if adj_flag and not dec_flag:
            print(i)
            numPasswords += 1

    return numPasswords

# 15622
def day3part2(puzzleInput):
    
    wireMoves = [x.split(",") for x in (y for y in puzzleInput.split("\n"))]

    wirePositions1 = set()
    wireSteps1 = {}
    curWireSteps1 = 0
    lastPosition = (0,0)
    for i in wireMoves[0]:
        if i[0] == 'U':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps1 += 1
                if (lastPosition[0], lastPosition[1] + j) not in wirePositions1:
                    wireSteps1[(lastPosition[0], lastPosition[1] + j)] = curWireSteps1
                    wirePositions1.add((lastPosition[0], lastPosition[1] + j))
            lastPosition = (lastPosition[0], lastPosition[1] + int(i[1:]))
        elif i[0] == 'D':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps1 += 1
                if (lastPosition[0], lastPosition[1] - j) not in wirePositions1:
                    wireSteps1[(lastPosition[0], lastPosition[1] - j)] = curWireSteps1
                    wirePositions1.add((lastPosition[0], lastPosition[1] - j))
            lastPosition = (lastPosition[0], lastPosition[1] - int(i[1:]))
        elif i[0] == 'L':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps1 += 1
                if (lastPosition[0] - j, lastPosition[1]) not in wirePositions1:
                    wireSteps1[(lastPosition[0] - j, lastPosition[1])] = curWireSteps1
                    wirePositions1.add((lastPosition[0] - j, lastPosition[1]))
            lastPosition = (lastPosition[0] - int(i[1:]), lastPosition[1])
        elif i[0] == 'R':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps1 += 1
                if (lastPosition[0] + j, lastPosition[1]) not in wirePositions1:
                    wireSteps1[(lastPosition[0] + j, lastPosition[1])] = curWireSteps1
                    wirePositions1.add((lastPosition[0] + j, lastPosition[1]))
            lastPosition = (lastPosition[0] + int(i[1:]), lastPosition[1])
        else:
            print("uh oh")
            return -1

    intersectionDistances = []
    lastPosition = (0,0)
    curWireSteps2 = 0
    for i in wireMoves[1]:
        if i[0] == 'U':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps2 += 1
                x = (lastPosition[0], lastPosition[1] + j)
                if x in wirePositions1:
                    intersectionDistances.append(wireSteps1[x] + curWireSteps2)
            lastPosition = (lastPosition[0], lastPosition[1] + int(i[1:]))
        elif i[0] == 'D':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps2 += 1
                x = (lastPosition[0], lastPosition[1] - j)
                if x in wirePositions1:
                    intersectionDistances.append(wireSteps1[x] + curWireSteps2)
            lastPosition = (lastPosition[0], lastPosition[1] - int(i[1:]))
        elif i[0] == 'L':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps2 += 1
                x = (lastPosition[0] - j, lastPosition[1])
                if x in wirePositions1:
                    intersectionDistances.append(wireSteps1[x] + curWireSteps2)
            lastPosition = (lastPosition[0] - int(i[1:]), lastPosition[1])
        elif i[0] == 'R':
            for j in range(1, 1 + int(i[1:])):
                curWireSteps2 += 1
                x = (lastPosition[0] + j, lastPosition[1])
                if x in wirePositions1:
                    intersectionDistances.append(wireSteps1[x] + curWireSteps2)
            lastPosition = (lastPosition[0] + int(i[1:]), lastPosition[1])
        else:
            print("uh oh")
            return -1

    minDist = intersectionDistances[0]
    for d in intersectionDistances:
        minDist = d if d < minDist else minDist

    return minDist

# 273
def day3part1(puzzleInput):
    
    wireMoves = [x.split(",") for x in (y for y in puzzleInput.split("\n"))]

    wirePositions1 = set()
    lastPosition = (0,0)
    for i in wireMoves[0]:
        if i[0] == 'U':
            for j in range(1, 1 + int(i[1:])):
                wirePositions1.add((lastPosition[0], lastPosition[1] + j))
            lastPosition = (lastPosition[0], lastPosition[1] + int(i[1:]))
        elif i[0] == 'D':
            for j in range(1, 1 + int(i[1:])):
                wirePositions1.add((lastPosition[0], lastPosition[1] - j))
            lastPosition = (lastPosition[0], lastPosition[1] - int(i[1:]))
        elif i[0] == 'L':
            for j in range(1, 1 + int(i[1:])):
                wirePositions1.add((lastPosition[0] - j, lastPosition[1]))
            lastPosition = (lastPosition[0] - int(i[1:]), lastPosition[1])
        elif i[0] == 'R':
            for j in range(1, 1 + int(i[1:])):
                wirePositions1.add((lastPosition[0] + j, lastPosition[1]))
            lastPosition = (lastPosition[0] + int(i[1:]), lastPosition[1])
        else:
            print("uh oh")
            return -1

    intersectionDistances = []
    lastPosition = (0,0)
    for i in wireMoves[1]:
        if i[0] == 'U':
            for j in range(1, 1 + int(i[1:])):
                x = (lastPosition[0], lastPosition[1] + j)
                if x in wirePositions1:
                    intersectionDistances.append(abs(x[0]) + abs(x[1]))
            lastPosition = (lastPosition[0], lastPosition[1] + int(i[1:]))
        elif i[0] == 'D':
            for j in range(1, 1 + int(i[1:])):
                x = (lastPosition[0], lastPosition[1] - j)
                if x in wirePositions1:
                    intersectionDistances.append(abs(x[0]) + abs(x[1]))
            lastPosition = (lastPosition[0], lastPosition[1] - int(i[1:]))
        elif i[0] == 'L':
            for j in range(1, 1 + int(i[1:])):
                x = (lastPosition[0] - j, lastPosition[1])
                if x in wirePositions1:
                    intersectionDistances.append(abs(x[0]) + abs(x[1]))
            lastPosition = (lastPosition[0] - int(i[1:]), lastPosition[1])
        elif i[0] == 'R':
            for j in range(1, 1 + int(i[1:])):
                x = (lastPosition[0] + j, lastPosition[1])
                if x in wirePositions1:
                    intersectionDistances.append(abs(x[0]) + abs(x[1]))
            lastPosition = (lastPosition[0] + int(i[1:]), lastPosition[1])
        else:
            print("uh oh")
            return -1

    minDist = intersectionDistances[0]
    for d in intersectionDistances:
        minDist = d if d < minDist else minDist

    return minDist

# 7603
def day2part2(puzzleInput):
    
    originalPuzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    for noun,verb in [(n,v) for n in range(100) for v in range(100)]:

        puzzleInput = [x for x in originalPuzzleInput]

        puzzleInput[1] = noun
        puzzleInput[2] = verb

        for i in range(0,len(puzzleInput), 4):
            if puzzleInput[i] == 1:
                puzzleInput[puzzleInput[i + 3]] = puzzleInput[puzzleInput[i + 1]] + puzzleInput[puzzleInput[i + 2]]
            elif puzzleInput[i] == 2:
                puzzleInput[puzzleInput[i + 3]] = puzzleInput[puzzleInput[i + 1]] * puzzleInput[puzzleInput[i + 2]]
            elif puzzleInput[i] == 99:
                if puzzleInput[0] == 19690720:
                    return (100 * noun) + verb
            else:
                break

    return -1

# 5534943
def day2part1(puzzleInput):
    
    puzzleInput = list(map(lambda e: int(e), puzzleInput.split(",")))

    puzzleInput[1] = 12
    puzzleInput[2] = 2

    for i in range(0,len(puzzleInput), 4):
        if puzzleInput[i] == 1:
            puzzleInput[puzzleInput[i + 3]] = puzzleInput[puzzleInput[i + 1]] + puzzleInput[puzzleInput[i + 2]]
        elif puzzleInput[i] == 2:
            puzzleInput[puzzleInput[i + 3]] = puzzleInput[puzzleInput[i + 1]] * puzzleInput[puzzleInput[i + 2]]
        elif puzzleInput[i] == 99:
            break
        else:
            return -1

    return puzzleInput[0]

# 4882038
def day1part2(puzzleInput):
    
    puzzleInput = map(lambda e: int(e), puzzleInput.split("\n"))
    
    sum = 0
    for i in puzzleInput:
        tempSum = 0
        while True:
            x = (i // 3) - 2
            if x <= 0:
                break
            tempSum += x
            i = x
        sum += tempSum

    return sum

# 3256599
def day1part1(puzzleInput):

    puzzleInput = map(lambda e: int(e), puzzleInput.split("\n"))
    
    sum = 0
    for i in puzzleInput:
        sum += (i // 3) - 2

    return sum

main()