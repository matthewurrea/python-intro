#using dicitonaries
#dictionaries are a special structure in python that allows us to store
#information in key value pairs 

#example
#word(key) ~ definition associated to the word

#all keys need to be unique
#keys can be strings or number
#Jan -> January 
#Mar -> March

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Luv", "Not a valid key"))
#                                   default value
