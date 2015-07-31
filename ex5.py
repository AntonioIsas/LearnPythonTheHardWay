my_name = 'Zed A. Shaw'
my_age = 35 # not a lie 
my_height = 74 # inches
height_cm = my_height * 2.54
my_weight = 180 # lbs 
weight_kg = my_weight * .45
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %0.2f cm tall or %d inches tall." % (height_cm, my_height)
print "He's %0.2f kg or %d pounds heavy." % (weight_kg, my_weight)
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

#tricky line 
print "if I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight )


