#! /usr/bin/env python

for i in range(10):
	if i<=4 or i>=7 :
		print ("\033["+str(i)+";m"+"style "+str(i)+"\033[0m\n")
