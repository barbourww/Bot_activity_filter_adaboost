import matplotlib.pyplot as plt

ada_output = []
with open('mySubmission_raw.csv', 'rb') as f:
    for line in f:
        ada_output.append(float(line))

ada_output_norm = []
with open('minMax_submission2.csv', 'rb') as f:
    for line in f:
        ada_output_norm.append(float(line))

ada_output_norm2 = []
with open('minMax_submission3.csv', 'rb') as f:
    for line in f:
        ada_output_norm2.append(float(line))

ada_output_norm3 = []
with open('minMax_submission4.csv', 'rb') as f:
    for line in f:
        ada_output_norm3.append(float(line))

tree_output = []
with open('tree_mySubmission.csv', 'rb') as f:
    f.readline()
    for line in f:
        tree_output.append(float(line.split(',')[1]))

#plt.hist(ada_output, bins=20)
#plt.show()
print ada_output_norm.__len__(), ada_output_norm2.__len__()
plt.scatter(ada_output_norm3, ada_output_norm2)
plt.show()