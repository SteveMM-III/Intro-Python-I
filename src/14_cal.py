"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
#########################################
# Imports
import sys
import calendar
from datetime import datetime

#########################################
# Functions
def show_usage():
    
    print( "usage:" )
    print( "    python 14_cal.py month year" )
    print( "\tmonth - integer 1-12 inclusive" )
    print( "\tyear  - four digit integer" )
    print( "" )
    print( "    * Month and year are both optional" )
    print( "    * Month can be used without year - will default to current year" )
    print( "    * If year is provided, month must also be provided, and month must come first" )

######
def num_check( num ):

    value = 0
    
    try:
        value = int( num )
    except:
        show_usage()
        exit()

    return value
#########################################
# Setup
num_args = len( sys.argv )

dt = datetime.now()

calendar.setfirstweekday( 6 )

#########################################
# Check number of arguments and execute
if num_args < 2:

    print( calendar.month( dt.year, dt.month ) )

elif num_args == 2:

    month = num_check( sys.argv[ 1 ] )

    print( calendar.month( dt.year, month ) )

elif num_args == 3:

    month = num_check( sys.argv[ 1 ] )
    year  = num_check( sys.argv[ 2 ] )

    print( calendar.month( year, month ) )

else:
    show_usage()
#########################################EoF
