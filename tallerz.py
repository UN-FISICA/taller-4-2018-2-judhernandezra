#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import math
from scipy import optimize

def newton(a,vi):
	i=1
	while (abs(f(vi))>=a.error):
		x1=vi-f(vi)/Df(vi)
		vi=x1
		i=i+1
	
		if i==a.max_iter:
			break
	print vi


def bisectriz(a,vi):
	i=1
	while (abs(f((vi[0]+vi[1])/2))>=a.error):
		c=(vi[0]+vi[1])/2

		if f(vi[0])*f(c)<0:
			vi[1]=c
			i=i+1
			if i==a.max_iter:
				break
		elif f(vi[0])*f(c)>0:
			vi[0]=c
			i=i+1
			if i==a.max_iter:
				break

	print c

def interpolacion(a,vi):
	i=1
	while(abs(f((f(vi[1])*vi[0]-f(vi[0])*vi[1])/(f(vi[1])-f(vi[0]))))>=a.error):
		c=(f(vi[1])*vi[0]-f(vi[0])*vi[1])/(f(vi[1])-f(vi[0]))
		
		if f(c)>0:
			vi[1]=c
			i=i+1
			if i==a.max_iter:
				break
		elif f(c)<0:
			vi[0]=c
			i=i+1
			if i==a.max_iter:
				break
	print c	
	
	
def newtonsp(a,vi):
	return optimize.newton(f,vi)	
	
def fsolvesp(a,vi):
	return optimize.fsolve(f,vi)
	
def brentqsp(a,vi):
	return optimize.brentq(f,vi[0],vi[1])
	

class Zeros:
	def __init__(self,metodo="newton",error=1e-4, max_iter=100):
		
		self.metodo=metodo
		self.error=error
		self.max_iter=max_iter

	def zero(self,vi):
		return self.metodo(self,vi)
	
	def __str__(self):
		return str(self.zero)
		
		
		
if __name__=="__main__":
	
	vi=1.5
	f= lambda x:math.log(x)
	Df= lambda x:1/x
	a=Zeros(newton,1e-7,20)
	print "Newton ln(x) ",a.zero(vi)
	
	vi=[0.8,1.4]
	a=Zeros(bisectriz,1e-7,20)
	print "Bisectriz ln(x) ",a.zero(vi)
	
	vi=[0.8,1.4]
	a=Zeros(interpolacion,1e-7,20)
	print "Interpolación ln(x) ",a.zero(vi)
	
	vi=1.5
	a=Zeros(newtonsp,1e-7,20)
	print "Newton-sp ln(x) ",a.zero(vi)
	
	vi=1.5
	a=Zeros(fsolvesp,1e-7,20)
	print "fsolve-sp ln(x) ",a.zero(vi)
	
	vi=[0.8,1.4]
	a=Zeros(brentqsp,1e-7,20)
	print "brentq-sp ln(x) ",a.zero(vi)	
			
		
		
