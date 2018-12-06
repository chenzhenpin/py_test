from flask import Flask ,render_template
from selenium import webdriver
import time, threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')
def openWeb():
	#time.sleep(0.1)
	url = 'http://localhost:5000/'
	driver = webdriver.Firefox()
	#driver = webdriver.Chrome()
	driver.get(url)
if __name__ == '__main__':
	t = threading.Thread(target=openWeb, name='LoopThread')
	t.start()
	app.run()

