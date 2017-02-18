
import numpy as np


def sig(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

def relu(x,deriv=False):
	x[x < 0] = .001
	if(deriv==True):
		x= 1*(x>0)
	return x

def f(x,deriv=False):
	#return sig(x,deriv)
	return relu(x,deriv)



X = np.array([
[0,0,1],
[0,1,1],
[1,0,1],
[1,1,0]
	])

y = np.array([[0,0,1,1]]).T



np.random.seed()
syn0 = (2*np.random.random((3,1)))-1

for iter in range(1000):
	l0 = X
	l1 = f(np.dot(l0,syn0))
	error = y-l1
	change = error * f(l1,True)
	syn0 += np.dot(l0.T,change)

	if iter%10==9 or iter==0:
		print np.round(syn0.T,5), iter+1

	if np.mean(np.abs(error)) < .05:
		print 'got it!'
		break

def test(a):
	return f(np.dot(a,syn0))


print
print "syn0"
print np.round(syn0.T,2)
print
print "f(X dot syn0)"
print np.round(f(np.dot(X,syn0)),2)
print
print "error"
print np.round(y-f(np.dot(X,syn0)),2)
print
for a in X:
	print a, test(a)