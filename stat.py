# ECE 2524 Homework 2 Problem 3 Zeid Ayssa
from sys import argv
script, filename = argv
f = open(filename , 'r')

#Initialize Variables
total = 0
avg = 0
Max = 0
flag = 1

for line in f:
           firstN = line.rsplit()[0]
           lastN = line.rsplit()[1]
           cost = line.rsplit()[2]
           number = line.rsplit()[4]
           
           total = float(cost) + total
           acounter = avg + 1
           avg = total / acounter
                    
           if flag == 1:
            Min= cost
            flag = 0
            
            if cost > Max:
                Max = cost
                string = "Maximum amount owed = " + Max+ " by " + lastN
           
           if cost < Min:
                Min = cost
                string2 = "Minimum amount owed = " + Min+ " by " + lastN

print "ACCOUNT SUMMARY"          
print "Total amount owed = %s" % total
print "Average amount owed = %s" % avg
print string
print string2
