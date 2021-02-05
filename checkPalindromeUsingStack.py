class Node:
	'''Node object to store data and reference to next'''
	def __init__(self, data):
		self.data = data
		self.next = None
		
class stack:
	'''Stack data structure that adhere to FILO philosphy'''
	def __init__(self):
		self.top = None
		self.size = 0

	def push(self, data):
		'''Put data onto the top of the stack'''
		node = Node(data)   # Make a new node with the data
		if self.top:    # If there are any items on the stack...
			node.next = self.top    # Set the next param to the top of the stack
			self.top = node     # Set the top of the stack to the new node
		else:
			self.top = node # Make the top of the stack the new node
		self.size += 1  # Increase the size of the stack
    
	def pop(self):
		if self.top:    # If the stack is not empty
			data = self.top.data # Get the data off the top
			self.top = self.top.next if self.top.next else None # Set the top to next node down
			self.size -= 1  # Decrease the stack size 
			return data
		return '' # Return nothing if stack is empty
	


def isPalindrome(word):
    s = stack()
    word=str.lower(word).strip()

    for character in word:
        s.push(character)
		
    reversed_word=''
	
    while (s.top is not None):
        reversed_word = reversed_word + s.pop()

    if word==reversed_word:
        print(word.strip()+" IS a palindrome\n")
    else:
        print(word.strip()+" is NOT a palindrome\n")





file = open("d:\\checkPalindrome.txt")
wordlist=list(file.readline().split(','))
	
for i in wordlist:
    isPalindrome(i)


'''
Morning, Level, Madam, First, Noon, Racecar, Extra, Radar, Refer, Repaper, Fill, Sagas, Stats, Tenet, Status, Wow
'''
