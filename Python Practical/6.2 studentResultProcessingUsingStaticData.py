# Write a program for Result processing using nested list
lst=[
        [
            {
                "name": "Mahi",
                "rollNo": 11
            },
            [90,80,89,98,88]
        ],
        [
            {
                "name": "Azhr",
                "rollNo": 12
            },
            [92,83,87,88,98]
        ],
        [
            {
                "name": "Vinay",
                "rollNo": 13
            },
            [99,90,79,89,92]
        ]
        
    ]

def calPercentage(lst1):
    total=0
    for i in range(len(lst1)):
        total += lst1[i]
    return (total/len(lst1))

def printDetails(lst):
    print("Name      : ",lst[0]["name"])
    print("Roll No.  : ",lst[0]["rollNo"])
    print("Percentage: ",calPercentage(lst[1]))

for i in range(len(lst)):
    print("******************************")
    print("Students details : ",i+1)
    printDetails(lst[i])


