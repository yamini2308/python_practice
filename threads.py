# without threads
import time

def square(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f"Square of {i} is {i*i}")

def cube(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f"Cube of {i} is { i * i * i}")

numbers = [1, 2, 3, 4, 5]

start = time.time()
square(numbers)
cube(numbers)
print("Time taken:", time.time() - start)

#with threading
import time
import threading

def cal_square(numbers):
    print("Calculating Squares...")
    for i in numbers:
        time.sleep(0.2)
        print(f"Square of {i} is {i*i}")

def cal_cube(numbers):
    print("Calculating Cubes...")
    for i in numbers:
        time.sleep(0.2)
        print(f"Cube of {i} is {i*i*i}")

start_time = time.time()

numbers = [1, 2, 3, 4, 5]

# Create threads
t1 = threading.Thread(target=cal_square, args=(numbers,))
t2 = threading.Thread(target=cal_cube, args=(numbers,))

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Time taken with threading:", time.time() - start_time)
