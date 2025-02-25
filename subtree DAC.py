
path = '*'
max01= -99999999
tree = "5 2 -1 + + 21 1 -3 + -1 + + + *" # example tree 
list_tree = []
for el in tree.split(" ") :
    if el == "*":
        continue
    list_tree.append(el)
length1 = len(list_tree)-1
def subtree(list, length , path):

    global max01
    length -= 1
    i=length
    sub_right =[]
    sub_left=[]
    counter=1
    global b
    part_a =0
    part_b = 0
    if len(list)==3: # two leafs checking
        k=len(list)-1
        sub_right.append(int(list[k-1]))
        sub_left.append(int(list[k-2]))
        if max01 < sub_right[0] < sub_left[0] or sub_right[0] < max01 < sub_left[0]:
            max01 = sub_left[0]
            b =path + '0'
        if max01 < sub_left[0] < sub_right[0] or sub_left[0] < max01 < sub_right[0]:
            max01 = sub_right[0]
            b =path + '1'

    else:
        path += "1" # entering right subtree to find maximum
        while (counter != 0):
            if (list[i] == '+'):
                sub_right.append(list[i])
                counter += 1
            else:
                sub_right.append(int(list[i]))
                part_a += int(list[i])
                counter -= 1
            i -= 1
        sub_right.reverse()
        if (max01 < part_a):
            max01 = part_a
            b = path
        if len(sub_right) > 1:
            subtree(sub_right, len(sub_right) - 1 , path )
        path = path[: -1] # entering left subtree to find maximum
        path += '0'
        counter = 1
        while (i >= 0):
            if (list[i] == '+'):
                sub_left.append(list[i])
                i -= 1
                continue
            else:
                sub_left.append(int(list[i]))
                part_b += int(list[i])
            i -= 1
        sub_left.reverse()
        if ( max01<part_b ):
            b = path
            max01 = part_b
    if len(sub_left) > 1:
       subtree(sub_left, len(sub_left)-1 , path )
    if max01 < part_b + part_a :
        max01 = part_a + part_b
        b = path[: -1]
    return max01
    return b

subtree(list_tree ,length1 , path )
print("maximum subtree is : ", max01)
print("the path is : ", b)