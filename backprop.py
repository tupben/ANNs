import numpy as np

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


X = np.array([
				[0,0],
				[0,1],
				[1,0],
				[1,1]		])

y = np.array([	[0,0,0,1]	]).T
l0 = X

def runnetwork(print_stats=False):
	np.random.seed()
	syn0 = (2*np.random.random((2,1)))-1
	bias0 = np.zeros((1,1))

	for iter in range(10000):
		l1 = f(np.dot(l0,syn0) + bias0)
		error = y-l1
		change = error * f(l1,True)
		syn0 += np.dot(l0.T,change)
		bias0 += np.array([np.sum(change, axis=0)])

		if np.mean(np.abs(error)) < .05:
			if print_stats:
				print 'got it!', iter+1, 'iters'
				print 'syn0\n',np.round(syn0,5)
				print bias0
			return iter+1

runnetwork(True)

# for z in range(4):
# 	blist = []
# 	for b in range(500):
# 		output = runnetwork()
# 		if output<'':
# 			blist.append(output)
# 	print z,'dimensions, ', sum(blist)/len(blist), 'iters'
