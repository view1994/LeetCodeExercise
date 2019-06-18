#coding utf-8
import  copy,time
'''
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。

匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''
debug = False
def debug_print(x,debug = False):
    if debug:
        print(x)

def SwitchPattern(p):
    pattern = list(p)
    temp = []
    while pattern:
        pp = pattern.pop()
        if pp == '*':
            z = pattern.pop()
            if z == '.':
                temp.insert(0, '^')
            else:
                temp.insert(0, z.upper())
        else:
            temp.insert(0, pp)
    return temp

def isUpWord(w):
    if not w :
        return False
    elif (ord(w) >= ord('A')) & ( ord(w ) <= ord( 'Z' )):
        return True
    elif w=='^':
        return True
    else:
        return False

##solution1
def ForwardMatch1( s , p ):
    P=p.split('*')
    s=list(s)
    d=[]
    print(P,s,d)
    for j in P[:-1]:
        print('sub_p={},s={}'.format(j, s,d))
        for i in j[:-1]:
            if i=='.':
                d.append(s.pop(0))
            elif i!=s[0]:
                return False
            else:
                d.append(s.pop(0))
        saved=j[-1]
        print('saved={},s={}'.format(saved, s ,d ))
        if s:
            while (s[0]==saved)|(saved=='.'):
                d.append(s.pop(0))
                if len(s)==0:
                    break
        print('saved={},s={}\n'.format(saved, s , s))
    print('\nsub_p={},s={}'.format(P[-1], s ,s))
    for i in P[-1]:
        if s=='':
            return False
        if i == '.':
            d.append(s.pop(0))
        elif s:
            if i != s[0] :
                return False
            else:
                d.append(s.pop(0))
        else:
            return False
    print('s={}'.format(s, s))
    if len(s)!=0:
        return False
    else:
        return True

##solution2
def BackwardMatch(s, p):
    pattern = list( p )
    txst = list( s )
    d = []
    if (pattern==[]) :
        return True if  txst == [] else False
    else:
        pp = pattern.pop()
    if (txst==[]) :
        if (pp != '*' ):
            return False
        else:
            while pp == '*':
                d.append(pattern.pop())
                if pattern == []:
                    return True
                pp = pattern.pop()
            else:
                return False
    while (txst):
        i=txst.pop()
        if pattern == [] :
            if i in d:
                d = d[d.index(i):]
            elif '.' in d:
                d = d[d.index('.'):]
        while pp == '*':
            d.append( pattern.pop() )
            if pattern==[]:
                pp=[]
                break
            pp =pattern.pop()
        #print('i={},\td={},\tpp={},\ttxst={},\tpattern={}'.format(i, d, pp, txst, pattern))
        if i == pp:
            if i in d:
                d = d[ d.index( i ) : ]
            else:
                d = []
            pp= [] if pattern == [] else pattern.pop()
        elif i in d:
            ind = d.index( i )
            d = d[ ind : ]
        elif pp == '.':
            d = []
            pp = [] if pattern == [] else pattern.pop()
        elif '.' in d:
            ind = d.index('.')
            d = d[ind:]
        else:
            return False
    else:
        while pp == '*':
            d.append( pattern.pop() )
            if pattern==[]:
                pp=[]
                break
            pp =pattern.pop()
        if (pp ==[] ) & (pattern == []):
            return True
        return  False

##solution3
def ForwardMatch(s, p):
    txst = list(s)
    pattern = SwitchPattern(p)
    print('pattern = {},\ttxst = {}'.format(pattern,txst))
    d = []
    if ( pattern==[] ) & ( txst==[]):
        return True
    elif( pattern==[] ) & ( txst!=[]):
        return False
    else:
        pp = pattern.pop(0)
    while txst:
        w = txst.pop(0)

        while isUpWord(pp ):
            d.append(pp.lower())
            pp = [] if pattern == [] else pattern.pop(0)
        print('w={}\tpp={}\td={}\ttxst={}\tpattern={}'.format(w, pp, d, txst, pattern))
        if  w == pp:
            if w in d :
                d = d[d.index(w):]
            else:
                d=[]
                pp = [] if pattern==[] else pattern.pop(0)
        elif '^' in d:
            d = d[d.index('^'):]
        elif w in d:
            d = d[d.index(w):]
        elif pp == '.':
            pp = [] if pattern == [] else pattern.pop(0)

        else:
            return False
    else:               #txst==[]       pp有值    pp = pattern.pop(0)
        #print('w={}\tpp={}\td={}\ttxst={}\tpattern={}'.format(w, pp, d, txst, pattern))
        if ( pp !=[] ) & ( not isUpWord(pp)) :
            return False
        while pattern:
            if not isUpWord(pattern.pop(0)):
                return False
        else :
            return True

##solution4
def isMatch4( s , p ):
    print('s={},\tp={}'.format( s , p ) )
    return True if BackwardMatch( s , p ) else ForwardMatch( s , p )

##solution5
def Match1word5(sentence,pattern):        #backword match
    print( 'START-->{: <60}\t{}'.format(str(sentence),str(pattern )))
    i=0
    if ( pattern==[] ) & ( sentence==[]):
        print('return True ---pattern , sentence all empty!')
        return True
    elif( pattern==[] ) & ( sentence!=[]):
        print('return False --- pattern empty , but sentence not empty')
        return False
    else:       #pattern not empty
        d = []
        while pattern:
            pp = pattern.pop()
            if isUpWord( pp ):
                d.append( pp )
            else:
                p = pp
                break
        else:       #patter dose not have any low word
            p = []
    if not sentence :  #sentence empty
        if ( p !=[] )  :
            print('False--sentence empty, and p != []')
            return False
        while pattern:
            if not isUpWord(pattern.pop()):
                print('False--sentence empty, and pattern has low word')
                return False
        else :
            print('return True--sentence empty,and pattern  all up word')
            return True
    else:   #sentence is not empty
        word = sentence.pop()
        print('\t word={},\tp={},\td={}'.format(word, p, d))
        #print('sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        d_saved= copy.deepcopy(d)
        pattern_saved = copy.deepcopy(pattern)
        sentence_saved = copy.deepcopy(sentence)
        if ( word == p) :
            #print('SAVED ==[p=word]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word( sentence, pattern ):
                print('word == p:return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
        if p == '.':
            #print('SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word(sentence, pattern):
                print('p == . :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        if word.upper() in d :
            #print('SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern, word, p, d))
            d = d [ d.index( word.upper()) : ]
            if  p:
                pattern.append(p)
            while d :
                pattern.append( d. pop() )
            if Match1word(sentence, pattern) :
                print('word.upper() in d :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern,word, p, d))

        if '^' in d:
            #print('1SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            d = d[d.index('^'):]
            if  p:
                pattern.append(p)
            while d:
                pattern.append(d.pop())
            #print('2SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            if  Match1word(sentence, pattern):
                print('^ in d :return True')
                return True
            else:
                #print('3SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
                return False
        else:
            print('else false')
            return False


################################################
#solution6
def Match1word6(sentence,pattern):        #backword match
    print( 'START-->{: <60}\t{}'.format(str(sentence),str(pattern )))
    if ( pattern==[] ) & ( sentence==[]):
        #print('return True ---pattern , sentence all empty!')
        return True
    elif( pattern==[] ) & ( sentence!=[]):
        #print('return False --- pattern empty , but sentence not empty')
        return False
    else:       #pattern not empty
        d = []
        while pattern:
            pp = pattern.pop(0)
            if isUpWord( pp ):
                d.append( pp )
            else:
                p = pp
                break
        else:       #patter dose not have any low word
            p = []
    if not sentence :  #sentence empty
        if ( p !=[] )  :
            #print('False--sentence empty, and p != []')
            return False
        else :
            #print('return True--sentence empty,and pattern  all up word')
            return True
    else:   #sentence is not empty
        word = sentence.pop(0)
        #print('\t word={},\tp={},\td={}'.format(word, p, d))
        #print('sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        d_saved= copy.deepcopy(d)
        pattern_saved = copy.deepcopy(pattern)
        sentence_saved = copy.deepcopy(sentence)
        if ( word == p) :
            print('1SAVED ==[p=word]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word( sentence, pattern ):
                #print('word == p:return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
        if p == '.':
            print('2SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word,p, d))
            if Match1word(sentence, pattern):
                #print('p == . :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[p="."]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern, word, p, d))
        if word.upper() in d :
            print('3SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern, word, p, d))
            d = d [ d.index( word.upper()) : ]
            if  p:
                pattern.insert(0,p)
            while d :
                pattern.insert( 0,d. pop(0) )
            if Match1word(sentence, pattern) :
                #print('word.upper() in d :return True')
                return True
            else:
                d = d_saved
                pattern = pattern_saved
                sentence = sentence_saved
            #print('SAVED ==[word.upper() in d]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence,pattern,word, p, d))

        if '^' in d:
            print('4SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            d = d[d.index('^'):]
            if  p:
                pattern.insert(0,p)
            while d:
                pattern.insert(0,d.pop(0))
            #print('2SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
            if  Match1word(sentence, pattern):
                #print('^ in d :return True')
                return True
            else:
                #print('3SAVED ==["^" in d ]== sentence={},\t pattern={},\t word={},\tp={},\td={}'.format(sentence, pattern,word, p, d))
                return False
        else:
            #print('else false')
            return False

def pretreatment(sentence,pattern):
    #预处理，
    #基例
    if ( sentence==[] ) & ( pattern==[]):
        return True
    elif( sentence!=[] ) & ( pattern==[]):
        return False
    elif( sentence==[] ) & ( pattern!=[]):
        while pattern:
            if  not isUpWord(pattern.pop()):
                return False    # patter has  low word
        else:  # patter dose not have any low word
            return True
    elif (sentence != []) & (pattern != []):
        # pop all the upwords in pattern to d , and pop the first lowword to p0
        d = []
        while pattern:
            temp = pattern.pop()
            if isUpWord(temp):
                d.append(temp)
            else:
                p0 = temp
                break
        else:  # patter dose not have any low word, so give p0 an init value '-'
            p0 = '-'
        #pop the next match word in sentence to s0
        s0 = sentence.pop()
        return ( d , s0 , p0 , sentence , pattern )

def match1(s,p):
    #s[0]==p[0]
    debug_print('match1= sentence={},pattern={}'.format(s, p))
    pre = pretreatment( s , p )
    if pre ==True:
        return True
    elif pre == False:
        return False
    else:
        d=pre[0]
        s0 = pre [1]
        p0 = pre [2]
        s_pre = pre[3]
        p_pre = pre[4]
    if s0 == p0 :
        # match the first lowword ,so give up d
        sentence = s_pre
        pattern = p_pre
        return Match1word(sentence,pattern)
    else:
        return False

def match2(s,p):
    #p == '.'
    debug_print('match2= sentence={},pattern={}'.format(s, p))
    pre = pretreatment( s , p )
    if pre ==True:
        return True
    elif pre == False:
        return False
    else:
        d=pre[0]
        s0 = pre [1]
        p0 = pre [2]
        s_pre = pre[3]
        p_pre = pre[4]
    if p0 == '.':
        # match the first lowword '.' , so give up d
        sentence = s_pre
        pattern = p_pre
        return Match1word(sentence,pattern)
    else:
        return False

def match3(s,p):
    #s[0].upper() in d
    debug_print('match3= sentence={},pattern={}'.format(s, p))
    pre = pretreatment( s , p )
    if pre ==True:
        return True
    elif pre == False:
        return False
    else:
        d=pre[0]
        s0 = pre [1]
        p0 = pre [2]
        s_pre = pre[3]
        p_pre = pre[4]
    if s0.upper() in d :
        #
        sentence = s_pre
        pattern = p_pre
        if p0 != '-':
            pattern.append( p0 )
        d = d[d.index(s0.upper()):]
        while d :
                pattern.append( d.pop() )
        return Match1word( sentence , pattern )
    else:
        return False

def match4(s,p):
    #'^' in d
    debug_print('match4= sentence={},pattern={}'.format(s, p),debug)
    pre = pretreatment(s, p)
    if pre == True:
        return True
    elif pre == False:
        return False
    else:
        d = pre[0]
        s0 = pre[1]
        p0 = pre[2]
        s_pre = pre[3]
        p_pre = pre[4]
    if '^' in d:
        #
        sentence = s_pre
        pattern = p_pre
        if p0 != '-':
            pattern.append(p0)
        d = d[d.index('^'):]
        while d:
            pattern.append(d.pop())
        return Match1word(sentence, pattern)
    else:
        return False

#solution7
def Match1word(sentence,pattern):
    s = copy.deepcopy(sentence)
    p = copy.deepcopy(pattern)
    if match1(s,p):
        return True
    s = copy.deepcopy(sentence)
    p = copy.deepcopy(pattern)
    if match2(s,p):
        return True
    s = copy.deepcopy(sentence)
    p = copy.deepcopy(pattern)
    if match3(s,p):
        return True
    s = copy.deepcopy(sentence)
    p = copy.deepcopy(pattern)
    if match4(s,p):
        return True
    else:
        return False

def isMatch(s,p):
    '''
    :param s:str        #待匹配字符串
    :param p:str        #匹配模式
    :return:bool        #返回值
    note：
    '.' 匹配任意单个字符。
    '*' 匹配零个或多个前面的元素。
    '''
    sentence = list(s)
    pattern = SwitchPattern(p)
    debug_print('sentence = {},\tpattern = {},\t'.format( sentence , pattern ) )
    return  Match1word( sentence, pattern )



def main():
    testSample = [
        { 's' : "tccaaaaabsqa" , 'p' : "tc*a*bs.a" , 'result': True},
        dict(s="aaa",  p="ab*a*c*a", result = False),
        dict(s = "missassppi", p="mis*as*p*." ,result = True),
        dict(s = "aab",p="a.*" ,result = True),
        dict(s = "a",p=".*..a*" , result=False),
        dict(s="abbabaaaaaaacaaa" , p="a*.*b.a.*c*b*a*c*a" , result=True),      #417        true
        dict(s="bcaccbbacbcbcab" , p="b*.c*..*.b*b*.*c*", result=True),         #423        true
        dict(s='abcdef' , p='abCEd.f', result=True),
        dict(s='aa',p='a*', result=True),
        dict(s="aab",p="c*a*b", result=True),        #404    TRUE
        dict(s="bbbba",p=".*a*a", result=True),     #407    TRUE
        dict(s="baabbbaccbccacacc",p="c*..b*a*a.*a..*c", result=True),      #429       true
        dict(s="bccbbabcaccacbcacaa", p=".*b.*c*.*.*.c*a*.c", result=False),        # 433    false
        dict(s="bcacaa", p=".*b.*c*.*.*.c*a*.c", result=False),
        dict(s="ccabbaacbcbbabaa",p="bba*ba*.*.a*.*b*a*a", result=False),        #440        false
        dict(s='zxbbbaa',p='bba*ba*.*.a*.*b*a*a' , result=False)
    ]
    t = time.time()
    for i in testSample:
        if isMatch(i['s'], i['p']) != i['result']:
            isMatch(i['s'], i['p'])
        #print(isMatch(i['s'], i['p']),i['result'])
    #print(ForwardMatch(s, p))

    #print( isMatch( s , p ) )
    print('time:',time.time()-t)

if __name__ == '__main__':
    main()


'''
    s , p = "abbabaaaaaaacaaa" , "a*.*b.a.*c*b*a*c*a"
    #s , p = "bcaccbbacbcbcab" , "b*.c*..*.b*b*.*c*"        #423        true
    #s ,p = 'abcdef' , 'abCEd.f'
    s,p='aa','a*'
    #s,p="aab","c*a*b"                                       #404    TRUE
    #s,p="bbbba",".*a*a"                                     #407    TRUE
    #s ,p = "baabbbaccbccacacc","c*..b*a*a.*a..*c"                   #429       true
    #s, p = "bccbbabcaccacbcacaa", ".*b.*c*.*.*.c*a*.c"             # 433    false
    #s, p = "bcacaa", ".*b.*c*.*.*.c*a*.c"
    s,p="ccabbaacbcbbabaa","bba*ba*.*.a*.*b*a*a"           #440        false
    #s,p='zxbbbaa','bba*ba*.*.a*.*b*a*a'                            #false
'''