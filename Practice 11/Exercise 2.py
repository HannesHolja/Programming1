from usefulFunctions import GreeterWeather,nameofmonth,nameforfunctions,findindex,median,smallest,greatest
def main():
    GreeterWeather()
    rainlist = nameofmonth()
    greatestname = nameforfunctions(findindex(rainlist,greatest(rainlist)))
    lowestname = nameforfunctions(findindex(rainlist,smallest(rainlist)))
    print("The overall it rained this year was {0} millimeters.".format(sum(rainlist)))
    print("The greatest value for rain was in {0} with a value of {1}".format(greatest(rainlist),lowestname))
    print("The smallest value for rain was in {0} with a value of {1} millimeters.".format(greatestname,smallest(rainlist)))
    print("Median of all the values you entered was {0} millimeters".format(median(rainlist)))
main()
