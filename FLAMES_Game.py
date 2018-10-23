f_n=input("Enter the name of the first person\n")

f_n=f_n.replace(' ','')         #Removing Space
s_n=input("Enter the name of the second person\n")
s_n=s_n.replace(' ','')         #Removing Space

#identify which name has more character

if len(f_n)>=len(s_n):
    f_n_list=list(f_n)
    s_n_list=list(s_n)
else:
    f_n_list=list(s_n)
    s_n_list=list(f_n)

#get flames count

def Flamescount(f_n_list,s_n_list):
    f_temp=[]
    for char in f_n_list:
        if char in s_n_list:
            f_temp.append(char)
            s_n_list.remove(char)
    for c in f_temp:
        f_n_list.remove(c)

    finallist=f_n_list+s_n_list
    flamescount=len(finallist)
    return flamescount

def flameresult(count):
    string='FLAMES'

    while len(string)>1:
        test_count=count%len(string)        #get position to remove char
        if test_count==0:
            string=string.replace(string[-1],'')
        else:
            first_var=string[test_count:]       #identifying first char for next loop
            first_var_swap=string.replace(first_var,"")
            string=string.replace(string[-1],'')
    result=string
    return result

flamescount=Flamescount(f_n_list,s_n_list)
flame_result=flameresult(flamescount)

flames_dict={'F':'Friends','L':'Love','A':'Attraction','M':'Marriage','E':'Enemies','S':'Siblings'}
print(flames_dict[flame_result])