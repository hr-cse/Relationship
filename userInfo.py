userDictionary = {}
relationDictionary = {}
index = 1
relation = []

father = False
mother = False
grandFather = False
son = False


def addUser(name="", gender="", index=""):
    ID = name.lower() + str(index);
    userDictionary[ID.lower()] = [name, gender]
    return ID


def queryInfo(id, who):
    try:
        userName = userDictionary[id]
        relation = relationDictionary[id]

        if who == "f":
            nameID = relation[0]
            name = userDictionary[nameID][0]
        elif who == "m":
            nameID = relation[1]
            name = userDictionary[nameID][0]

        elif who == 'g':
            nameID = relation[2]
            name = userDictionary[nameID][0]

        elif who == 's':
            nameID = relation[3]
            name = userDictionary[nameID][0]

        else:
            pass

        return str(userName).title(), str(name).title()
    except:
        print("Not Found")


def updateRelation(id, who, personID):
    if who == "f":
        relationDictionary[id][0] = personID
    elif who == "m":
        relationDictionary[id][1] = personID
    elif who == "g":
        relationDictionary[id][2] = personID
    else:
        relationDictionary[id][3] = personID



def defaultRelation(userReturnId):
    relationDictionary[userReturnId] = ["", "", "", ""]


def relationMaker(id, rID):
    if father:
        relationDictionary[id] = ["", "", "", rID]
    if mother:
        relationDictionary[id] = ["", "", "", rID]

def allInfo():
    print(userDictionary)
    print(relationDictionary)


if __name__ == "__main__":
    while True:

        addOrQuery = input("Add Info or Query or Update? (A/Q/U): ")

        if addOrQuery.lower() == "a":
            userName = input("Enter your Name: ")
            gender = input("Enter Gender(M/F): ")
            userReturnId = addUser(userName, gender, index)
            index = index + 1
            #print("Your User Id: " + userReturnId)

            reply = input("Do you want add parent? (y/n): ")
            if reply == 'y':
                name = input("Enter User Father Name: ")
                gender = 'm'
                fatherReturnID = addUser(name, gender, index)
                index = index + 1

                name = input("Enter User Mother Name: ")
                gender = 'f'
                motherReturnID = addUser(name, gender, index)
                index = index + 1

                name = input("Enter User GrandFather Name: ")
                gender = 'f'
                grandFatherReturnID = addUser(name, gender, index)
                index = index + 1

                name = input("Enter User Son Name: ")
                gender = input("Enter Gender(M/F): ")
                sonReturnID = addUser(name, gender, index)
                index = index + 1

                relationDictionary[userReturnId] = [fatherReturnID, motherReturnID, grandFatherReturnID, sonReturnID]
                relationDictionary[fatherReturnID] = [grandFatherReturnID, "", "", userReturnId]
                relationDictionary[motherReturnID] = ["", "", "", userReturnId]
                relationDictionary[grandFatherReturnID] = ["", "", "", fatherReturnID]

            else:
                defaultRelation(userReturnId)

            newOne = input("Add Info or Query or Update? (A/Q/U): ")
            if newOne.lower() == 'a':
                continue
            elif newOne.lower() == "q":
                allInfo()
                searchingUserId = input("Enter Your userID: ")
                whichOne = input("Which One you want to show? Father, Mother, GrandFather or son?  (F/M/G/S): ")
                print(queryInfo(searchingUserId.lower(), whichOne.lower()))

            elif newOne.lower() == "u":
                allInfo()
                searchingUserId = input("Enter Your userID: ")
                whichOne = input("Which One you want to update? Father, Mother, GrandFather or son?  (F/M/G/S): ")
                personName = input("Enter Name: ")
                personReturnID = addUser(personName, whichOne, index)
                index = index + 1

                updateRelation(searchingUserId.lower(), whichOne.lower(), personReturnID)
                print("OK , successfully update!")
                continue
            else:
                pass

        elif addOrQuery.lower() == "q":
            allInfo()
            searchingUserId = input("Enter Your userID: ")
            whichOne = input("Which One you want to show? Father, Mother, GrandFather or son?  (F/M/G/S): ")
            print(queryInfo(searchingUserId.lower(), whichOne.lower()))


        elif addOrQuery.lower() == "u":
            allInfo()
            searchingUserId = input("Enter Your userID: ")
            whichOne = input("Which One you want to update? Father, Mother, GrandFather or son?  (F/M/G/S): ")
            if whichOne.lower() == 'f':
                father = True
            elif whichOne.lower() == 'm':
                mother = True
            elif whichOne.lower() == 'g':
                grandFather = True
            elif whichOne.lower() == 's':
                son = True
            personName = input("Enter Name: ")
            personReturnID = addUser(personName, whichOne, index)
            index = index + 1

            updateRelation(searchingUserId.lower(), whichOne.lower(), personReturnID)

            relationMaker(personReturnID, searchingUserId)
            father = False
            mother = False
            grandFather = False
            son = False
            print("OK , successfully update!")

        else:
            pass



