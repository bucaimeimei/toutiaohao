#---*--- coding:utf-8 ---*---

import json
from view_count import ViewCount
from threading import Timer
import threading
import urllib

class ViewCountFetch:
    def count_toutiao():
        url = 'https://i.snssdk.com/api/feed/profile/v1/?category=profile_article&visited_uid=5800776838&stream_api_version=82&offset=0&version_code=700&version_name=70000&device_platform=android&user_id=5800776838&media_id=5800776838&request_source=1&active_tab=dongtai&visit_user_id=0&device_id=50465333489&iid=52394141321'
        req=urllib.request.urlopen(url)#向url发送请求，并传送表单data#获取响应
        req_data=req.read()#解析#
        req_data = req_data.decode('utf8')
        dict_data = eval(req_data.replace('null','None').replace('true','True').replace('false','False'))
        data = dict_data['data']
        title = []
        read_count =[]
        
        for i in range(0,20):
            content = data[i]['content']
            content_dict = eval(content)
            title.append(content_dict['title'])           
            read_count.append(content_dict['read_count'])       
        print(title)
        print(read_count)
        #保存数据 
        view_count_list = dict(zip(title,read_count))  #{'title':title,'read_count':read_count}
        ViewCount.toutiao_count = view_count_list
        print(ViewCount.toutiao_count)
        
  
class CallBack():
    content = ''
    view_count_list = []
    def firstCallFunc(self,content):
        #print(content)
        self.content = content

    def nextCallFunc(self,content):
        json_content = json.loads(content)
        articles = json_content['list']
        for article in articles:
            title = article['title']
            view_count = article['view_count']
            _dict = {'title' : title, 'view_count' : view_count}
            self.view_count_list.append(_dict)   
            

class RunLoop(threading.Thread):

    def __init__(self):
        super(RunLoop,self).__init__()

    def run(self):
        self.loopfunc()

    def loopfunc(self):
        #v = ViewCountFetch()
        #v.count_toutiao()
        ViewCountFetch.count_toutiao()
        Timer(60*3, self.loopfunc).start()
        print('aba')

        
      

    
    
    
    
    
    