def hamming_distance(s1, s2):
	"""Calculating hamming distance of two strings with equal length
	"""
	return sum( 1 for c1, c2 in zip(s1, s2) if c1 != c2 )