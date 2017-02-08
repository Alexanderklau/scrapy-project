# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
import random
from .user_agent import agents
class userAgentMiddleware(object):
    def process_agent(self,request,spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent









# if __name__ == '__main__':