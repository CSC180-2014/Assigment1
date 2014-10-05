""" Assigment #1
The Student Life Simulator starter code.
You should complete every incomplete function,
and add more functions and variables as needed.
Also add comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Sept. 22, 2014

Francis Kang & Ryan Tam
"""

"""
Submitted by: Ryan Tam, Francis Kang
CSC1800
"""


HOURS_IN_WEEK = 24 * 5 - 7 # The total number of hours from 12AM Monday to 5PM Friday.
MIN_SLEEP_PRECENT = 0.3 # The min % that a studnet must have slept to be considered awake
MIN_COFFEE_INTERVAL = 3 # The min hours that must pass before the student can drink coffee again without crashing

# Global variables.
hours_slept = 0  # total number of hours that the student has slept so far
hours_left = HOURS_IN_WEEK  # number of hours that remain in the week
knol_total = 0 #total knoledge gained durring the week
last_coffee_time = 0 #the last time the sudent drank coffee
coffee_crash = False # if the studented has drank too much coffee and has crashed

'''
Function returnes the knoledge points gained by attending one hour of class taking
in account if the student is alert. Function expects a valid course code (string) and
a boolen for if the student is awake or not.
'''
def knols_per_hour(subj, is_alert):
   #Deterimns how many knols are gained based on the course
   if subj is 'CSC':
      knols_gained=4
   elif subj is "MAT" or subj is "ESC" or subj is "PHY" or subj is "CIV":
      knols_gained=2
   else:
      return

   #If the student is not alert then they get half the knoledge
   if is_alert:
      return(knols_gained)
   else:
      knols_gained /=2
      return(knols_gained)

'''
Function record the time that the studnet drinks coffee at. If the studnet drinks
coffee to frequently (less than MIN_COFFEE_INTERVAL) then it determins the sudent
has crashed
'''
def drink_coffee():
   global last_coffee_time
   global hours_left
   global coffee_crash
   global MIN_COFFEE_INTERVAL
   
   #Check to see if student has crashed
   if abs(last_coffee_time-hours_left) < MIN_COFFEE_INTERVAL:
      coffee_crash = True
   
   #Record the last time the student drank coffee
   last_coffee_time = hours_left
   return

'''
Function deterimes if student is awake baised on how much they have slept and
if they have had coffee recently. Function returns a boolean
'''
def is_alert():
   global hours_slept
   global hours_left
   global HOURS_IN_WEEK
   global MIN_SLEEP_PRECENT
   global last_coffee_time
   global coffee_crash
   
   if coffee_crash:  #if the student has crashed on coffee already they cannot be alet for rest of week
      return(False)
   if (abs(last_coffee_time-hours_left) <= 1):  #if the student has had coffee he is awake
      return(True)
   
   #calcuate the hours that have elapsed
   hours_elapsed = HOURS_IN_WEEK-hours_left
   
   if hours_elapsed == 0:  #special case of time has not started studnet cannot have slept already
      sleep_percentage=0
   else: #calculate the precent of time spent sleeping
      sleep_percentage = hours_slept/hours_elapsed
   
   if (sleep_percentage > MIN_SLEEP_PRECENT):   #if the student has slept enough he is alert
      return(True)
   else: #student has not slept enough and is not alert
      return(False)
   
'''
Function addes to the knoledge learned baised on how long the student goes to class.
Function expects a valid course code (String) and a number of hours (int).
If there are not that many hours left in the week the function does nothing.
'''
def attend_lecture(subj, hrs):
   global knol_total
   global hours_left
   
   
   if hours_left >= hrs and hrs > 0:   #If there are that many hours left in the week
      #add the knoledge learned and update the time
      knols_earned = knols_per_hour(subj,is_alert())*hrs
      hours_left -= hrs
      knol_total+=knols_earned
   else: #Do nothing because there arent that many hours left
      return

'''
Function keeps track of hours slept by student and expects # hours slept (int)
If there are not that many hours left in the week the function does nothing.
'''
def sleep(hrs):
   global hours_left, hours_slept

   if hrs < 0 or hours_left < hrs:  # If hours is negative or there is not enough time in the week do nothing
      return
   else: #Update the hours left and the hours slept
      hours_left -= hrs
      hours_slept += hrs

'''
Function retuns the hours left in week
'''
def get_hours_left():
   global hours_left
   return(hours_left)

'''
Function retuns the total knowledge learned durring the week.
'''
def get_knol_amount():
   global knol_total
   return(knol_total)

'''
Function rests the week. Just for testing purpouses.
'''
def reset_week():
   global HOURS_IN_WEEK
   
   global hours_slept
   global hours_left
   global knol_total
   global last_coffee_time
   global coffee_crash
   
   hours_slept = 0
   hours_left = HOURS_IN_WEEK
   knol_total = 0
   last_coffee_time = 0
   coffee_crash = False
   print('')
'''
Test cases in main block
'''
if __name__ == '__main__':
   
   
   '''
   Test 1
   Basic functionality
   Code from the handout.
   '''
   print('Test 1: Basic Functionality')  
   sleep(8)                    # sleep from 12AM to 8AM on Monday
   attend_lecture("CSC", 2)    # attend the CSC lecture for 2 hours,
                               # gain 2*4 = 8 knols
   attend_lecture("MAT", 30)   # attend the MAT lecture for 30 hours,
                               # gain 30*2 = 60 knols (note that since the
                               # student was alert at the start of the
                               # lecture, they gain two knols per hour for
                               # the entire 30 hours)
   print(get_knol_amount())    # should print 68
   print(get_hours_left())     # should print 73 (24 * 5 - 7 - 40)   
   reset_week()                # reset the week for the next test
   
   
   
   '''
   Test 2
   Sleep Function Tests
   '''
   print('\n')
   print('Test 2: Sleep Function')

   #Test for basic functionality
   print('Test 2.1')                   
   sleep(5)
   print('Hours slept:', hours_slept)  # should be 5
   print('Hours left:', hours_left)    # should be 108 (24 * 5 - 7 - 5)
   reset_week()                        # reset the week for the next test

   # Test 2: Call sleep() several times, see if the sleep accumulates.
   print('Test 2.2')
   sleep(5)
   sleep(2)
   sleep(10)
   print('Hours slept:', hours_slept)  # should be 17 (2 + 5 + 10)
   print('Hours left:', hours_left)    # should be 96
   reset_week()                        # reset the week for the next test
   
   # Test 3: Call sleep() with more hours than there are in the workweek.
   print('Test 2.3')
   sleep(200)
   print('Hours slept:', hours_slept)  # should be 0
   print('Hours left:', hours_left)    # should be 113
   reset_week()                        # reset the week for the next test
   
   # Test 4: Call sleep() with more hours than there are in the workweek.
   print('Test 2.4')
   sleep(100)
   sleep(100)  # shouldn't have an effect
   print('Hours slept:', hours_slept)  # should be 100
   print('Hours left:', hours_left)    # should be 13
   reset_week()                        # reset the week for the next test
   


   '''
   Test 3
   Coffee Drinking Test
   '''
   print('\n')
   print('Test 3: Coffee Function')

   #Test for basic functionality
   print('Test 3.1')
   sleep(7)
   drink_coffee()
   print('Last Coffe Time:', last_coffee_time)  # should be 113-7=106
   reset_week()                                 # reset the week for the next test
   
   #Test for crash
   print('Test 3.2')
   drink_coffee()
   sleep(3)
   drink_coffee()
   print('Crash:', coffee_crash)                # should be false because was not less than 3 hours
   reset_week()                                 # reset the week for the next test
   
   #Test for crash
   print('Test 3.3')
   drink_coffee()
   sleep(2)
   drink_coffee()
   print('Crash:', coffee_crash)                # should be true because was less than 3 hours
   reset_week()                                 # reset the week for the next test
