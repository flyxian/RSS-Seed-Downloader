
#! -*- coding: utf-8 -*-
'''
Created on Aug 21, 2011

@author: flyxian
'''
debug = 1

import substr_find

<<<<<<< HEAD
test_kwl = [["èŠ±å¼€", "è½»ä¹‹å›½åº¦"],
            ["ç¾Žé£Ÿ", "mkv", "å¼‚åŸŸå­—å¹•ç»„"]]
=======
test_kwl = [["花开", "轻之国度"],
            ["美食", "mkv", "异域字幕组"]]
>>>>>>> release-0.4

#keyword list, if without initialization use test_kwl
keywords_list = test_kwl

def init_keywords_list(filename="keywords"):
    fp = open(filename, "r")
    lines = fp.readlines()
    fp.close()
    
    global keywords_list
    keywords_list = []
    for line in lines:
        if line[0] == "#" or len(line) == 0:
            continue
        
        if debug > 2:
            print line.strip()
            
        words = unicode(line.strip().lower(), 'utf-8').split(" ")
        keywords_list.append(words)
        
    if debug > 3:
        print keywords_list

def check_keywords(keywords, title):
    counter = 0
    checkee = title.lower()
    kw_flags = []

    for word in keywords:
        if debug > 3:
            print "Checking: %s" % word
#        if checkee.encode("utf-8").find(word) >= 0:
#            counter += 1
<<<<<<< HEAD
        if checkee.find(word) >= 0:
#        if substr_find.find(checkee, word):
=======
#        if substr_find.find(checkee, word):
        if checkee.find(word) >= 0:
>>>>>>> release-0.4
            counter += 1
            if debug > 1:
                kw_flags.append(True)
        else:
            if debug > 1:
                kw_flags.append(False)
                
    
    if counter == len(keywords):
        return True
    else:
        if debug > 1 and counter == len(keywords) - 1:
            print "Miss matched keywords:",
            for i in range(0,len(kw_flags)):
                if not kw_flags[i]:
                    print "[%d]%s" % (i,keywords[i]),
            print " "
        return False
    
def check(text):
#    print text
    for keywords in keywords_list:
        if check_keywords(keywords, text):
            return True
    #no match
    return False



if __name__ == "__main__":
    print "keyword_filter: Hello world."
    init_keywords_list()
<<<<<<< HEAD
    print check("[è½»ä¹‹å›½åº¦][é�’ä¹‹é©±é­”å¸ˆ][ç¬¬22è¯�][GB][480P][MP4]")
=======
    print check("[轻之国度][青之驱魔师][第22话][GB][480P][MP4]")
    
>>>>>>> release-0.4
    