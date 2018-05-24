#Program converts the temperature from Ferenheit to Celsius


    
def getInput():
    #get input
    tempInCAsString = input('Enter the temperature in Ferenheit: ')
    tempInF = int( tempInCAsString )
    return tempInF
        
def convertTemp(tempInF):
 #temperature conversion formula
    tempInC = (tempInF - 32) * 5/9
    return tempInC
       
    
def main():
    tempInF=getInput()
    tempInC=convertTemp(tempInF)
    print('The temperature in Celsius is: ', "%.1f" %tempInC, 'degrees')

    #asks the user to perform 3 conversions
    #for conversionCount in range( 3 ):
       # doConversion()
        
if __name__ == "__main__":
    main()