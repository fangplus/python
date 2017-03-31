#---coding:utf-8---
#此代码在pyhton2.7上测试的
import urllib2
import json
def API_get(htmls):
    ranking = 1
    for html in htmls:
        try:
            web_data = urllib2.urlopen(html)
            hjson = json.loads(web_data.read())
        except Exception as error:
            print error
        for key in hjson['subjects']:
            print str(ranking) + ' : ' + key['title'] + ',' + key['year'] + ',' + str(key['rating']['average'])
            ranking+=1
if __name__ == "__main__":            
    htmls = ['https://api.douban.com/v2/movie/top250?start={}'.format((page-1)*20)for page in range(1,6)]
    API_get(htmls)
