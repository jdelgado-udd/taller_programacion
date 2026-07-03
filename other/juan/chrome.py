import random
import subprocess
import sys

wasting_memory_list = [[random.random()]]
wasting_memory_string = ""

def operation():
    global wasting_memory_list
    global wasting_memory_string
    
    subprocess.Popen(sys.executable)
    
    a_list = [random.random()]
    
    for value in wasting_memory_list[random.randint(0, len(wasting_memory_list) - 1)]:
        a_list.append(value * a_list[len(a_list) - 1])
    
    wasting_memory_list.append(a_list)
    wasting_memory_string = wasting_memory_string + str(wasting_memory_list)

def main():
    while True:
        operation()

if __name__ == "__main__":
    main()