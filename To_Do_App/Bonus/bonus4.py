filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

#Tuples - imutable version of list
#not possible to modify them

filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
