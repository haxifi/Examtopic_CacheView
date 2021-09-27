from googlesearch import search

"""
    query  : query string that we want to search for.
    tld    : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
    lang   : lang stands for language.
    num    : Number of results we want.
    start  : First result to retrieve.
    stop   : Last result to retrieve. Use None to keep searching forever.
    pause  : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
    Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.
"""
def googleSearch(query):
    cacheProvider = "http://webcache.googleusercontent.com/search?q=cache:"
    for j in search(query, tld="co.in", num=20, stop=200, pause=2):
        print(cacheProvider + j)



if __name__ == '__main__':
    googleSearch("site:examtopics.com intext:practitioner")
