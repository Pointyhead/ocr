# coding=UTF-8
from __future__ import division
from nltk import metrics
import os, math

# ABBYY will save utf-8 text files with a Byte Order Mark.
ocr = "C:\\Users\\Pointyhead\\Documents\\nybg\\ocr\\"
lines = "C:\\Users\\Pointyhead\\Documents\\nybg\\lines.txt"
dir_ocr = os.listdir(ocr)
output = "C:\\Users\\Pointyhead\\Documents\\nybg\\processed.txt"
punct = ".!¡:;?\'\"\]\|—“°\¿[’»«}{()*• \t~■£€„&-=+_#@®©$%*,<>/”^".decode('utf-8')

class process:
    def __init__(self):
        pass
    
    def depunc(self, linea):
        self.linea = linea
        for t in linea:
            if t in punct:
                linea = linea.replace(t, '')
        return linea.rstrip('\n').lower()

p = process()

def chug():
    for title in dir_ocr:
        with open(ocr + title, 'r') as o_open:
            with open(lines, 'r') as l_open:
                #lists of lines for each doc.
                o_open_r = o_open.readlines()
                l_open_r = l_open.readlines()
                tot_o_line = len(o_open_r)
                tot_l_line = len(l_open_r)
                o_line = 0
                for o in o_open_r:
                    #strip ocr lines of punctuation/whitespace
                    d={}
                    o_1 = p.depunc(o.decode('utf-8'))
                    l_line = 0
                    o_line += 1
                    for l in l_open_r:
                        #strip 'known' lines of punctuation/whitespace
                        l_1 = p.depunc(l.decode('utf-8'))
                        #ignore ocr lines with few characters, still count the line thought
                        if len(o_1) < 4:
                            l_line += 1
                        #don't compare ocr lines less than half or over twice the length of the reference 'known' line(does this improve performance?)    
                        elif len(o_1) < .5*len(l_1) or len(o_1)> 1.5*len(l_1):
                            l_line +=1
                        #compare ocr and known lines, get a similarity value between 0(not similar) and 1 (exact match), insert line pairs into dictionary
                        else:
                            l_line += 1
                            x = len(o_1)+len(l_1)
                            dist = (x - metrics.edit_distance(o_1, l_1))/(x)
                            d['"'+str(title + '| '+ str(o_line)+ '","' +o.rstrip('\n') +'","'+ 'line: ' + str(l_line)+'","'+ l.rstrip('\n')+'"')] = dist
                            #keep the top score in the dictionary for each ocr line. Append to file.
                    if len(d) >0 and (max(d.values())) > .85:
                        m = d.keys()[d.values().index(max(d.values()))]
                        f = open(output, 'a')
                        f.write(str(m) + ',' +str((max(d.values())))+'\n')
                        print str(m).decode('utf-8')+',', (max(d.values()))
            l_open.close()
        o_open.close()
    f.close()
chug()                    
                
