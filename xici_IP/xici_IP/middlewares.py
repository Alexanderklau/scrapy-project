__author__ = 'Yemilice_lau'
import base64

# Start your middleware class
class ProxyMiddleware(object):
 # overwrite process request
 def process_request(self, request, spider):
  # Set the location of the proxy
  request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
  # Use the following lines if your proxy requires authentication
  proxy_user_pass = "USERNAME:PASSWORD"
  # setup basic authentication for the proxy
  encoded_user_pass = base64.encodestring(proxy_user_pass)
  request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

# 2.在项目配置文件里(./project_name/settings.py)添加
#
# DOWNLOADER_MIDDLEWARES = {
#  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#  'project_name.middlewares.ProxyMiddleware': 100,
# }

