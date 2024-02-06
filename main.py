"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  
  if n == 1:
    return 1
  else:
    return a * simple_work_calc(n // b, a, b) + n
    
"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO

def work_calc(n, a, b, f):
  if n == 1:
    return 1 
  else:
    return a * work_calc(n // b, a,b,f) + f(n)
    
"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
pass

def span_calc(n, a, b, f):
   return work_calc(n, a, b, f) / a
"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""



def compare_work(work_fn1,work_fn2,sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((n,work_fn1(n),work_fn2(n)))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1,
			span_fn2
			))
	return result





n = 16
a = 2
b = 2
result_1 = work_calc(n, a, b, lambda x: 1)
print(f'W({n}) for a={a}, b={b}, f(n)=1: {result_1}')

# Test with f(n) = log(n)
result_2 = work_calc(n, a, b, lambda x: max(1, int(x.bit_length())))
print(f'W({n}) for a={a}, b={b}, f(n)=log(n): {result_2}')

# Test with f(n) = n
result_3 = work_calc(n, a, b, lambda x: x)
print(f'W({n}) for a={a}, b={b}, f(n)=n: {result_3}')
