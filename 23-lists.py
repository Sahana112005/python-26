
arr = [12, 35, 1, 10, 34, 1]

largest = -1
second_largest = -1

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element is:", second_largest)




arr = [4, 3, 2, 7, 8, 2, 3, 1]

print("Duplicate elements:")
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])


arr = [1, 2, 4, 5, 6]  # 3 is missing
n = 6
expected_sum = (n * (n + 1)) // 2

actual_sum = 0
for num in arr:
    actual_sum += num

missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)



arr = [1, 0, 2, 3, 0, 4, 0, 5]

insert_pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[insert_pos] = arr[i]
        insert_pos += 1
while insert_pos < len(arr):
    arr[insert_pos] = 0
    insert_pos += 1
print("Array after moving zeros:", arr)




arr = [10, 20, 35, 50, 75]
target_sum = 70
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target_sum:
            print("Pair found:", arr[i], "and", arr[j])





start = 1
end = 10
total_sum = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        # Check factors
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total_sum += num

print("Sum of primes in range:", total_sum)









