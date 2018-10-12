# from titlecase import titlecase
userDictionary  = {}
relationDictionary = {}
incrementalVariableForID = 1
relation = []



def addUser(name, gender, incrementalVariableForID):
    userID = name + str(incrementalVariableForID);
    userDictionary[userID.lower()] = [name, gender]
    return userID


def queryInfo(id, who):
    userName = userDictionary[id]
    relation = relationDictionary[id]

    if who == "f":
        nameID = relation[0]
        name = userDictionary[nameID][0]
    elif who == "m":
        nameID = relation[1]
        name = userDictionary[nameID][0]

    else:
        nameID = relation[2]
        name = userDictionary[nameID][0]

    return str(userName).title(), str(name).title()


if __name__ == "__main__":
    while True:
        addOrQuery = input("Add Info Or Query? (A/Q): ")

        if addOrQuery.lower() == "a":
            userName = input("Enter your Name: ")
            gender = input("Enter Gender(M/F): ")
            userReturnId = addUser(userName, gender, incrementalVariableForID)
            incrementalVariableForID = incrementalVariableForID + 1
            print("Your User Id: " + userReturnId)

            reply = input("Do you want add parent? (y/n): ")
            if reply == 'y':
                name = input("Enter User Father Name: ")
                gender = 'm'
                fatherReturnID = addUser(name, gender, incrementalVariableForID)
                incrementalVariableForID = incrementalVariableForID + 1

                name = input("Enter User Mother Name: ")
                gender = 'f'
                motherReturnID = addUser(name, gender, incrementalVariableForID)
                incrementalVariableForID = incrementalVariableForID + 1

                name = input("Enter User GrandFather Name: ")
                gender = 'f'
                grandFatherReturnID = addUser(name, gender, incrementalVariableForID)
                incrementalVariableForID = incrementalVariableForID + 1


                relationDictionary[ userReturnId ]= [fatherReturnID, motherReturnID, grandFatherReturnID]


            else:
                pass

            newOne = input("do you want add another Info or query? (a/q): ")
            if newOne == 'a':
                continue
            else:
                searchingUserId = input("Enter Your userID: ")
                whichOne = input("Which One you want to show? Father or Mother or GrandFather (F/M/G): ")
                print(queryInfo(searchingUserId.lower(), whichOne.lower()))

        else:
            searchingUserId = input("Enter Your userID: ")
            whichOne = input("Which One you want to show? Father or Mother(F/M): ")
            print(queryInfo(searchingUserId.lower(), whichOne.lower()))





#
# print(userDictionary)
# print(relationDictionary)