#Write a Python function that takes two lists and returns True if they have
#at least one common member
#a =[1, 2, 3, 4, 5]
#b =[6, 7, 8, 9]
#False

def test_includes_any(nums, lsts):
    for x in lsts:
        if x in nums:
            return True
    return False
print(test_includes_any([10, 20, 30, 40, 50, 60], [22, 42]))
print(test_includes_any([10, 20, 30, 40, 50, 60], [20, 80]))

