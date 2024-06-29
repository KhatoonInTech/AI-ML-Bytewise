# iterator class `Countdown`
class Countdown():
    """
  An iterator class that counts down from a given start number to 0.
  """
    def __init__(self,starting_num):
        """
         Initializes the Countdown object with the starting number.

        Args:
          start_number (int): The number to start counting down from.
        """

        self.current_num=starting_num


    def __iter__(self):
        """
         Returns the Countdown object itself as the iterator.
        """
        return self    
    def __next__(self):
        """
        Returns the next number in the countdown sequence.

        Raises:
            StopIteration: If the current number reaches 0.
         """
        if self.current_num >0:
            next_num=self.current_num
            self.current_num-=1
            return next_num
        else:
            raise StopIteration
            
#fibonacci_generator
def fibonacci_generator(n):
    '''
    The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers. Starting from 0 and 1, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, ...
    '''
    if not all( dig.isdigit() for dig in str(n)):
        raise ValueError ("Please enter a number only")
    a,b=0,1
    while a <=n :
       yield a
       a,b=b,a+b
      

    

# random_number_generator
import random as r
def  random_number_generator(start,end):
  """
  Generates a random integer between a specified minimum and maximum value (inclusive).

  Args:
      min_value (int): The minimum value for the random number.
      max_value (int): The maximum value for the random number.

  Returns:
      int: A random integer within the specified range.

  Raises:
      ValueError: If the minimum value is greater than the maximum value.
  """
  if start>=end:
      raise ValueError ("The starting index of the range must be smaller than the ending index. ")
  rand=r.randint(start,end)
  yield rand
  
  #main program.....
  # >>>demonstrating Countdown Class
stopwatch= Countdown(13)
print("\nfetching values from generator via .__next__() \n")

print(f"{stopwatch.__next__()}\n")

#second way of using this class is as follows
print("\nContinuing fetching values from iterating class via loop\n")

for i in stopwatch:
    print(f"{i}")

#demostrating fibonacci generator function
fg=fibonacci_generator(13)
print("\nfetching values from generator via NEXT function\n")
print(next(fg))
print(next(fg))
print("\nContinuing fetching values from generator via loop\n")
#another way to demonstrate fibonacci generator
for i in fg:
    print(i)

#demonstrating Random Number generator function
mynum=random_number_generator(6,10)

print("\nfetching values from generator via NEXT function\n")
print(next(mynum))
