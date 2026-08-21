'''Exercises from Python Programming Exercises, Gently Explained,
henceforth, referred to as PPEGE.

Starting with Exercise #39, Collatz sequence'''

collatz = [] #'''sets the base number to null'''

def getCollatz(a):

    col = int(a)

    '''The following gives the Collatz code.'''

    if col != '':

        collatz.append(col)
        
        while col>2:

            if col%2 == 0:
                col = int(col//2)

            elif col%2 == 1:
                col = (3*col) + 1

            collatz.append(col)

            next

        collatz.append(1)

##    else:
##        '''This ensures no errors arise from having no seed'''
##        collatz = None

'''The main code begins here.'''

a = input('Please input seed.\n')

getCollatz(a)

print('The seed',a,'leads to the Collatz sequence\n',collatz)
