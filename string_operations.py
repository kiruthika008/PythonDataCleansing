# WORD COUNT PROGRAM
def wordcount(mystr):
    #mystr="KIRUTHIKA"
    d={}
    for i in list(mystr):
        d[i]=d.get(i,0)+1
    print(d.get('K'))
    for i,v in d.items():
        print(f"{i}: count {v}")
    return d

def find_element():
    mystr="KIRUTHIKA"
    print(mystr.find('I'))
    print(mystr[:6])

find_element()   

def remove_leading_and_trailing_zero():
    num='0002540020000'
    num_list=list(num)
    for i in num_list:
        if i!='0':
            start_index=num_list.index(i)
            print(start_index)
            break
    for i in num_list[::-1]:
        if i!='0':
            end_index=-num_list[::-1].index(i) #negative index 4 to -4
            print(end_index)
            break
    print(num[start_index:end_index]) 
remove_leading_and_trailing_zero()

def remove_duplicates():
    mystr='Technoloogy'
    print("".join(dict.fromkeys(mystr)))
remove_duplicates()

def remove_duplicates():
    mystr='Technoloogy'
    mystr='Technoloogy'
    print("".join([x for x in mystr if mystr.count(x)==1 ]))
remove_duplicates()



    





