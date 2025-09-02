#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculate the factorial of a non-negative integer n using recursion.

	The factorial of n (noted n!) is defined as:
	  - 0! = 1
	  - n! = n × (n-1)! for n > 0

	Args:
		n (int): A non-negative integer.

	Returns:
		int: The factorial of n.

	Raises:
		RecursionError: If n is too large and exceeds the maximum recursion depth.
		ValueError: If n is negative.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

if __name__ == "__main__":
	# Read an integer from command line arguments
	# Example: ./factorial_recursive.py 4 → prints 24
	f = factorial(int(sys.argv[1]))
	print(f)
