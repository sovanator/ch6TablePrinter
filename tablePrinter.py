tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose'],]
def printTable(itemsParam):
    longestString =[]
    newItems=[]
    #get the longest string from the table items
    for items in tableData:
        l2=0
        for item in items:
            l1 = len(item)
            if l1> l2:
                l2=l1
        longestString.append(l2)
    #Flip the table to print
    for i in range(len(tableData)+1):
        newItem=[]
        j=0
        while j<len(tableData) and i<len(tableData[0]):
            newItem.append(tableData[j][i])
            j=j+1
        newItems.append(newItem)
    #Print the table
    for items in newItems:
        for k in range(len(items)):
            print(items[k].ljust(longestString[k]+1), end="")
        print("")

printTable(tableData)