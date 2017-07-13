

def make_smallurl():
    counter=0
    url_new = ''
    def smallurl(url):
        nonlocal counter, url_new
        counter = counter + 1
        url_new = 'this is your new url ' + url + " " + str(counter)
        return url_new
    return smallurl



if __name__=="__main__":
    sml=make_smallurl()
    print (sml('ass'))
    print (sml('assdd'))
    print (sml('assrete'))
    print (sml('asshhvdd'))
    print (sml('asyr54s'))
    print (sml('assdgd4dd'))
    print(sml('assdgd4dd'))
    print(sml('assdgd4dd'))
    print(sml('assdgd4dd'))
    print(sml('assdgd4dd'))


