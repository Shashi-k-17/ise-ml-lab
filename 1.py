import csv

a = []
with open('trainingdata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
    print(a)

print("\n The total number of training instances are: ", len(a))
num = len(a[0]) - 1
print("\n The initial hypothesis is: ")
hypothesis = ['0']*num
print(hypothesis)

for i in range(len(a)):
    if a[i][num] == 'Yes':
        for j in range(num):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print("\n The hypothesis for the training instance {} is: \n" .format(i+1), hypothesis)

print("\n The maximally hypothesis is:")
print(hypothesis)