data = []
continentData = {}

rank, country, y2018, y2019, share, popChange, percentChange, continent = 0,1,2,3,4,5,6,7


#open file
file = open('WorldPopulationData2019.txt', 'r')
with file as f:
    #skipping first 2 rows
    next(f)
    next(f)
    #reading from 3rd row onwards
    for line in f:
        #remove trailing newline
        line = line.rstrip('\n')
        #spliting it and putting it as individual array
        dataSplit = line.split(";")
        #adding data into array
        data.append(dataSplit)
#close the file so it does not continue to take up memory
file.close()

#adding continents
for i in range(len(data)):
        if data[i][continent] not in continentData:
            continentData[(data[i][continent])] = 0

#first loop to get country data array
for i in range(len(data)):
    #check if country data array has the coninent in the continent data array
    if data[i][continent] in continentData:
        #add value to key
        continentData[(data[i][continent])] = int(data[i][y2019]) + int(continentData[(data[i][continent])])

#sort and store in a variable
descending_sort = sorted(data, key=lambda x:x[percentChange], reverse=True)

worldPop = 0
#world calculator
for i in continentData.values():
    worldPop = worldPop + i
    
            
#counter to keep while loop going
flag = 0
#while loop will only stop when flag = 1
while flag != 1:
    print("Option 1: List the total populations of the different continents")
    print("Option 2: List the percentage population change in 2019 compared to 2018 for the different countries, in descending order.")
    print("Option 3: List the country based on first letter input. Next step will be asking for letter input.")
    print("Option 4: List the percentage population change in 2019 compared to 2018 for the different countries, in ascending order.")
    print("Option 5: World Population")
    print("Option 6: Continent to World Population")
    print("Option 7: Quit")
    option = int(input("Please select an option: "))
    #option 1: total continents
    if option == 1:        
        print(continentData)
    #option 2: percentage population change in descending order
    elif option == 2:
        #ouput only country, 2019 population and % changed
        for i in range(len(descending_sort)):
            print("Country name: " + descending_sort[i][country])
            print("2019 Population: " + descending_sort[i][y2019])
            print("% Changed: " + descending_sort[i][percentChange])
            print("*" * 50)
    #option 3: single letter option
    elif option == 3:
        #internal counter
        internalFlag = 0
        #while loop for interactive purposes
        while internalFlag != 1:
            #input for a letter
            letterOption = str.upper(input("Please choose a letter or type quit to quit: "))
            #check if it is 1
            if letterOption == 'QUIT' and len(letterOption) > 1:
                #trigger the flag and back to main menu
                internalFlag = 1
            #check if it is a single letter
            elif len(letterOption) == 1:
                #check if it is alpha
                if letterOption.isalpha:
                    #array
                    for i in range(len(data)):
                        #storing first letter in the array as a variable
                        compareString = data[i][country][1]
                        #comparing the letters
                        if compareString == letterOption:
                            print("Country name: " + data[i][country])
                            print("2019 Population: " + data[i][y2019])
                            print("*" * 70)
                #if input is not a letter
                else:
                    print("Input is not a letter. Please input a single letter")
            #if input has too many letters
            else:
                print("Input has too many letters. Please input a SINGLE letter")

    #option 4
    elif option == 4:
        internalFlag = 0
        while internalFlag != 1:
            top = str(input("Top how many would you like to see? Answer in whole numbers please :"))
            if not top.isdigit():
                print("Please input whole numbers")
            else:
                top = int(top)
                for i in range(top-1):
                    print("Country name: " + descending_sort[i][country])
                    print("2019 Population: " + descending_sort[i][y2019])
                    print("% Changed: " + descending_sort[i][percentChange])
                    print("Population Changed: " + descending_sort[i][popChange])
                    print("*" * 50)
                    internalFlag = 1                
            
    #option 5: World Population
    elif option == 5:         
        print("World population: " + str(worldPop))
    
    #option 6: Continent to World Population
    elif option == 6:
        print("*" * 50)
        for keys,values in continentData.items():
            print("{0} ratio to the world: {1}/".format(keys,values) + str(worldPop))
        print("*" * 50)
    #option 7: quit
    elif option == 7:
        #sets the while loop flag to 1 so it ends the loop
        flag = 1    
    #if option is not available
    else:
        print("Option not available, please rechoose your options")
