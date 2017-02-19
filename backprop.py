
import numpy as np


def sig(x,deriv=False):
	if(deriv==True):
		return sig(x,deriv=False)*(1-sig(x,deriv=False))
	return 1/(1+np.exp(-x))

def relu(x,deriv=False):
	if(deriv==True):
		return .1
	return np.maximum(x,0)

def f(x,deriv=False):
	#return sig(x,deriv)
	return relu(x,deriv)



X = np.array([
				[0,0],
				[0,1],
				[1,0],
				[1,1]
			])

y = np.array([[0,0,1,1]]).T


np.random.seed()
syn0 = (2*np.random.random((2,1)))-1

#print 'syn0 = ', syn0
#syn0 = np.array([[1.],[0],[0]])


for iter in range(1000):
	if iter == 0: 
		print np.round(syn0.T,3), iter+1
	l0 = X
	l1 = f(np.dot(l0,syn0))
	error = y-l1
	change = error * f(l1,True)
	if iter%10==9 or iter<10:
		print 'syn', np.round(syn0.T,3), 'err', np.round(error.T,2), 'chg', np.round(change.T,2), 'ch!', np.dot(l0.T,change).T, 'iter',iter+1
	syn0 += np.dot(l0.T,change)


	#if np.mean(np.abs(error)) < .05:
	#	print np.round(syn0.T,5), iter+1
	#	print 'got it!'
	#	break

print 'syn0 = ', syn0.T

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
	print a, np.round(test(a),3)