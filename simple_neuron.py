import numpy as np
import math

def relu(x,deriv=False):
	if deriv:
		return 0.2
	return np.maximum(0,x)

def sig(x,deriv=False):
	if deriv:
		return x*(1-x)
	return 1/(1 + np.exp(-x))

def f(x,deriv=False):
	return relu(x,deriv)
	#return sig(x)

X = np.array([	[0,0],
				[0,1],
				[1,0],
				[1,1]		])
y = np.array([	[0,1,1,0]	]).T
l0 = np.copy(X)
solved = False

def run_network(d = 50):
	np.random.seed()
	syn0 = 2*(np.random.random((2,d))-.5)
	syn1 = 2*(np.random.random((d,1))-.5)
	bias0 = np.zeros((1,d))
	bias1 = np.zeros((1,1))

	for iters in xrange(10000):
		# Forward
		l1 = f(np.dot(l0,syn0)+bias0)
		l2 = f(np.dot(l1,syn1)+bias1)

		# Back
		error = y - l2
		l2_delta = f(l2,True)*error
		l1_delta = f(l1,True)*np.dot(l2_delta,syn1.T)
		syn1 += np.dot(l1.T,l2_delta)
		syn0 += np.dot(l0.T,l1_delta)
		bias1 += np.array([np.sum(l2_delta, axis=0)])
		bias0 += np.array([np.sum(l1_delta, axis=0)])
		mean_err = np.mean(np.abs(error))
		if mean_err<0.01:
			print 'solved!   iters:', iters
			print 'error :\n', error
			return iters
	

run_network()

# def forward(l0,syn0,syn1):
# 	l1 = f(np.dot(l0,syn0) + bias0)
# 	l2 = f(np.dot(l1,syn1) + bias1)
# 	return l2

# for dim in [25,30,35,40,45,50]:
# 	epochs = []
# 	for b in range(50):
# 		output = run_network(dim)
# 		if output<'':
# 			epochs.append(output)
# 	print dim, 'dimensions, ', sum(epochs)/len(epochs), 'iters'
