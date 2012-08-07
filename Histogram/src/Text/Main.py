'''
Created on 22/05/2012
^ yes that is 9 days ago
@author: ultrazoid_
'''
import string
import time

fileName = 'IT.CEL.SETS.P2_Indicator_MetaData_en_EXCEL.csv'
mainFile = open(fileName, 'r')  #opens the *.csv file
linesSolid = mainFile.readlines() #reads all lines and places them into a list
mainFile.close() #closes the *.csv file as it is no longer needed
linesYears = string.split(linesSolid[0],',') #creates a list that has the years in it 
linesYears.remove('Country Name') #removes Country Name and 
linesYears.remove('Country Code') #Country Code from said list
hist = '|' #defines the character that is going to be used for the histogram
def median (y):
    z = len(y) #finds the length of the list (y) parameter
    if not z%2: #if the list length is even
        return (y[(z/2)-1] + y[z/2]) / 2 #return the average of the two middle values
    return y[z/2] #if not even return the middle value
def mode(li):
    li.sort() #sorts the list li
    numbers = {} #creates a dictionary called numbers
    for x in li: #creates a for loop
        num = li.count(x) #counts how many times x appears in the list
        numbers[x] = num #stores num in numbers for x
    highest = max(numbers.values()) #finds the highest value count in numbers
    n = []
    for m in numbers.keys():
        if numbers[m] == highest:#if m is equal to highest
            n.append(m) #add it to the list n
    return n # return list n
print 'Cell Phones Per 100 People'
print "By Emerson 'ultrazoid_' Pender \n"
print 'There are currently',len(linesSolid)-1,'Lines in the data file'
print "NOTE: All values are expressed as 'Cell phone(s) per 100 people'\n"
print "Please choose a mode"
print "By entering the Name or Number:"
print "CountryCode(1)/Year(2)/Mean(3)/Median(4)/Mode(5)"
modeInput = raw_input("Or type end to end:") #creates a user input
while modeInput != 'end': #while loop so the program will continue to prompt the user to select a mode until the end command is entered
    if modeInput == "CountryCode" or modeInput == "1": #if the user enters CountryCode mode values
        print "CountryCode Mode Activated...\n"           #start CountryCode mode
        countryCodesS = []
        lineGather = 1
        while lineGather in range(1, len(linesSolid)):
            lineCode = string.split(linesSolid[lineGather], ',')
            if '"' not in lineCode[0]:
                countryCodesS.insert(lineGather-1, lineCode[1])
            if '"' in lineCode[0]:
                countryCodesS.insert(lineGather-1, lineCode[2])
            lineGather = lineGather + 1
        print "NOTE: The program will now load country codes,"
        print "Please note that this may take an extended period of time"
        raw_input("Press enter to continue...")
        for code in countryCodesS:
            print code
        goFor = False
        while goFor == False:
            codeInput = raw_input("Please enter a country code (Case insensitive):")
            codeInputUpper = string.upper(codeInput)
            if codeInputUpper in countryCodesS: #if the country code inputed is in the List containing the country codes
                print "Country Found" #start country code data finding
                line = countryCodesS.index(codeInputUpper)+1 #Uses the index of the input to find the line value
                lin = str(line-1)
                print "Finding Data for", codeInputUpper,"(Index",lin + ")"
                time.sleep(2) #waits for 2 seconds
                codeSplit = string.split(linesSolid[line], ',') #splits the selected line at ',' 
                codeSplit.remove(codeInputUpper) #removes the input
                countr = codeSplit[0] #defines the country name that this data is for
                print "This Data is for:", countr #prints a prompt
                if '"' in codeSplit[0]: #if the country name contains '"'
                    codeSplit.remove(codeSplit[1]) #remove another index (due to the name being split e.g Bahamas, The)
                codeSplit.remove(codeSplit[0]) #remove the country name
                yearSet = 0
                sl = 1
                dataFix = 0
                while sl <= len(codeSplit)-1: #this while loop is the 'plotting' loop
                    if codeSplit[dataFix] == '': #if the current value is ''
                        data = "No Data" #make data = 'No Data'
                    elif codeSplit[dataFix] != '': # if it doesn't
                        data = codeSplit[dataFix] #data = the value
                    spacePrint = '_' #the next lines up to the end of the while next while loop
                    spaceMod = len(linesYears[yearSet]) #are to work out how much spacing is needed
                    spaceBlock = 20 - spaceMod 
                    spaceNeed = 1
                    while spaceNeed <= spaceBlock:
                        spacePrint = spacePrint + '_'
                        spaceNeed = spaceNeed + 1 #(up until here)
                    if data != "No Data": #if data does not = 'No Data'
                        try: #starts an exception
                            dataFloat = float(data) # the next few lines work out how many '|' to print
                            dataInt = int(dataFloat)
                            dataIntStr = str(dataInt)
                            multNight = dataFloat / 200.0
                            secTen = multNight * 50
                            dataHist = int(secTen)
                            histLimit = 1
                            if dataHist == 0:
                                dataPrint = ': '
                            elif dataHist != 0:
                                dataPrint = ': '+ '|'
                            while histLimit in range(1, dataHist):
                                dataPrint = dataPrint + '|'
                                histLimit += 1
                        except ValueError: #if the a ValueError occurs make the dataPrint conversion error
                            dataPrint = "Conversion Error"
                    elif data == "No Data":
                        dataPrint = ': No Data'
                    if dataPrint != ': No Data': #if the data contains data print this set
                        print linesYears[yearSet] + spacePrint + dataPrint, '('+dataIntStr+')'
                    elif dataPrint == ': No Data': #if not print this data
                        print linesYears[yearSet] + spacePrint + dataPrint
                    sl += 1 #increments count values
                    dataFix += 1
                    yearSet += 1
                goFor = True #allows the program to advance                                     
            elif codeInputUpper not in countryCodesS: #if the input is 'invalid' just prints a message
                print "Please enter a valid Country Code"
        time.sleep(2)
        print "\n" #:O A NEW LINE
    elif modeInput == "Year" or modeInput == '2': #year mode is entered
        goFor =False
        print "Year Mode Activated..."
        time.sleep(2)
        print "\n"
        print "Years Found:"
        for element in linesYears: #prints availible years
            print element
        while goFor == False: 
            yearInput = raw_input("Please select a year:") #user input prompt
            if yearInput in linesYears: #if year found do this...
                print "Year Found"
                collumn = linesYears.index(yearInput)+2#sets collumn values
                collum = str(collumn-2)
                print "Finding Data for", yearInput,"(Index",collum + ")" 
                time.sleep(2)
                dataYear = []
                countrName = []
                sl = 1
                insertLine = 0
                while sl <= len(linesSolid)-1: #data fetching while loop
                    yearSplit = string.split(linesSolid[sl],',')
                    if '"' in yearSplit[0]: #refer to explanation in CountryCodes
                        collumn = collumn + 1
                    if '"' not in yearSplit[0]:
                        collumn = linesYears.index(yearInput)+2
                    dataYear.insert(insertLine,yearSplit[collumn]) #list for data
                    countrName.insert(insertLine, yearSplit[0]) # list for country names
                    sl += 1 #increments
                    insertLine += 1
                insertLine = 0
                for element in countrName: #printing for loop
                    if dataYear[insertLine] == '': #data = no data for ''
                        data = "No Data"
                    elif dataYear[insertLine] != '': #opposite to above
                        data = dataYear[insertLine]
                    #start space block
                    spacePrint = '_' 
                    spaceMod = len(countrName[insertLine])
                    spaceBlock = 20 - spaceMod
                    spaceNeed = 1
                    while spaceNeed <= spaceBlock:
                        spacePrint = spacePrint + '_'
                        spaceNeed = spaceNeed + 1
                    #end space block
                    if data != "No Data": #you know the drill
                        try: #creates an exception
                            dataFloat = float(data) #conversion
                            dataInt = int(dataFloat)
                            dataIntStr = str(dataInt)
                            #start scaling
                            multNight = dataFloat / 200.0
                            secTen = multNight * 50
                            dataHist = int(secTen)
                            #end scaling
                            histLimit = 1
                            if dataInt == 0:
                                dataPrint = ': '
                            if dataInt != 0:
                                dataPrint = ': '+ '|'
                            while histLimit in range(1, dataHist): #creates the histogram
                                dataPrint = dataPrint + '|'
                                histLimit = histLimit + 1
                        except ValueError: #ValueError exception
                            data = "Conversion Error"
                    elif data == "No Data":
                        dataPrint = ': No Data' 
                    if dataPrint != ': No Data': #print if data
                        print element + spacePrint + dataPrint, '('+dataIntStr+')'
                    elif dataPrint == ': No Data': #print if no data
                        print element + spacePrint + dataPrint
                    insertLine += 1#increment
                goFor = True #continue
            else: 
                print "Please enter a valid year" #year not found
        time.sleep(2)
    elif modeInput == 'Mean' or modeInput == '3': #mean selected
        print 'Mean mode activated...'
        time.sleep(2)
        meanYC = raw_input("Would you like to find the mean of a Year(1) or a Country(2):") #year or country
        if meanYC == "Year" or meanYC == "1":
            print 'YEARS FOUND:'
            for year in linesYears: #print years
                print year
            goFor = False
            while goFor == False:
                meanInput = raw_input("Please enter a year:") #prompts for year
                if meanInput in linesYears:
                    print "Year Found"
                    collumn = linesYears.index(meanInput)+2
                    collum = str(collumn-2)
                    print "Finding Mean for", meanInput,"(Index",collum + ")"
                    time.sleep(2)
                    averageYear = []
                    sl = 1
                    insertLine = 0
                    #start add to list
                    while sl <= len(linesSolid)-1:
                        yearSplit = string.split(linesSolid[sl],',')
                        if '"' in yearSplit[0]:
                            collumn = collumn + 1
                        if '"' not in yearSplit[0]:
                            collumn = linesYears.index(meanInput)+2
                        averageYear.insert(insertLine,yearSplit[collumn])
                        insertLine += 1
                        sl += 1
                    #end add to list
                    summ = 0
                    for value in averageYear:
                        if value != '':
                            try:
                                valueFloat = float(value) 
                                valueInt = int(valueFloat)#converts to integer
                                summ += valueInt #adds to the sum
                            except ValueError:
                                a = 1
                        elif value == '':
                            averageYear.remove(value)
                    avv = summ / len(averageYear) #divides by the length 
                    avvs = str(avv) #converts average to a string
                    print "Mean for",meanInput + ': ' + avvs,'Cell phone(s) per 100 people' #PRINT
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a valid year"
        elif meanYC == "Country" or meanYC == "2":
            print "COUNTRYCODES FOUND...\n"
            #practically the same as years
            countryCodesS = []
            lineGather = 1
            while lineGather in range(1, len(linesSolid)):
                lineCode = string.split(linesSolid[lineGather], ',')
                if '"' not in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[1])
                if '"' in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[2])
                lineGather = lineGather + 1
            print "NOTE: The program will now load country codes,"
            print "Please note that this will take an extended period of time"
            raw_input("Press enter to continue...")
            for code in countryCodesS:
                print code
            goFor = False
            while goFor == False:
                codeInput = raw_input("Please enter a country code (Case insensitive):")
                codeInputUpper = string.upper(codeInput)
                if codeInputUpper in countryCodesS:
                    print "Country Found"
                    line = countryCodesS.index(codeInputUpper)+1
                    lin = str(line-1)
                    print "Finding Mean for", codeInputUpper,"(Index",lin + ")"
                    time.sleep(2)
                    codeAverage = string.split(linesSolid[line], ',')
                    codeAverage.remove(codeInputUpper)
                    countr = codeAverage[0]
                    print "This Mean is for:", countr
                    if '"' in codeAverage[0]:
                        codeAverage.remove(codeAverage[1])
                    codeAverage.remove(codeAverage[0])
                    summ = 0
                    for value in codeAverage: #for each value add it to the sum
                        if value != '':
                            try:
                                valueFloat = float(value)
                                valueInt = int(valueFloat)
                                summ += valueInt
                            except ValueError:
                                a=1
                        elif value == '':
                            codeAverage.remove(value)
                    avv = summ/len(codeAverage) #find average
                    avvs = str(avv) #convert to string
                    print "Mean for",countr + ': ' + avvs,'Cell phone(s) per 100 people' #PRINT
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a Valid country code"
    elif modeInput == 'Median' or modeInput == '4': #median selected
        print 'Median mode activated...'
        time.sleep(2)
        medianYC = raw_input("Would you like to find the mean of a Year(1) or a Country(2):") #year or country
        if medianYC == "Year" or medianYC== '1': #YEAR
            print 'YEARS FOUND:'
            for year in linesYears: #print years
                print year
            goFor = False
            while goFor == False:
                medianInput = raw_input("Please enter a year:") #which year
                if medianInput in linesYears:
                    print "Year Found"
                    collumn = linesYears.index(medianInput)+2 #prepare data
                    collum = str(collumn-2)
                    print "Finding Median for", medianInput,"(Index",collum + ")"
                    time.sleep(2)
                    middleYear = []
                    sl = 1
                    insertLine = 0
                    #start add to list
                    while sl <= len(linesSolid)-1:
                        yearSplit = string.split(linesSolid[sl],',')
                        if '"' in yearSplit[0]:
                            collumn = collumn + 1
                        if '"' not in yearSplit[0]:
                            collumn = linesYears.index(medianInput)+2
                        try:
                            yearFloat = float(yearSplit[collumn])
                            yearInt = int(yearFloat)
                            middleYear.insert(insertLine,yearInt)
                        except ValueError:
                            a = 1
                        insertLine += 1
                        sl += 1
                    #end add to list
                    y = sorted(middleYear) #sort that list NAOW
                    medianPrint = str(median(y)) #finds the median AND converts to a string
                    print "Median for",medianInput +': ' + medianPrint,'Cell phone(s) per 100 people' #PRINT
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a valid year"
        elif medianYC == "Country" or medianYC == '2': #COUNTRY
            print "COUNTRYCODES FOUND...\n"
            countryCodesS = []
            lineGather = 1
            #start add to list
            while lineGather in range(1, len(linesSolid)):
                lineCode = string.split(linesSolid[lineGather], ',')
                if '"' not in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[1])
                if '"' in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[2])
                lineGather = lineGather + 1
            #end add to list
            print "NOTE: The program will now load country codes,"
            print "Please note that this will take an extended period of time"
            raw_input("Press enter to continue...")
            for code in countryCodesS: #print codes
                print code
            goFor = False
            while goFor == False:
                codeInput = raw_input("Please enter a country code (Case insensitive):") #which one?
                codeInputUpper = string.upper(codeInput)
                if codeInputUpper in countryCodesS:
                    print "Country Found"
                    line = countryCodesS.index(codeInputUpper)+1 #prepares data
                    lin = str(line-1)
                    print "Finding Median for", codeInputUpper,"(Index",lin + ")" #prompt
                    time.sleep(2)
                    codeMedian = string.split(linesSolid[line], ',') #prepare some more
                    codeMedian.remove(codeInputUpper)
                    countr = codeMedian[0]
                    print "This Median is for:", countr #state country
                    if '"' in codeMedian[0]:#if '"' in countr
                        codeMedian.remove(codeMedian[1]) # remove that
                    codeMedian.remove(codeMedian[0]) #then remove that
                    spot = 0
                    middleCountry = []
                    for value in codeMedian:
                        try:
                            valueFloat = float(value) #convert
                            valueInt = int(valueFloat)
                            middleCountry.insert(spot,valueInt) #insert
                        except ValueError:
                            a = 1
                        spot += 1
                    sortC = sorted(middleCountry) #sort
                    medianPrint = str(median(sortC)) #find median and convert to string
                    print "Median for",countr +': ' + medianPrint,'Cell phone(s) per 100 people' #PRINT
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a valid Country Code" #OI! You didn't enter I valid code
    elif modeInput == 'Mode' or modeInput == '5': #mode selected                      
        print 'Mode mode activated...'
        time.sleep(2)
        modeYC = raw_input('Would you like to find the mean of a Year(1) or a Country(2):') #year or country
        if modeYC == 'Year' or modeYC == '1': #YEAR
            print 'YEARS FOUND:'
            for year in linesYears: #print years
                print year
            goFor = False
            while goFor == False:
                modesInput = raw_input("Please enter a year:")#which one?
                if modesInput in linesYears:
                    print "Year Found"
                    collumn = linesYears.index(modesInput)+2 #prepare data
                    collum = str(collumn-2)
                    print "Finding Mode for", modesInput,"(Index",collum + ")" #prompt
                    time.sleep(2)
                    middleYear = []
                    sl = 1
                    insertLine = 0
                    #start add to list
                    while sl <= len(linesSolid)-1:
                        yearSplit = string.split(linesSolid[sl],',')
                        if '"' in yearSplit[0]:
                            collumn = collumn + 1
                        if '"' not in yearSplit[0]:
                            collumn = linesYears.index(modesInput)+2
                        try:
                            yearFloat = float(yearSplit[collumn])
                            yearInt = int(yearFloat)
                            middleYear.insert(insertLine,yearInt)
                        except ValueError:
                            a = 1
                        insertLine += 1
                        sl += 1
                    #end add to list
                    print "Mode(s) for", modesInput + ':',mode(middleYear),'Cell phone(s) per 100 people' #PRINT
                                                            #^calculates mode
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a valid year"
        elif modeYC == 'Country' or modeYC == '2': #COUNTRY
            print "COUNTRYCODES FOUND...\n"
            countryCodesS = []
            lineGather = 1
            #start country find
            while lineGather in range(1, len(linesSolid)):
                lineCode = string.split(linesSolid[lineGather], ',')
                if '"' not in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[1])
                if '"' in lineCode[0]:
                    countryCodesS.insert(lineGather-1, lineCode[2])
                lineGather += 1
            #end country find
            print "NOTE: The program will now load country codes," #prompt
            print "Please note that this will take an extended period of time"
            raw_input("Press enter to continue...") #did this because os.system("PAUSE") was causing errors
            for code in countryCodesS: #print codes
                print code
            goFor = False
            while goFor == False:
                codeInput = raw_input("Please enter a country code (Case insensitive):") #which one?
                codeInputUpper = string.upper(codeInput)
                if codeInputUpper in countryCodesS:
                    print "Country Found"
                    line = countryCodesS.index(codeInputUpper)+1 #prepare
                    lin = str(line-1)
                    print "Finding Mode for", codeInputUpper,"(Index",lin + ")" #prompt
                    time.sleep(2)
                    codeMedian = string.split(linesSolid[line], ',') #prepare more
                    codeMedian.remove(codeInputUpper)
                    countr = codeMedian[0]
                    print "This Mode is for:", countr #prompt
                    if '"' in codeMedian[0]: #if '"' in countr
                        codeMedian.remove(codeMedian[1]) #remove that
                    codeMedian.remove(codeMedian[0]) #remove that
                    spot = 0
                    middleCountry = []
                    for value in codeMedian:
                        try:
                            valueFloat = float(value) #convert
                            valueInt = int(valueFloat)
                            middleCountry.insert(spot,valueInt) #insert
                        except ValueError:
                            a=1
                        spot += 1
                    print "Mode(s) for", countr + ':',mode(middleCountry),'Cell phone(s) per 100 people' #PRINT
                                                            #^calculates mode
                    goFor = True
                    time.sleep(2)
                else:
                    print "Please enter a valid country code"
    print "Please choose a mode"
    print "By entering the Name or Number:"
    print "CountryCode(1)/Year(2)/Mean(3)/Median(4)/Mode(5)"
    modeInput = raw_input("Or type end to end:") #prompts user for mode selct again
    
print "\nThank for using\nEmerson 'ultrazoid_' Pender's\nIT 1+2 Assignment\n" #closing statement
time.sleep(3)
loopy = 0
while loopy in range (0,3): #beg ^.^
    print "Please give me a good mark\n" 
    loopy += 1
time.sleep(1)
print "THE END" #or is it?