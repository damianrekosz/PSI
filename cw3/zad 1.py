def merge(a_list, b_list):
    out = list()
    if (len(a_list) >= len(b_list)):
        for i in range(len(a_list)):
           if i%2 == 0:
               if (i < len(a_list)):
                   out.append(a_list[i])
           else:
               if (i < len(b_list)):
                   out.append(b_list[i])
    else:
        for i in range(len(b_list)):
           if i%2 == 0:
               if (i < len(a_list)):
                   out.append(a_list[i])
           else:
               if (i < len(b_list)):
                   out.append(b_list[i])

    return out

a_list = (1,2,3,4,5,6,7,8)
b_list = ('a','b','c','d','e','f','g')
print(merge(a_list, b_list))