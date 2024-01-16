# Sort some data and display it on the screen
# Parameters:
# data: a list to sort into ascending order
# Returns: (None)
def sortAndDisplay(data):
    for i in range(len(data)):
        for j in range(len(data)-1, 0, -1):# without -1 j takes 6th index and there is no 6th index in data
            if data[j] < data[j-1]:
                t = data[j]
                data[j] = data[j-1]
                data[j-1] = t #in upper row data[j] is defined as data[j-1], and data[j] is also defined as t: so that means data[j-1] is t
    return(data) #return should be in 1st for loop scope to display the work which is doing 1st for loop
print(sortAndDisplay([1,3,5,4,6,2]))