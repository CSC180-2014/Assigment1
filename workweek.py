"""The Student Life Simulator starter code.
You should complete every incomplete function,
and add more functions and variables as needed.
Also add comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Sept. 22, 2014

"""


# The total number of hours from 12AM Monday to 5PM Friday.
HOURS_IN_WEEK = 24 * 5 - 7
MIN_SLEEP_PRECENT = 0.3

# Global variables.
hours_slept = 0  # total number of hours that the student has slept so far
hours_left = HOURS_IN_WEEK  # number of hours that remain in the week
knol_total = 0
last_coffee_time = HOURS_IN_WEEK



def knols_per_hour(subj, is_alert):
   subjects = {"CSC": 4,
                "MAT": 2,
                "ESC": 2,
                "PHY": 2,
                "CIV": 2,}
   knols_gained = 0
   knols_gained = subjects[subj]
   if not is_alert:
      knols_gained /= 2

def attend_lecture(subj, hrs):
   if hours_left >= hrs and hrs > 0:
      hours_left -= hrs
      knols_earned = knols_per_hour(subj,is_alert())*hrs

def drink_coffee():
   global last_coffee_time
   global hours_left
   last_coffee_time = hours_left
   return

def is_alert():
   global hours_slept
   global hours_left
   global HOURS_IN_WEEK
   global MIN_SLEEP_PRECENT
   global last_coffee_time
   hours_elapsed = HOURS_IN_WEEK-hours_left
   sleep_percentage=0
    
   if hours_elapsed == 0:
      sleep_percentage=0
      return(False)
   else:
      sleep_percentage = hours_slept/hours_elapsed
      print(sleep_percentage)

   if (sleep_percentage > MIN_SLEEP_PRECENT) or (last_coffee_time-hours_left < 1):
      return(True)
   else:
      return(False)
    
def get_knol_amount():
   global knol_total
   return(knol_total)


def sleep(hrs):
   """
   Update the global variables hours_left and hours_slept by
   respectively subtracting and adding hrs to each one, to account for hrs
   hours of sleep, as long as hrs is non-negative and there are enough
   hours left in the workweek.  Otherwise, do nothing.
   """
    
   # Declare hours_left and hours_slept as global so we can modify
   # these global variables.
   global hours_left, hours_slept
    
   # If hours is negative or there is not enough time in the week, we do
   # nothing and return right away.
   if hrs < 0 or hours_left < hrs:
      return
   else:
      hours_left -= hrs       #NOTE: this is the same as hours_left = hours_left - hrs
      hours_slept += hrs


def get_hours_left():
   """
   Return the number of hours left in the workweek (the amount is stored
   in the variable hours_left, which should be kept up-to-date by the
   other functions).
   """
   global hours_left
   return hours_left


if __name__ == '__main__':
   # You should thoroughly test all of your functions.  Here, we show how
   # to test sleep().
   '''
   # Test 1: Call sleep() once.
   print('Test 1')
   hours_slept = 0  # Note: no need to declare hours_slept global since
                    # we're not inside a function.
   hours_left = HOURS_IN_WEEK
   sleep(5)
   print('Hours slept:', hours_slept)     # should be 5
   print('Hours left:', hours_left)  # should be 108 (24 * 5 - 7 - 5)
   
   # Test 2: Call sleep() several times, see if the sleep accumulates.
   print('Test 2')
   hours_slept = 0
   hours_left = HOURS_IN_WEEK
   sleep(5)
   sleep(2)
   sleep(10)
   print('Hours slept:', hours_slept)     # should be 17 (2 + 5 + 10)
   print('Hours left:', hours_left)  # should be 96
   
   # Test 3: Call sleep() with more hours than there are in the workweek.
   print('Test 3')
   hours_slept = 0
   hours_left = HOURS_IN_WEEK
   sleep(200)
   print('Hours slept:', hours_slept)     # should be 0
   print('Hours left:', hours_left)  # should be 113
   
   # Test 4: Call sleep() with more hours than there are in the workweek.
   print('Test 4')
   sleep(100)
   sleep(100)  # shouldn't have an effect
   print('Hours slept:', hours_slept)     # should be 100
   print('Hours left:', hours_left)  # should be 13
   '''
    

   '''
   # Code from the handout.  It might be useful as a test case (if you
   # want to use it that way).
   #NOTE: it doesn't work yet: you have to implement the appropriate functions!
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
   '''