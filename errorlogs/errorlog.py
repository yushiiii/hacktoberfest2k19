def readfile():
    fo=open("/home/shivam/Documents/test.txt","r")
    lines=fo.read().split("\n")
    fo.close()
    str="System.err:"
    words=[]
    st=[]
    li=[]
    s=[]
    comp=[]
    count=0
    l={}
    trace=dict()
    temp=""
    y=""
    component=[]
    count=0
    for i in range(0,len(lines)):
        if str in lines[i]:
            if lines[i] not in words:
                words.append(lines[i].split())
    for i in words:
        pid=i[2]
        tid=i[3]
        print("pid=",pid, )
        print("tid=",tid, ) 
        print("i[6]=",i[6], )
        if "Exception" in i[6]:
            ex=i[6]
            print("ex=",ex, )
            del li[:]
            if len(s)!=0:
                print("\n")
                print("Stack trace")
                for x in s:
                    for k in x:
                        print(k, )
                    print()
                print()
            print("\n")
            li=i[6].split(".")
            print(li[2])
            if i not in s:
                s.append(i)
            del li[:]
            del s[:]
        else:
            if i not in s:
                s.append(i)
            if len(s)>2:
                continue
            li=i[7].split(".")
            print("i[7]",i[7])
            print("li=",li)
            x=consplit(li)
            print("\nComponent:",x)
            temp=x
            print("temp=",temp, )      
            print("File:",li[-3],".java")
            print("Function:",li[-2],"()")
            for x in range(0,len(li[-2])):
                if li[-2][x]=="(":
                    break
                else:
                    y=""+li[-2][x]
                    print(y, )
            print("()")
            print("Line number: ", )
            for x in range(0,len(li[-1])-1):
                if li[-1][x].isdigit():
                    print(li[-1][x], )
            print()
            count=count+1
        if ex in l.keys():
            l.update({ex:count})
        else:
            l.update({ex:1})
    print("\nErrors:\n")
    for i,j in l.items():
        if "Exception" in i:
            if ":" in l.keys():
                print(i, )
            else:
                print(i,":")
            print(j)
            print()
        
def consplit(x):
    y=""
    for i in range(0,3):
        y=y+""+x[i]+"."
    return y

readfile()
