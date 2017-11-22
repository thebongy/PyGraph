from decimal import Decimal

import os,math
W, H = 120,50
SCALEx = 0.1
SCALEy = 0.1
os.system("mode %s, %s" % (W+1,H+1))
def cls():
		os.system("cls")

data = [[" " for i in range(W)] for j in range(H)]

X = [SCALEx * i for i in range(0,W)]
Y = [-1+SCALEy * i for i in range(0,H)]

GOP = []
GOPI = []
Clist = ['T','T']

def plotfn():
	prevY = False
	for i in range(len(X)):
		try:
			GOP.append(math.tan(X[i]))
		except:
			GOP.append(1000000000000000.0)
		if i > 1:
			if GOP[-1] > Y[-1] or GOP[-1] < Y[0]:
				Clist.append('D')
			elif GOP[-1] > GOP[-2]:
				Clist.append('>')
			elif GOP[-1] < GOP[-2]:
				Clist.append('<')
			else:
				Clist.append('=')

		t = True
		for j in range(len(Y)):
			if Y[j] == GOP[-1] and t:
				data[H-j-1][i] = "*"
				t = False
			elif GOP[-1] < Y[j] and t and GOP[-1] >= Y[0]:
				if j != 0:
					data[H-j][i] = "*"
				data[H-j-1][i] = "*"
				t = False
				

			if (len(GOP) > 1) and (not t) and (j > 1):
				if (GOP[-1]-GOP[-2]) > SCALEy:
					for g in range(prevY, (prevY+j)/2):
						data[H-1-g][i-1] = "@"
					for g in range((prevY+j)/2, j):
						data[H-1-g][i] = "#"
				elif (GOP[-2]-GOP[-1]) > SCALEy:
					for g in range((prevY+j)/2-1,prevY):
						try:
							data[H-1-g][i-1] = "@"
						except:
							print j,H-1-g,g
							return
					for g in range(j, (prevY+j)/2):
						data[H-1-g][i] = "#"
				prevY = j
				break

plotfn()
print len(Clist)

def display():
		for row in data:
				print ''.join(row)
display()
				

		
	
