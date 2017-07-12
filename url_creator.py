gindex=0


def smallurl(url):
    global gindex

    letters=list('ABCDEFabcdef')
    url_new=letters[gindex]
    gindex+=1
    return 'this is your new url ' + url + " " + url_new


if __name__=="__main__":
    print (smallurl('ass'))
    print (smallurl("bbb"))

