# ECE 2524 Homework 2 Problem 1 Zeid Ayssa

with open('/etc/passwd', 'r') as f:
    for line in f:
    
        arg1 = line.split(':',6)[0]
        arg2 = line.split(':',6)[6]
    
        
        print arg1 + "      "  +arg2
