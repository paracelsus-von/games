import sys
import msvcrt
import random
import os

os.system('cls')

print("  ___   ___  _  _   ___  ")
print(" |__ \ / _ \| || | / _ \  ")
print("    ) | | | | || || (_) | ")
print("   / /| | | |__  __> _ <  ")
print("  / /_| |_| |  | || (_) | ")
print(" |____|\___/   |_| \___/  ")
print("\n")
print("Welcome to 2048. \nUse WASD to move the board. \nPress ENTER to begin. \nHave fun!")

raw_input()

X = [2, 4]
X2 = ['-', '-', '-', '-', 2, 2, 4]

r1 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r2 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r3 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]
r4 = [random.choice(X), random.choice(X), random.choice(X), random.choice(X)]

# clears terminal output
os.system('cls')

print '\n'
print '   '.join(str(r) for r in r1)
print '   '.join(str(r) for r in r2)
print '   '.join(str(r) for r in r3)
print '   '.join(str(r) for r in r4)

for turn in range(1000):
	
	tempr4 = list(r4)
	tempr3 = list(r3)
	tempr2 = list(r2)
	tempr1 = list(r1)

	x = msvcrt.getch()

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

	for c in range(4):
	
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
		
			if r2[c] == r3[c] and type(r3[c]) == int:
				r3[c] *= 2
				r2[c] = r1[c]
			
		elif r2[c] == r3[c] and type(r3[c]) == int:
			r3[c] *= 2
			r2[c] = r1[c]
			r1[c] = '-'
	
		elif r1[c] == r2[c] and type(r2[c]) == int:
			r2[c] *= 2
			r1[c] = '-'
	
	tempr1 = list(r1)
	tempr2 = list(r2)
	tempr3 = list(r3)
	tempr4 = list(r4)
	
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
	
	# clears terminal output
	os.system('cls')
	
	print '\n'
	print ' '.join(str(r) for r in tempr1)
	print ' '.join(str(r) for r in tempr2)
	print ' '.join(str(r) for r in tempr3)
	print ' '.join(str(r) for r in tempr4)
	
	#adds random new numbers
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
	
	os.system('cls')
	
	print '\n'
	print ' '.join(str(r) for r in tempr1)
	print ' '.join(str(r) for r in tempr2)
	print ' '.join(str(r) for r in tempr3)
	print ' '.join(str(r) for r in tempr4)
	
	
