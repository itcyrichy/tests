import numpy
import math
import pytest

# pi, sqrt, pow, hypot

def pi():
   return math.pi

def root(x):
   return math.sqrt(x)

def stepen(x,y):
   return math.pow(x,y)

def hypo(x,y):
   return math.hypot(x,y)

def test1():
   assert type(pi()) == float

def test2():
   assert root(9) == 3

def test3():
   assert stepen(9, 2) < 100

def test4():
   assert hypo(2, 3)

def test5():
   assert len(list(filter(lambda x: x<3,[1,2,3,4,5]))) == 2

def test6():
   assert sum(list(map(lambda x: x**2,[1,2,3,4,5]))) > 100

def test7():
   assert sorted([5,6,3,21,9],reverse=True)[0] == 21