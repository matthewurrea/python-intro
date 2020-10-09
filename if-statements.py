# if statements

# if statement logic example 

#I wake up 
#if I'm hungry 
#    I eat breakfast 
#
#I leave my house: 
#if it's cloudy 
#    I bring an umbrella 
# otherwise 
#    I bring sunglasses 
#
# Im at a restaurant 
# if I want meat 
#    I order a steak 
#otherwise if I want pasta 
#    I order spaghetti & meatballs 
#otherwise
#    I order a salad


# create a boolean variable 
is_male = False
is_tall = True

if is_male or is_tall: 
    print("You are a tall male.")
    # not() function negates the argument
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
else: 
    print("You are not a male and not tall.")

