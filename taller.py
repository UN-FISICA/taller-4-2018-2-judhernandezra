#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import math



def adelante(a,x):
	return (f(x+a.dx)-f(x))/a.dx
		
def central(a,x):
	return (f(x+a.dx/2)-f(x-(a.dx/2)))/a.dx
				
def extrapolada(a,x):
	return ((4*(f(x+a.dx/4)-f(x-a.dx/4))/(a.dx/2))-((f(x+a.dx/2)-f(x-a.dx/2))/a.dx))/3
	
def segunda(a,x):
	return (f(x+a.dx)+f(x-a.dx)-2*f(x))/(a.dx**2)	


class Derivada:
	def __init__(self,metodo="adelante",dx=0.001):
		
		self.metodo=metodo
		self.dx=dx


	def calc(self,x):
		return self.metodo(self,x)
	
	def __str__(self):
		return str(self.calc)

		

if __name__=="__main__":
	x=10
	
	f=lambda x:math.sin(x)/math.exp(x)
	
	a=Derivada(adelante,0.000001)
	print "Adelante sen(x)/exp(x) x=10 ",a.calc(x)
	a=Derivada(central,0.000001)
	print "Central sen(x)/exp(x) x=10 ",a.calc(x)
	a=Derivada(extrapolada,0.000001)
	print "Extrapolada sen(x)/exp(x) x=10 ",a.calc(x)
	a=Derivada(segunda,0.000001)
	print "Segunda sen(x)/exp(x) x=10 ",a.calc(x)
	
	
