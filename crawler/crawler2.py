import urllib.request 
import urllib.parse
import http.cookiejar
url= "http://a.hi96999.com/business_login.html"
postdata=urllib.parse.urlencode({
	"username":"96999",
	"password":"123456"
}).encode('utf-8')
req=urllib.request.Request(url,postdata)
data=urllib.request.urlopen(req).read()
fl=open("C:/Users/chenzhen/Desktop/py/crawler/1.html","wb")
fl.write(data)
fl.close()
print(data)

