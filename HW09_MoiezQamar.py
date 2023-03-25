# Name
#CS 100 Section 021
#HW 09, November 9, 2021

#----------PROBLEM 1:

def file_copy(in_file, out_file):
    r = open(in_file,'r')
    w = open(out_file, 'w')
    w.write(r.read())
    r.close()
    w.close()


#----------PROBLEM 2:

def file_stats(in_file):
    r = open(in_file, 'r')
    line_counter=0
    word_counter=0
    char_counter=0
    for line in r:
        line_counter+=1
        word_counter+=len(line.split())
        for t in line:
            char_counter+=1
    print("Lines:",line_counter)
    print("Words:",word_counter)
    print("Chars:",char_counter)



#----------PROBLEM 3:

import string 

def repeat_words(in_file, out_file): 
    rep_word=[]
    x=[]
    r = open(in_file,'r')
    w = open(out_file, 'w')
    for line in r: 
        rep_word=[]


        x=line.lower().split()
        for t in x:
            x[x.index(t)]=t.strip(string.punctuation)
        
        for i in x:
            if x.count(i)>1:
                if i in rep_word:
                    continue
                else:
                    rep_word.append(i)
        for y in rep_word:
            w.write(y+" ")
        w.write('\n')