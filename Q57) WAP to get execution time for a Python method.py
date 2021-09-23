import time

# starting time
start = time.time()

for i in range(11):
    time.sleep(0.5)  # sleeping for 1 sec to get 10 sec runtime
    print(i/2)

# end time
end = time.time()

print(f"Execution time of the program {end - start}")
