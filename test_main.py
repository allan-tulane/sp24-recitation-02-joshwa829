from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 210
  assert simple_work_calc(20, 3, 2) == 6880
assert simple_work_calc(30, 4, 2) == 121810
assert simple_work_calc(5, 2, 3) == 33
assert simple_work_calc(15, 3, 2) == 5238  
assert simple_work_calc(25, 4, 3) == 378013 
def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 210
	assert work_calc(20, 1, 2, lambda n: n*n) == 6880
	assert work_calc(30, 3, 2, lambda n: n) == 121810


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    def work_fn1(n):
      return work_calc(n, 2, 2, lambda x: x**2)
    def work_fn2(n):
      return work_calc(n, 3, 2, lambda x: x**3)
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
    print(res)

	
def test_compare_span():
  result_comparison = compare_span(
      lambda n: span_calc(n, 2, 2, lambda x: x**2),
      lambda n: span_calc(n, 3, 2, lambda x: x**3))
