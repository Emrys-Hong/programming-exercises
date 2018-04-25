#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

from libdw import sm

class SpellCheckSM(sm.SM):
	startState = 'new word' # startState new word to accept input

	def getNextValues(self, state, inp):
		consonants = 'kgstdnhbmr'
		vowels = 'aeiou'

		nextState = ""
		outp = ""
		if state == 'new word':
			if inp.isspace(): # transition E10
				nextState = 'new word'
				outp = ''
			elif inp in consonants: # transition A1
				nextState = 'consonant'
				outp = ''
			else: # transition E8
				nextState = 'error'
				outp = ''
		elif state == 'consonant':
			if inp.isspace(): # transition E4
				nextState = 'new word'
				outp = 'error'
			elif inp in vowels: # transition A2
				nextState = 'vowel'
				outp = ''
			else: # transition E5
				nextState = 'error'
				outp = ''
		elif state == 'vowel':
			if inp.isspace(): # transition A3
				nextState = 'new word'
				outp = 'ok'
			else: # transition E6
				nextState = 'error'
				outp = ''
		elif state == 'error':
			if inp.isspace(): # transition E7
				nextState = 'new word'
				outp = 'error'
			else: # transition E9
				nextState = 'error'
				outp = ''

		return (nextState, outp)


# print 'Test case A'
# a = SpellCheckSM()
# line = 'a si tu ne mai me pas je '
# print a.transduce(line)

# print 'Test case B'
# a = SpellCheckSM()
# line = 'hi ka ru no de '
# print a.transduce(line)
        
# print 'Test case C'
# a = SpellCheckSM()
# line = 'mu '
# a.transduce(line,verbose=True)