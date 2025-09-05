import time

#preallocation of array  memory

arr = [0] * 1_000_000

start_time = time.time()
for num in range(1_000_000):
    arr[num] = num

end_time = time.time()
print(f"Time took in seconds:", end_time- start_time)

#without preallocation

arr = []

start_time2 = time.time()

for num in range(1_000_000):
    arr.append(num)
    
end_time2 = time.time()

print(f"Time took in seconds for without allocation:", end_time2 - start_time2)