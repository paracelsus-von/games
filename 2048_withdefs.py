import sys
import msvcrt
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("  ___   ___  _  _   ___  ")
print(" |__ \ / _ \| || | / _ \  ")
print("    ) | | | | || || (_) | ")
print("   / /| | | |__  __> _ <  ")
print("  / /_| |_| |  | || (_) | ")
print(" |____|\___/   |_| \___/  ")
print("\n")
print("Welcome to 2048. \nUse WASD to move the board. \nPress ENTER to begin. \nHave fun!")

raw_input()

# 50% chance of 2; 50% chance of 4
X = [2, 4]
# 1/2 chance of '-', 1/3 chance of 2, 1/6 chance of 4
X2 = ['-', '-', '-', 2, 2, 4]

# randomly populates grid initially
r1 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r2 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r3 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r4 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]

score = 0
winning = 1

# clears terminal output
os.system('cls' if os.name == 'nt' else 'clear')

highscorefile = open('highscore.txt', 'r+')
highscore = int(highscorefile.read())


print '\n'
print '   '.join(str(r) for r in r1)
print '   '.join(str(r) for r in r2)
print '   '.join(str(r) for r in r3)
print '   '.join(str(r) for r in r4)
print '\nScore: %d' % score
print '\nHigh score: %d' % highscore



def shiftNumbers(r1, r2, r3, r4, score):
	# shifts grid in direction of movement, doubling same adjacent squares
	# updates score, adds any new tiles create by doubling
	for c in range(4):
		# shifts column down line of movement until all -'s have been killed
		while type(r4[c]) != int and not (type(r3[c]) != int and type(r2[c]) != int and type(r1[c]) != int):
			r4[c] = r3[c]
			r3[c] = r2[c]
			r2[c] = r1[c]
			r1[c] = '-'
		
		while type(r3[c]) != int and not (type(r2[c]) != int and type(r1[c]) != int):
			r3[c] = r2[c]
			r2[c] = r1[c]
			r1[c] = '-'
		
		while type(r2[c]) != int and not (type(r1[c]) != int):
			r2[c] = r1[c]
			r1[c] = '-'
	
		if r3[c] == r4[c] and type(r4[c]) == int:
			r4[c] *= 2
			r3[c] = r2[c]
			r2[c] = r1[c]
			r1[c] = '-'
			
			score += r4[c]
		
			if r2[c] == r3[c] and type(r3[c]) == int:
				r3[c] *= 2
				r2[c] = r1[c]
				
				score += r3[c]
			
		elif r2[c] == r3[c] and type(r3[c]) == int:
			r3[c] *= 2
			r2[c] = r1[c]
			r1[c] = '-'
			
			score += r3[c]
	
		elif r1[c] == r2[c] and type(r2[c]) == int:
			r2[c] *= 2
			r1[c] = '-'
			
			score += r2[c]
	
	return [score, r1, r2, r3, r4]


def orientGrid(r1, r2, r3, r4, tempr1, tempr2, tempr3, tempr4, x):
	#reorients grid so all actions are as if you were pushing the numbers 'down'
	if x == 'w':
		r4 = tempr1
		r3 = tempr2
		r2 = tempr3
		r1 = tempr4
	
	elif x == 'a':
		r4[0] = tempr1[0]
		r4[1] = tempr2[0]
		r4[2] = tempr3[0]
		r4[3] = tempr4[0]
		
		r3[0] = tempr1[1]
		r3[1] = tempr2[1]
		r3[2] = tempr3[1]
		r3[3] = tempr4[1]
		
		r2[0] = tempr1[2]
		r2[1] = tempr2[2]
		r2[2] = tempr3[2]
		r2[3] = tempr4[2]
		
		r1[0] = tempr1[3]
		r1[1] = tempr2[3]
		r1[2] = tempr3[3]
		r1[3] = tempr4[3]
	
	elif x == 'd':
		r4[0] = tempr1[3]
		r4[1] = tempr2[3]
		r4[2] = tempr3[3]
		r4[3] = tempr4[3]
		
		r3[0] = tempr1[2]
		r3[1] = tempr2[2]
		r3[2] = tempr3[2]
		r3[3] = tempr4[2]
		
		r2[0] = tempr1[1]
		r2[1] = tempr2[1]
		r2[2] = tempr3[1]
		r2[3] = tempr4[1]
		
		r1[0] = tempr1[0]
		r1[1] = tempr2[0]
		r1[2] = tempr3[0]
		r1[3] = tempr4[0]
		
	return [r1, r2, r3, r4]


def reorientGrid(r1, r2, r3, r4, tempr1, tempr2, tempr3, tempr4, x):
	# rotates grid back to original orientation
	
	if x == 'w':
		r4 = tempr1
		r3 = tempr2
		r2 = tempr3
		r1 = tempr4
	
	elif x == 'a':
		r1[0] = tempr4[0]
		r1[1] = tempr3[0]
		r1[2] = tempr2[0]
		r1[3] = tempr1[0]
		
		r2[0] = tempr4[1]
		r2[1] = tempr3[1]
		r2[2] = tempr2[1]
		r2[3] = tempr1[1]
		
		r3[0] = tempr4[2]
		r3[1] = tempr3[2]
		r3[2] = tempr2[2]
		r3[3] = tempr1[2]
	
		r4[0] = tempr4[3]
		r4[1] = tempr3[3]
		r4[2] = tempr2[3]
		r4[3] = tempr1[3]
	
	elif x == 'd':
		r4[0] = tempr1[3]
		r4[1] = tempr2[3]
		r4[2] = tempr3[3]
		r4[3] = tempr4[3]
		
		r3[0] = tempr1[2]
		r3[1] = tempr2[2]
		r3[2] = tempr3[2]
		r3[3] = tempr4[2]
		
		r2[0] = tempr1[1]
		r2[1] = tempr2[1]
		r2[2] = tempr3[1]
		r2[3] = tempr4[1]
	
		r1[0] = tempr1[0]
		r1[1] = tempr2[0]
		r1[2] = tempr3[0]
		r1[3] = tempr4[0]
	
	return [r1, r2, r3, r4]
	
def nextMove(r1, r2, r3, r4, score, y = None):
	# duplicate values for reordering grid
	# for 'wad', grid rotated and operation performed as if was 's'
	tempr4 = list(r4)
	tempr3 = list(r3)
	tempr2 = list(r2)
	tempr1 = list(r1)
	
	# more duplicate values to check if any changes have occurred
	sempr4 = list(r4)
	sempr3 = list(r3)
	sempr2 = list(r2)
	sempr1 = list(r1)
	
	# user input
	if y == None:
		x = msvcrt.getch()
	else:
		x = y
	
	orientedgrid = orientGrid(r1, r2, r3, r4, tempr1, tempr2, tempr3, tempr4, x)
	r1 = orientedgrid[0]
	r2 = orientedgrid[1]
	r3 = orientedgrid[2]
	r4 = orientedgrid[3]
	

	shiftedgrid = shiftNumbers(r1, r2, r3, r4, score)
	score = shiftedgrid[0]
	r1 = shiftedgrid[1]
	r2 = shiftedgrid[2]
	r3 = shiftedgrid[3]
	r4 = shiftedgrid[4]

	
	tempr1 = list(r1)
	tempr2 = list(r2)
	tempr3 = list(r3)
	tempr4 = list(r4)
	
	
	reorientedgrid = reorientGrid(r1, r2, r3, r4, tempr1, tempr2, tempr3, tempr4, x)
	r1 = reorientedgrid[0]
	r2 = reorientedgrid[1]
	r3 = reorientedgrid[2]
	r4 = reorientedgrid[3]
	
	
	tempr4 = list(r4)
	tempr3 = list(r3)
	tempr2 = list(r2)
	tempr1 = list(r1)
	
	return [r1, r2, r3, r4, tempr1, tempr2, tempr3, tempr4, sempr1, sempr2, sempr3, sempr4, score]
	


def gameOver(score):
	print 'Game over!'
	# locally saving highscore
	if score > highscore:
		highscorefile.truncate()
		highscorefile.write(str(score))
		highscorefile.close()
		print '\nYou beat the high score!'
	return 0
	


while winning == 1:
	
	newgrid = nextMove(r1, r2, r3, r4, score)
	r1 = newgrid[0]
	r2 = newgrid[1]
	r3 = newgrid[2]
	r4 = newgrid[3]
	
	tempr1 = newgrid[4]
	tempr2 = newgrid[5]
	tempr3 = newgrid[6]
	tempr4 = newgrid[7]
	
	sempr1 = newgrid[8]
	sempr2 = newgrid[9]
	sempr3 = newgrid[10]
	sempr4 = newgrid[11]
	
	score = newgrid[12]
	
	# keeps integers evenly spaced
	for s in [tempr1, tempr2, tempr3, tempr4]:
		for i in range(4):
			if len(str(s[i])) == 1:
				s[i] = str(s[i]) + '  '
			elif len(str(s[i])) == 2:
				s[i] = str(s[i]) + ' '
	
	# clears terminal output
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print '\n'
	print ' '.join(str(r) for r in tempr1)
	print ' '.join(str(r) for r in tempr2)
	print ' '.join(str(r) for r in tempr3)
	print ' '.join(str(r) for r in tempr4)
	print '\nScore: %d' % score
	
	#adds random new numbers if grid has changed
	if sempr1 != r1 or sempr2 != r2 or sempr3 != r3 or sempr4 != r4:
		for i in range(4):
			if type(r1[i]) != int:
				r1[i] = random.choice(X2)
	
	tempr4 = list(r4)
	tempr3 = list(r3)
	tempr2 = list(r2)
	tempr1 = list(r1)

	
	for s in [tempr1, tempr2, tempr3, tempr4]:
		for i in range(4):
			if len(str(s[i])) == 1:
				s[i] = str(s[i]) + '  '
			elif len(str(s[i])) == 2:
				s[i] = str(s[i]) + ' '
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print '\n'
	print ' '.join(str(r) for r in tempr1)
	print ' '.join(str(r) for r in tempr2)
	print ' '.join(str(r) for r in tempr3)
	print ' '.join(str(r) for r in tempr4)
	print '\nScore: %d' % score
	print '\nHigh score: %d' % highscore
	
	wgo = nextMove(r1,r2,r3,r4,score,'w')
	ago = nextMove(r1,r2,r3,r4,score,'a')
	sgo = nextMove(r1,r2,r3,r4,score,'s')
	dgo = nextMove(r1,r2,r3,r4,score,'d')
	
	current = [r1, r2, r3, r4]
	for i in range(4):
		if current[i] == wgo[i] and wgo[i] == ago[i] and ago[i] == sgo[i] and sgo[i] == dgo[i]:
			winning += 1
	if winning > 4:
		winning = gameOver(score)
	else:
		winning = 1
	
print 'Do you want to play again?'
	
