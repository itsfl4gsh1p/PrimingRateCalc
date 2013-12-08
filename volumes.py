# Justin A
# @itFL4GSH1P

def vols_dextrose(): #function to calculate volumes based on dextrose.
	conv = ((dvolumes - saturation) / .27027)
	final = ((conv * .1335) * batch_size)
	print round(final, 2), "ounces of sugar per 5gal batch of beer."

def vols_sucrose(): #function to calculate volumes based on surcose
	conv = ((dvolumes - saturation) / .286)
	final = ((conv * .1335) * batch_size)
	print round(final, 2), "ounces of sugar per 5gal batch of beer."

# variable explanation to define above.
# conv = Is the pitching rate in g/L (grams per liter)
# dvolumes = Desired CO2 volumes level as chosen below
# saturation = Volumes of CO2 present in beer which has been fermented and is at @ specific temp
# final =  converts the entire formula from g/L to o/G (ounces per gallon)


print "===================================================================================================="
print "| Welcome to my custom CO2 volumes calculator.                                                     |"
print "| This is not an 'exact' calculation as it is based on a table set of information.                 |"
print "| It should be plenty accurate enough for general use.                                             |"
print "| This calculation currently is only for dextrose (corn sugar) & sucrose (table sugar/brown sugar) |"
print "| That being said, let's get started.                                                              |"
print "===================================================================================================="

print "Please note this will exept decimal numbers to indicate very small test batch sizes (ie. 1/2gl would be entered as .5)"
batch_size = float(raw_input("Please choose your batch size in gallons: "))


print "1. Dextrose (corn sugar)"
print "2. Sucrose (table sugar/brown sugar)"
sugar = int(raw_input("Please choose your sugar type: ")) #allows user to make a simple menu choice


degrees = int(raw_input("Please enter the temperature of your beer in *F: ")) #easy enough. accepts a temperature in degrees F.

#the following lines turn a conversion table into a big mess of if statements. The orginal table was based on celsius and had to be converted to F.
#there must be a better way to do this but for now this is functional
if 32 <= degrees <= 34:
	saturation = 1.70
elif 35 <= degrees <= 38:
	saturation = 1.60
elif 39 <= degrees <= 41:
	saturation = 1.50
elif 42 <= degrees <= 45:
	saturation = 1.40
elif 46 <= degrees <= 49:
	saturation = 1.30
elif 50 <= degrees <= 52:
	saturation = 1.20
elif 53 <= degrees <= 56:
	saturation = 1.12
elif 57 <= degrees <= 59:
	saturation = 1.05
elif 60 <= degrees <= 63:
	saturation = 0.99
elif 64 <= degrees <= 67:
	saturation = .93
elif 68 <= degrees <= 70:
	saturation = .88
elif 71 <= degrees <= 74:
	saturation = .83

# table was formulated from 2 sources:
# 1. http://hdb.org/ddraper/priming.html
# 2. http://howtobrew.com
print "-------------------------------------------"
print "|     Volumes of CO2 in common styles     |"
print "|=========================================|"
print "|Beer Style                        Volumes|"
print "|=========================================|"
print "|British-style ales                1.5-2.0|"
print "|Porter, stout                     1.7-2.3|"
print "|Belgian ales                      1.9-2.4|"
print "|European lagers                   2.2-2.7|"
print "|American ales & lagers            2.2-2.7|"
print "|Lambic                            2.4-2.8|"
print "|American wheat                    2.7-3.3|"
print "|Fruit lambic                      3.0-4.5|"
print "|German wheat beer                 3.3-4.5|"
print "-------------------------------------------"

dvolumes = float(raw_input("Please enter desired CO2 volumes: ")) # accepts desired Volumes as floating point number

# choice of sugar defined above
if sugar == 1:
	vols_dextrose()
elif sugar == 2:
	vols_sucrose()

