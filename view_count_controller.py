from flask import Flask
import json
from view_count import ViewCount
from view_count_fetch import RunLoop
import multiprocessing

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

runloop = RunLoop()
runloop.start()

@app.route('/view/count/xueqiu')
def get_view_count_xueqiu():
    #return json.dumps(ViewCount.xueqiu_count,ensure_ascii=False)
    pass

@app.route('/view/count/jinritoutiao')
def get_view_count_jinritoutiao():
    return json.dumps(ViewCount.toutiao_count,ensure_ascii=False)

@app.route('/view/count')
def hello():
    return "hello"

if __name__ == '__main__':
    app.run()
    
    p = multiprocessing.Process(target=hello)
    p.start()
    p.join(10800)
    
    if p.is_alive():
        print("running... let's kill it...")
        p.terminate()
        p.join()
    