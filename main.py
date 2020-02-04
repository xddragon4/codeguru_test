from chalice import Chalice
import time

app = Chalice(app_name='helloworld')


@app.route('/')
def index():	
	for i in xrange(10):
		app.log.error("fuck")
	time.sleep(100000)
	time.sleep(100000)
    return {'hello': 'world'}