import csv
import os

'''
We intended to classify only 4 types of signals, 
where the normal beats are classified as 1, 
the atrial premature beat as 3 and the ventricular premature beat as 4
while all the other beats are classified as 2.
'''

dict= {'N':1,'L':2,'R':2,'B':2,'A':3,'a':2,'J':2,'S':2,
'V':4,'r':2,'F':2,'e':2,'j':2,'n':2,'E':2,'/':2,
'f':2,'Q':2,'~':2,'':2,'':2}

def normalToDict(pathX,PathY):
  for i in range(224, 225):


    path = pathX
    name =  path + str(i) + 'test.csv'

    if (os.path.exists(name) == True):

        path3 = pathY
        name3 = path3 + str(i) + '.csv'
        with open(name, 'r') as f:
            rdr = csv.reader(f, delimiter = ',')
            with open(name3, 'w') as l:
                wtr2 = csv.writer(l, delimiter = ',')
                for r in rdr:
                    for r in rdr:
                        if (r[1]=='~' or r[1]=='|' or 
                            r[1]=='~-' or r[1]=='"' or 
                            r[1]=='[' or r[1]==']' or 
                            r[1]=='!' or r[1]=='x' or
                            r[1]=='p' or r[1]=='u' or
                            r[1]=='s' or r[1]=='T' or 
                            r[1]=='D' or r[1]=='+' or 
                            r[1]=='!' or r[1]=='' or 
                            r[1] =='~' or r[1]=='  '):

                            pass
                        else:
                            r[3] = dict[r[3]]
                            wtr2.writerow((r[0],r[1]))
    else:
        i=+2


'''
replace all empty spaces with commas
'''

def spliting(pathX, pathY):
    for i in range(2, 49):
      path = pathX
      name = path + str(i) + '.txt'
      if (os.path.exists(name) == True):
          path2 = pathY
          name2 =  path2 + str(i) + '.csv'
          with open(name) as infile, open(name2, 'w') as outfile:
              for line in infile:
                  outfile.write(" ".join(line.split()).replace(' ', ','))
                  outfile.write("\n") # trailing comma shouldn't matter
      else:
          print('no path')
          pass


