total = 0 # sum of scores
count = 0 # number of scores entered
 
# get one score & convert string to integer
score = int(input("Enter score, (Enter -9 to end): ") ) 

while True:
    if(score==-9):
        break
    else:
        total+=score
        count+=1
        print(count)
        print("Score =",score)
        score=int(input("Enter next score, (Enter -9 to end): "))
# print average of scores entered
average = float( total ) / count
print("Class average is", average)