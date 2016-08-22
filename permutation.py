#n!/(m-n)!

def permutation(n,m):
	num = math.factorial(n)
	den = math.factorial(m-n)
	
	return float(num / den)
	
