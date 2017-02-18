import numpy as np


def sig(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

def relu(x,deriv=False):
	x[x < 0] = .01
	if(deriv==True):
		x*=1
	return x

def f(x,deriv=False):
	return sig(x,deriv)
	#return relu(x,deriv)



X = np.array([
[0,0,1],
[0,1,1],
[1,0,1],
[1,1,1]
	])

y = np.array([[0,0,1,1]]).T



np.random.seed(5)
syn0 = 2*np.random.random((3,1))-1

for iter in range(500):
	l0 = X
	l1 = f(np.dot(l0,syn0))
	error = y-l1
	change = error * f(l1,True)
	syn0 += np.dot(l0.T,change)

	if iter%10==9 or iter==0:
		print np.round(syn0.T,5), iter+1

def test(a):
	return f(np.dot(a,syn0))


print
print "syn0"
print np.round(syn0.T,2)
print
print "f(X dot syn0)"
print np.round(l1,2)
print
print "error"
print np.round(y-l1,2)
print
for a in X:
	print a, test(a)