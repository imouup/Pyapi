import json
import requests
# import ssl
# from requests.adapters import HTTPAdapter
# from urllib3.poolmanager import PoolManager
#
#
# # 定义一个继承自 HTTPAdapter 的自定义 Adapter
# class CustomHttpAdapter(HTTPAdapter):
#     def init_poolmanager(self, connections, maxsize, block=False):
#         # 创建一个自定义的 SSL 上下文
#         # 'ALL' 表示接受所有服务端支持的加密算法
#         # @SECLEVEL=1 降低了安全等级（默认为2），允许一些老旧但仍被部分服务器使用的算法
#         ctx = ssl.create_default_context()
#         ctx.set_ciphers('ALL:@SECLEVEL=1')
#
#         self.poolmanager = PoolManager(
#             num_pools=connections,
#             maxsize=maxsize,
#             block=block,
#             ssl_context=ctx
#         )
#
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
#     'Cookie':'JSESSIONID=0FE08A83FA1E9DC98A42F02F4C214558; clwz_blc_pst_SeuSx2dPortal=872097482.20480; Hm_lvt_39f7b5f548f7f7295c97c7f3517d1077=1758719186,1758720498,1758722380; HMACCOUNT=C7888A8BCFDB58B4; Hm_lpvt_39f7b5f548f7f7295c97c7f3517d1077=1758726239',
#     'Content-Type': 'application/json;charset=UTF-8',
#     'Origin': 'https://my.scut.edu.cn',
#     'Referer': 'https://my.scut.edu.cn/up/view?m=up'
# }
# payload = {
#   "mapping": "getAllPimList",
#   "pageNum": 1,
#   "pageSize": 10,
#   "PIM_TITLE": "",
#   "TYPE_NAME": "事务通知",
#   "BELONG_UNIT_NAME": "",
#   "START_TIME": "",
#   "END_TIME": ""
# }
#
# url = 'https://my.scut.edu.cn/up/up/pim/allpim/getAllPimList'
#
# # --- 使用自定义 Adapter ---
# # 创建一个 session 对象
# session = requests.Session()
#
# # 将我们的自定义 Adapter 挂载到 https:// 协议上
# session.mount('https://', CustomHttpAdapter())
#
# # 使用 session 对象发送请求，而不是直接用 requests.post
#
# re = session.post(url, headers=headers, json=payload)
# re.raise_for_status()  # 检查请求是否成功
# js = re.json()
# print(js)


re = requests.get('http://127.0.0.1:5000/scut/myscut_notice', params={'name': 'myscut_gw'})
te = re.text
print(te)



