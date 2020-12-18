all_inp = []
file = open("input.txt", "r")
for i in file:
    i = i.strip("\n")
    all_inp.append(i)
final_count = 0

for inp in all_inp:
    #inp_info1 = inp[0:3]
    ##inp_info2 = inp[3:-0]
    #print(inp_info1)
    #print(inp_info2)
    inp_split = inp.split(" ")
    inp_split2 = inp_split[0].split("-")
    most = int(inp_split2[1])
    lease = int(inp_split2[0])
    word = inp_split[1]
    word = word[0]
    count = 0
    for i in inp_split[2]:
        if i == word:
            count += 1
    if lease <= count <= most:
        print("count" + str(count))
        final_count += 1
    else:
        print("not valid")
sum = len(all_inp) - final_count
print("\nthere is " + str(final_count) + " valid password \nthere is " + str(sum) + " non valid password")
