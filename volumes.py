def vols_dextrose():
	conv = ((dvolumes - saturation) / .27027)
	final = ((conv * .1335) * 5)
	print round(final, 2), "ounces of sugar per 5gal batch of beer."

def vols_sucrose():
	conv = ((dvolumes - saturation) / .286)
	final = ((conv * .1335) * 5)
	print round(final, 2), "ounces of sugar per 5gal batch of beer."


print "Welcome to my custom CO2 volumes calculator."
print "This is not an 'exact' calculation as it is based on a table set of information."
print "It should be plenty accurate enough for general use."
print "This calculation currently is only for dextrose (corn sugar) & sucrose (table sugar/brown sugar)"
print "Let's get started."
print "==============================================="

print "1. Dextrose (corn sugar)"
print "2. Sucrose (table sugar/brown sugar)"
print "Please choose your sugar type:"


sugar = int(raw_input( ))

degrees = int(raw_input("Please enter the temperature of your beer in *F:"))

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

dvolumes = float(raw_input("Please enter desired CO2 volumes:"))

if sugar == 1:
	vols_dextrose()
elif sugar == 2:
	vols_sucrose()

