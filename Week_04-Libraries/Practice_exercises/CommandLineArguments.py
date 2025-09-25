import sys #module that allows us to take arguments at the command line

#argv is a list within the sys module that records what the user typed on the command line.
# sys.argv[0] is the file name
#ex: python CommandLineArguments.py [Enter]
if len(sys.argv) < 2:
    sys.exit("Too few arguments") #Error cause there is only 1 argument
elif len(sys.argv) > 2: #ex: python CommandLineArguments.py Paulito Nguyen
    sys.exit("Too many arguments") #Error cause there are 3 arguments

print("hello, my name is", sys.argv[1])
#ex: python CommandLineArguments.py Paulito
#ex: hello, my name is Paulito