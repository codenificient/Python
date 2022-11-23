#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #1st Video - creating a dictionary - walk them through this. And introduce the idea of a Case Study
    treeOrders ={}

    for row in reader:
        key = row[0]
        treeOrders[key]=row[1]
    
    infile.close()
    	
for key in treeOrders:
    trees = 0
    if reader.keys:
        trees.append(int(reader.values()))
    return trees

