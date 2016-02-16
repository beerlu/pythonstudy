def scan(self):
	
	words = self.split(' ')
	v1 = ('verb', 'go')
	v2 = ('verb', 'stop')
	v3 = ('verb', 'kill')
	v4 = ('verb', 'eat')
		
	d1 = ('direction', 'north')
	d2 = ('direction', 'south')
	d3 = ('direction', 'east')
	d4 = ('direction', 'west')
	d5 = ('direction', 'down')
	d6 = ('direction', 'up')
	d7 = ('direction', 'left')
	d8 = ('direction', 'right')
	d9 = ('direction', 'back')
		
	s1 = ('stop', 'the')
	s2 = ('stop', 'in')
	s3 = ('stop', 'of')
	s4 = ('stop', 'from')
	s5 = ('stop', 'at')
	s6 = ('stop', 'it')
	
	noun1 = ('noun', 'door')
	noun2 = ('noun', 'bear')
	noun3 = ('noun', 'princess')
	noun4 = ('noun', 'cabinet')
		
	sentence = [v1, v2, v3, v4,
				d1, d2, d3, d4, d5, d6, d7, d8, d9,
				s1, s2, s3, s4, s5, s6,
				noun1, noun2, noun3, noun4]
	
	match_result = []			
	pair = []			
		
	for word in words:
		for i in range(0,len(sentence)):
			if sentence[i][1] == word:
				pair = sentence[i]
				match_result.append(pair)
		if pair == []:
			if convert_number(word) is not None:
				match_result.append(('number', convert_number(word)))
			else:
				match_result.append(('error', word))		
		pair = []
	return match_result		
			
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None