import sys

def planetScale():
   planets = ['Mercury', 'Venus', 'Moon', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto',
'Sun']
   percents = [.378, .907, .166, .377, 2.364, .916, .889, 1.125, 0.067, 27.072]
   print('Please enter your current Earth weight.')
   lbs = float(sys.stdin.readline())
   kgs = lbs* 0.453592
   print('Please enter what planet you would like to visit.')
   myPlanet = input().rstrip()
   index = 0
   for i in planets:
        if i == myPlanet:
            planetWeight = kgs * percents[index]
            print('On %s your weight would be %d' % (i, planetWeight))
        else:
          index = index+1


planetScale()
