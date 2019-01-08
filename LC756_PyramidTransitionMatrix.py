#coding utf-8
def stack_1_layer(bottom,allowed):
    new_bottom = ''
    for i in range(len(bottom)-1):
        ab=bottom[i:i+2]
        if ab in allowed:
            new_bottom+=allowed[ab][0]
            print(allowed[ab][0],end='\t')
            #allowed[ab]=allowed[ab][1:]
            if allowed[ab]=='':
                del allowed[ab]
            print(ab,allowed)
        else:
            print(ab)
            return False
    if len(new_bottom)==1:
        return True
    else:
        return stack_1_layer(new_bottom,allowed)

    return True
def Pyramid_ok(bottom, allowed):
    allow={}
    for i in allowed:
        if i[0:2] not in allow:
            allow[i[0:2]]=i[2]
        else:
            allow[i[0:2]] += i[2]
    print(allow)
    return stack_1_layer(bottom,allow)

def main():
    bottom = "XXYX"
    allowed = ["XXA", "XXY", "XYB", "XYY", "YXA",'ABC','BAC','CCD']
    "CCC"
    allowed=["CBB", "ACB", "ABD", "CDB", "BDC", "CBC", "DBA", "DBB", "CAB", "BCB", "BCC", "BAA", "CCD", "BDD", "DDD", "CCA",
     "CAA", "CCC", "CCB"]
    bottom="CBDDA"
    allowed =["ACC", "ACA", "AAB", "BCA", "BCB", "BAC", "BAA", "CAC", "BDA", "CAA", "CCA", "CCC", "CCB", "DAD", "CCD", "DAB",
     "ACD", "DCA", "CAD", "CBB", "ABB", "ABC", "ABD", "BDB", "BBC", "BBA", "DDA", "CDD", "CBC", "CBA", "CDA", "DBA",
     "ABA"]
    print(Pyramid_ok(bottom, allowed))

if __name__ == '__main__':
    main()