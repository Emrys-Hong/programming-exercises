def findKey(dInput, strInput):
	keys = []

	for key in dInput:
		if dInput[key] == strInput:
			keys.append(key)
	return sorted(keys)

dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
print findKey(dInput, 'china') == [5, 20]
print findKey(dInput, 'korea') == []