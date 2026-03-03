#ADD A MEDIUM AND LINKEDIN LINK ON THE DOCTSTRING
#SOLVE FIZZBUZZ USING A DICTIONARY

"""
This module provides common beginner friendly functions ,
Some of the functions in this module are not optimized 
and should not be used without caution in production.

This modules also serves as a memorandum for most common python quizzes
and where possible I also provide tips ,tricks and alternatives.
For more details on this kindly visit my medium account where I explain 
concepts in detail *add medium link and linkedin link here*.

it is very important to know that
the solutions provided may not be the only way since there are countless ways to kill
a cat ,and it is also worth noting that most solutions will not cover all edge cases are not
tested for production.Though were possible I also try to provide optimimized alternatives ,
pseudocode and tips in respective function docstrings.

NB:I tried to avoid the usage of builtin methods functions where possible 
since this module tend to use overkill solutions removing abstraction
thus allowing users to practice loops,if statements and other programming concepts,
though it is advised that you use them in production.

No LLMs were used in writting this doc or any of the code in this module,
all material is created by me. 
"""

def get_largest_n(numbers):
	"""
	This function finds the largest number from
	a list of numbers (numbers).

	--> Initialize the largest_n variable to 0,
	--> then loop over numbers 
		--> if number > than the largest_n reasign largest_n to number,
		--> if not, skip then repeat.
	--> Return the largest_n at loop exit.

	"""
	largest_n = 0
	for number in numbers:
		if number > largest_n:
			largest_n = number
	return largest_n

def get_largest_n_two(numbers):
	"""
	This function find the largest number ,an alternative to
	get_largest_n()

	--> Initialize left = 0 and right = 1
	--> loop
		--> Then compare numbers at both indexes 
		--> if number at left > number at right index 
			--> increment right by 1
		--> else
			--> increment left by 1
		--> if either left or right values > length of numbers(has reached the end)
			--> stop loop
	--> if right > left return numbers[left] else numbers[right]
	
	This uses manual indexing and it is slower than get_largest_n()
	"""
	left = 0
	right = 1
	while True:
		if left >= len(numbers) or right >= len(numbers):
			break
		elif numbers[left] > numbers[right]:
			right += 1
		else:
			left += 1
	return numbers[left] if right > left else numbers[right]

def get_word_len(wordlist):
    """
    This functions takes in a list of words and returns 
    the length of each word. 

    --> Loop over a list of words 
	--> For every word set count = 0
		--> The loop over its characters incrementing count
		--> Then add the word count to result list.
	--> Then return the results list.

	This function is slow and can be achieved in less code
	and fast speed by the alternative [len(char) for char in wordlist]
    """
    results = []
    for word in wordlist:
        counter = 0
        for char in word:
            counter += 1
        results.append(counter)
    return results

def get_even_num(numbers):
	"""
	This function takes in a list of numbers and return a 
	only even numbers.

	--> Loop over numbers
		--> if number is not divided by 2 is not equal to 0
			--> skip the loop
		--> else
			--> append the number to the result list
	--> return the results list
	
	The same operation can be achieved at even faster speed by
	the alternatives [number for number in numbers if number % 2 == 0] ,
	list(filter(lambda x : x % 2 == 0 ,[1,2,3,4])) and other similar patterns

	"""
	results = []
	for number in numbers:
		if number % 2 != 0:
			continue
		else:
			results.append(number)
	return results


def reverse_str(str):
	"""
	This function ,takes in a string and return it reversed 

	--> loop over str indexes(begin at the end of str,end at 0 ,decrement by 1)
		--> add each character corresponding to index to the results list
	--> return the joined result list.

	The same effect can easily be achieved by the alternative s[::-1]
	CAUTION:The str local name shadows the builtin str name.

	"""
	results = []

	#start range at the end of a string minus 1 since string index start at 0
	#end at 0,though since upper bound is exclusive,specify upper bound as -1 
	#decrement by -1 from end of string until 0
	for s in range(len(str) - 1,-1 ,-1):
		results.append(str[s])

	return ''.join(results) 


def reverse_str_two(str):
	"""
	An alternative to the reverse_str which both use manual indexing
	(see reverse_str_two docs)

	--> Loop until then end of string(starting from the end of list)
		--> decrement str len by 1
		--> add the character corresponding to that index to results
	--> return the joined result list
	
	"""
	str_len = len(str)
	results = []
	while str_len > 0:
		str_len -= 1
		results.append(str[str_len])
	return ''.join(results)

	#str_len = len(str)
	#while (str_len := str_len -1) > 0:print(s[str_len])

def is_palindrome(word) :
	"""
	This function checks if a word is a palindrome
	The first part follows the reverse_str(),
	--> reverse the word then compare it with the original word
	--> if the equality comparison yield true then is palindrom else is not

	Though the problem can easily be solved with the ternary -->>
	'palindrome' if word == word[::-1] else 'not palindrome'

	reverse_str() could've been used to reduce redundancy though i strive to 
	keep every function indepedent of the other since all functions
	in this dont work together to form a larger system.They are just
	individual quizz functions.

	"""
	results = []
	for i in range(len(word) - 1,-1,-1):
		results.append(word[i])
	if ''.join(results) == word:
		return 'is palindrome'
	else:
		return 'is not palindrome'

def sum_digit(number):
	""" 
	This function return the sum of digits of a number e.g 123 -->> 6

	--> find string representative of the number ,then create a new list object using that string
	--> loop over the list ,
		--> then reconvert the str digit back to num
		--> increment the number to the sum variable
	--> return the sum variable

	Can also be solved by the alternative sum([int(n) for n in list(str(num))]) or by an overkill
	functools.reduce(lambda x ,y: x + y,[int(n) for n in list(str(num))]) or other similar coding patterns
	The problem can also be solved without typecasting by using other mathematical functions
	which tend to confuse most programmers and generally an overkill to this problem.

	CAUTION:local sum name is shadowing the builitin sum name
	"""
	sum = 0
	for n in list(str(number)):
		sum += int(n)
	return sum

def factorial(num):
	""" 
		This functions find the factorial of a number ,n!

		--> loop over a range of a number(start from 1 until the end of number)
			--> multiply the current number by the results variable
		--> return the return results

		This function can also be achieved by an alternative functools.reduce(lambda x,y: x * y ,range(1,5 + 1)),
		and other similar coding patterns
		Math module in python also provide a factorial function ,which is optimized.
	"""
	result = 1
	for n in range(1,num + 1):result *= n
	return result


def fizzbuzz(num):
	"""
	This function checks if number is fizz ,buzz or fizbuzz
	"""
	if num % 2 == 0 and num % 3 == 0:
		return 'fizzbuzz'
	elif num % 2 == 0 :
		return 'fizz'
	elif num % 3 == 0:
		return 'buzz'
	else:
		return 'no fizzbuzz'
	
def unique_char(word):

	"""
	Function takes in a word and checks if it has unique characters
	'text' --> no uniques chars
	'code' --> has unique chars
	
	--> Uses manual indexing
	--> for every character index
		-->loop on top of of every other character index
			--> if both character indexes are at the same spot 
					--> skip
			--> if both indexes link to the same char
					--> word has no unique chars
			--> else
					--> word has unique chars

	This can also be solved by the alternative 'unique' if len(n) == len(set(n)) else 'not unique'
	
	"""
	#if length of word is 1 ,then by default is unique
	if len(word) == 1:
		return 'has unique character(one character word)'
	
	for i in range(len(word)):
		for j in range(len(word)):
			if i == j:
				continue
			elif word[i] == word[j]:
				return 'has no unique characters'
			else:
				return 'has unique characters'

def word_count(word ,sentence):
	"""
	Return how many occurences a word appears in a sentence

	-->replace all the occurences of the word in the sentence with x
	-->then count how many times x appears in the sentence.

	This can also be achieved by the str.count method
	"""
	#This code is buggy also count subwords e.g 'name' in 'surname' is also counted.
	#This bug can be solved in various words using regex patterns
	# though due to complexity ,they are omitted here.

	count = 0
	s = sentence.replace(word,'x')

	for w in s:
		if w == 'x':
			count += 1
	return f"word '{word}'' appears {count} times"


