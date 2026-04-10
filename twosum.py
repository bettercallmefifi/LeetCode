from typing import List
def twoSum( nums: List[int], target: int) -> List[int]:
	i = 0
	while i < len(nums):
		j = i + 1
		while j < len(nums):
			if nums[i] + nums[j] == target:
				return [i, j]
			j += 1
		i += 1
	return 0
print(twoSum([3,2,4], 6))

def lengthOfLastWord(s: str) -> int:
	thislist = []
	[len(s.split(" ")) -1]
	p = s.split(" ")
	for i in p:
		if i != '':
			thislist.append(i)
	return len(thislist[len(thislist) - 1])
print(lengthOfLastWord("luffy is still joyboy"))

def isHappy(n: int) -> bool:
	p = str(n)
	thislist = []
	for i in p:
		thislist.append(i)
	p = sum(pow(int(i), 2) for i in thislist)
	if p == 1:
		return True
	elif p > 10:
		return isHappy(p)
	else:
		return False

print(isHappy(7))