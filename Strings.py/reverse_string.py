# Problem:
# Input: "hello"
# Output: "olleh"
# Methods:
# •	Python slicing
# •	loop from end

# Using python slicing:

a = "hello"
rev = a[::-1]
print(rev)

# using loop from end:

a = "hello"
rev = ""
for i in range(len(a)-1, -1, -1):
    rev = rev+a[i]
print(rev)
