# encoding: utf-8
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

dic = dict(name = "中文")
# name.decode("utf-8")
# name.encode("utf-8")
# print name
json_data = json.dumps(dic)
data = json.loads(json_data.encode("utf-8"))

print data