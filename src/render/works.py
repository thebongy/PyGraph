import os,math
W, H = 120,50
SCALE = 0.1
os.system("mode %s, %s" % (W+1,H+1))
def cls():
	os.system("cls")

data = [[" " for i in range(W)] for j in range(H)]

X = [SCALE * i for i in range(0,W)]
Y = [SCALE * i for i in range(0,H)]

def plot(x,y):
	x = X.index(x)
	valid_Y = []
	
	if y < Y[0] or y > Y[-1]:
		return
	for i,j in enumerate(Y):
		if j == y:
			data[H-i][x] = "*"
			return i,x
		elif y < j:
			data[H-i][x] = "*"
			data[H-i-1][x] = "*"
			return
			
def display():
	for row in data:
		print ''.join(row)

x = []
delta = 0.1
current = 0
for i in range(100):
	x.append(current)
	current += delta
print x
for i in x:
	plot(i,math.sin(i))

#display()
				
	