# addition
a = 2+3
print(a)

# multiplication
b = 3*1
print(b)

# linear algebra
a,b,c = 3,1,2

ans = (a+b)/c
print(ans)

print("alice" + "bob")
print("bob" * 55)

my_dict = {}

#manual add to a dictionary
my_dict["bob"] = 56
my_dict["jane"] = 30

# add from a multi dimension list
test_list1 = [["jack","jill","hairy"],[30,19,15]]
i = 0
for item in test_list1:
    if len(test_list1[0]) is len(test_list1[1]):
        my_dict[test_list1[0][i]] = test_list1[1][i]
    i += 1




for i,j in my_dict.items():
    print(i, j)

