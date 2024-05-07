def subs(s, t):
	return [
		i + 1
		for i, _ in enumerate(s[:-len(t)])
		if s[i:i+len(t)] == t
	]