import json,datetime
class DateEncoder(json.JSONEncoder):
	def default(self,obj):
		if isinstance(obj,datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj,datetime.date):
			return obj.strftime("%Y-%m-%d")
		else:
			json.JSONEncoder.default(self,obj)
print json.dumps(rs,cls=DateEncoder)
