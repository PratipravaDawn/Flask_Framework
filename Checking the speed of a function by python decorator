import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper_fun():
      print(f"{function.__name__} run speed:")
      diff = function()-current_time
      print(diff)
  return wrapper_fun
    
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
  return time.time()
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
  return time.time()
  
fast_function()
slow_function()
