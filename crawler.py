import urllib.request
import util

# util
formatter = util


def get_page(url):
       try:
           return urllib.request.urlopen(url).read().decode('utf-8')
       except:
           return ''

def get_next_target(page):
    start_link = page.find('href=')
    if start_link == -1:
        return None, 0

    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    f = open('C:\\Users\\eduardo.brandes\\Desktop\\Udacity\c.out', 'w')
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            formatter.union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            f.write(page + '\n')
    f.close()
    return crawled

def main():
    url = 'http://www.sulinfoco.com.br/'
    print(crawl_web(url))

# start
main()