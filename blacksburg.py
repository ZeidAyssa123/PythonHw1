# ECE 2524 Homework 2 Problem 2 Zeid Ayssa

from sys import argv
script, filename = argv
f = open(filename , 'r')

print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
Bburg_String = 'Blacksburg'
for line in f:
           
           city = line.rsplit()[3]
              
           if Bburg_String.lower() == city.lower():
            firstN = line.rsplit()[0]
            lastN = line.rsplit()[1]
            cost = line.rsplit()[2]
            number = line.rsplit()[4]
            print number + ", " + lastN + ", " + firstN + ", " + number
