# NAME: Spencer Beatty
# ID: 260898452


import doctest
import numpy as np
#GLOBAL VARIABLE
TAB = '\t'
def which_delimiter(string):
    '''
    (str) -> str
    returns the delimiter which is used the most (comma, space, or tab)

    >>> which_delimiter('1 2 3,4')
    ' '
    >>> which_delimiter("3\\t4\\t5,6 7")
    '\\t'
    >>> which_delimiter('cat\\tdog\\trat')
    '\\t'
    >>> which_delimiter('cat,dog rat,mouse')
    ','
    >>> which_delimiter('')
    Traceback (most recent call last):
    AssertionError: does not contain any delimiters
    '''
    delimiter = [TAB, ',' , ' ']
    d ={}
    s = 0
    #checks for each of the delimiters
    for i in delimiter:
        g = 0
        g += string.count(i)
        s += string.count(i)
        d[i] = g
    if s == 0:
        raise AssertionError('does not contain any delimiters')
    #max delimiter is the one that will be chosen.
    p = max(d)

    t = []
    for i in d:
        t.append(d[i])
    value = max(t)
    
    for i in delimiter:
        if d[i] == value:
            return i

def stage_one(input_file, output_file):
    '''
    (str, str) -> int
    takes two inputs and opens the first one input_filename, makes changes to the file
    then puts the new changes into file output_filename.
    encoding  = 'utf-8' to all lines when opening to read because of the french.
        Changes include:
        - .changes the most common delimiter to tab
        -  changes all text to uppercase
        -  change any / or . into a hyphen
    returns how many lines were written in output_filename
    >>> stage_one('shortA4.txt', 'short_stage1.tsv')
    10

    >>> stage_one('textA4.txt', 'long_stage1.tsv')
    3000

    >>> stage_one('edge1.txt', 'edge1_stage1.tsv')
    3000

    >>> stage_one('edge2.txt', 'edge2_stage1.tsv')
    3000
    '''
    #opens the file
    file = open(input_file, 'r', encoding = 'utf-8')
    list_file = (file.readlines())
    file.close()
    t = []
    #runs a for loop and checks for lower case as well as upper case and
    # adds tabs and '-'
    for i in list_file:
        delimiter = (which_delimiter(i))
        s = ''
        for j in i:
            if j.islower():
                 s += j.upper()
            elif j is delimiter:
                s += TAB
            elif j is '/' or j is '.':
                s += '-'
            else:
                s += j
        t.append(s)
    
    out_file = open(output_file, 'w', encoding = 'utf-8')
    counter = 0
    for i in t:
        (out_file.write(i))
        counter += 1
    out_file.close()

    return counter

    
def stage_two(input_file, output_file):
    '''
    (str, str) -> int
    this will open the input_file and read the file line by line, add the same
    French encoding, and be making changes to the file
        Changes include:
        - all lines have 9 columns
        - any line with more than 9 columns must be cleaned
    >>> stage_two('short_stage1.tsv', 'short_stage2.tsv')
    10

    >>> stage_two('long_stage1.tsv', 'long_stage2.tsv')
    3000

    >>> stage_two('edge1_stage1.tsv', 'edge1_stage2.tsv')
    3000

    >>> stage_two('edge2_stage1.tsv', 'edge2_stage2.tsv')
    4000
    '''
    file = open(input_file, 'r', encoding = 'utf-8')
    list_file = (file.readlines())
    file.close()
    
    #check for three cases, case 1 if the problem is inbetween not applicable, case 2 if the problem is at the end where the letter has been pushed
    # case 3 if the problem is at the end but is instead that the french comma has been turned into a tab.
    t = []
    # after file is created iterates through the list and checks that each line has 8 tabs ('\t')
    for i in list_file:

        string = ''
        counter = 0
        if i.count(TAB) != 8:
            for pos, j in enumerate(i):
                #each time the for loop encounters a tab it ups the counter so we can check the specific instances.
                if j == TAB:
                    counter += 1
                    if counter == 6 and (not(i[pos-1].isdigit())):
                        string += ' '
                    if counter == 8 and (i[pos+1] == 'A'):
                        string += ' '
                    elif counter == 8 and (i[pos+1].isdigit()):
                        string += ','

                    else:
                        string += TAB
                else:
                    string += j
            
            t.append(string)
        
        #this is the case in which there were no problems with I
        else:
            t.append(i)

    for i in t:
        if i.count(TAB) != 8:
            print(i)
            #raise AssertionError('there are some edge cases you have not covered')


    new_file = open(output_file, 'w', encoding = 'utf-8')
    line_counter = 0
    for i in t:
        new_file.write(i)
        line_counter += 1
    new_file.close()
    return line_counter
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    doctest.testmod()
