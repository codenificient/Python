#getting a dictionary from a text file
#Getting a dictionary from a CSV file
import  csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)
   #creating a dictionary - walk through code.
   # And introduce the idea of a Case Study
    mydict ={}
    

    for row in reader:
        key = row[0]
        mydict[key]=row[1]
        
   
    
    infile.close()

# dictionary methods average, length, total trees, max value of trees

# total customers

customers = len(mydict)
print(customers)

    	
#change number of trees
def change_trees(division, trees):
        mydict[division] = int(trees)
        return mydict

def add_new(division, trees):
    if mydict[division] == int(trees):
        return 'exits already'
    else:
        mydict[division] = int(trees)
        return mydict

for key in mydict:
    print(key, mydict[key])