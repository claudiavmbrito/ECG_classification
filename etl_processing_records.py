import csv

'''
This script is used for choosing only one of the channels 
of the ECG 
'''

for i in range(0,10):

    name = '/path/to/csv/'+str(i)+'.csv'
    name2 = '/path/to/csv1/'+str(i)+'.csv'

    print('Record ' + str(i) +'\n')
    with open(name, 'r') as f:
        rdr = csv.reader(f, delimiter = ',')
        with open(name2, 'w') as t:
            wtr = csv.writer(t, delimiter = ';')
            for r in rdr:
                #r[0] = float(r[0])/360
                #r[0] = float("{0:.3f}".format(r[0]))
                wtr.writerow( (r[1],) )
