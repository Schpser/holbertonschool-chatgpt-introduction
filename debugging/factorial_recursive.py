#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculate the factorial of a non-negative integer.
	
	The factorial of a number n is the product of all positive integers
	from 1 to n. This function uses a recursive approach.
	
	Parameters:
	n (int): A non-negative integer for which to compute the factorial
	
	Returns:
	int: The factorial of the input number n
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
