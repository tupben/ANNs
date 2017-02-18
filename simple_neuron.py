import numpy as np

def sig(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

def relu(x,deriv=False):
	x[x < 0] = .01
	if(deriv==True):
		x*=.3
	return x

def f(x,deriv=False):
	return sig(x,deriv)
	#return relu(x,deriv)

def print_info():
	print "X", X.shape
	print np.round(X,3)
	print
	print "syn0", syn0.shape
	print np.round(syn0,1)
	print
	print "l1", l1.shape
	print np.round(l1,1)
	print
	print "syn1", syn1.shape
	print np.round(syn1.T,1)
	print
	print "l2", l2.shape
	print np.round(l2.T,1)
	print
	print "l2error"
	print np.round(l2error.T,3)
	print
	print "l2delta"
	print np.round(l2delta.T,3)
	print
	print np.mean(np.abs([l2error])), "mean error in ", iter+1, "iterationss"


X = np.array([
	[0,0,1,0],
	[0,1,1,0],
	[1,0,1,0],
	[1,1,1,0]])

y = np.array([[1],[1],[1],[0]])
logicgate = 'NAND \n x x'

np.random.seed(1)
syn0 = 2*np.random.random([4,5])-1
syn1 = 2*np.random.random([5,1])-1

for iter in range(10000):
	l0 = X
	l1 = f(np.dot(l0,syn0)) #+1)
	l2 = f(np.dot(l1,syn1)) #+1)
	l2error = y - l2
	l2delta = l2error*f(l2,deriv=True)
	l1error = np.dot(l2delta, syn1.T)
	l1delta = l1error*f(l1,deriv=True)
	syn1 += np.dot(l1.T,l2delta)
	syn0 += np.dot(l0.T,l1delta)


	if np.mean(np.abs(l2error)) < .05:
		print 'y = ', y
		print 'l2 = ', l2
		print "l2error = ", l2error
		print 'y - l2', y - l2
		break

print_info()

def test(a):
	an1 = f(np.dot(a,syn0)) #+1)
	an2 = f(np.dot(an1,syn1)) #+1)
	return np.round(an2,3)

t = np.array([
	[0,0,0,1],
	[1,1,0,1]
	])

print
print logicgate
print X[0], np.round(test(X[0]),0)[0]==1, test(X[0])
print X[1], np.round(test(X[1]),0)[0]==1, test(X[1])
print X[2], np.round(test(X[2]),0)[0]==1, test(X[2])
print X[3], np.round(test(X[3]),0)[0]==1, test(X[3])
print 'and more...'
print t[0], np.round(test(t[0]),0)[0]==1, test(t[0])
print t[1], np.round(test(t[1]),0)[0]==1, test(t[1])
