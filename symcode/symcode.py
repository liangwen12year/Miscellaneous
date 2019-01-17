



if __name__ == '__main__':
    file=open("/home/wliang/Desktop/symcode/test.txt", "r")
    symcode = ['s', 'y', 'm', 'a', 'n', 't', 'e', 'c']
    content = file.readline()
    print(content)
    print(list(content))
    pp= list(content)
    i=0
    # if len(pp) % 3 == 0:
    #
    # elif len(pp) % 3 == 1:
    #
    # else:




    while(i<len(pp)-1):


        if i+2 > len(pp)-1:
            t1 = format(ord(pp[i]), '08b')
            t2 = format(0, '08b')
            t3 = format(0, '08b')
            splited = t1 + t2 + t3
            list_result = list(splited)
            j = 0
            while (j < 22):
                t4 = list_result[j] + list_result[j + 1] + list_result[j + 2]
                index = int(t4, 2)
                print(symcode[index])
                j = j + 3





        if i+2 == len(pp)-1:
            t1 = format(ord(pp[i]), '08b')
            t2 = format(ord(pp[i + 1]), '08b')
            t3 = format(0, '08b')
            splited = t1 + t2 + t3
            list_result = list(splited)
            j = 0
            while (j < 22):
                t4 = list_result[j] + list_result[j + 1] + list_result[j + 2]
                index = int(t4, 2)
                print(symcode[index])
                j = j + 3



        if i+2 < len(pp)-1:
            t1=format(ord(pp[i]), '08b')
            t2=format(ord(pp[i+1]),'08b')
            t3 =format(ord(pp[i + 2]), '08b')
            splited=t1+t2+t3
            list_result = list(splited)
            j=0
            while(j<22):
                t4=list_result[j]+list_result[j+1]+list_result[j+2]
                index = int(t4, 2)
                print(symcode[index])
                j=j+3

        i+=3

    #while(pp[i]!=' ' and pp[i]!='\n'):

    # test = "MACBETH"
     #symcode=['s','y','m','a','n','t','e','c']
    #
    # print(test)
    # print(ord('g'))
    # print(ord('i'))
    # print(ord('m'))
    # #print(bin(97))
    # test1= format(103, '08b')
    # print(test1)
    #
    # test2 = format(105, '08b')
    # print(test2)
    #
    # test3 = format(109, '08b')
    # print(test3)
    #
    # print(test1+test2+test3)
    # splited = test1+test2+test3
    # print(list(splited))
    # list_result=list(splited)
    # test4=list_result[0] + list_result[1] + list_result[2]
    # print(list_result[0]+list_result[1]+list_result[2])
    # print(int(test4,2))
    # index=int(test4,2)
    # print(symcode[index])
    #print content
