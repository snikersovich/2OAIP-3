import csv
n = int(input())
with open('vps.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    print('\n'.join([i[0] for i in list(reader)[1:] if int(i[-2]) >= n]))