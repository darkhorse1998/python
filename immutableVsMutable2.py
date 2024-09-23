def sortNumbers(nums: list) -> None:
    nums.sort()

def sortedNumbers(nums1: list) -> list:
    return sorted(nums1)

list1 = [99,1,2,7,3]
list2 = [79,32,7897,1]

print("Sort")
print(list1)
sortNumbers(list1)
print(list1)
print("Sorted...")
print(list2)
print(sortedNumbers(list2))