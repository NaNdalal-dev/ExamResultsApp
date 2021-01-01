import sqlite3 as sq
conn=sq.connect('results.db',check_same_thread=False)
class GetResult:

	def __init__(self,uid,course):
		self.uid=uid
		self.course=course
		self.Bsc=['UID','Name','English','Mathematics','Statistics','Java','Total','Percentage','Result']
		self.Bcom=['UID','Name','Accounts','MIS','Economics','English','Total','Percentage','Result']
		self.BBA=['UID','Name','English','Financial Management','Marketing','Organization Behavior','Total','Percentage','Result']
	def getResult(self):
		try:
			with conn:
				c=conn.cursor()
				c.execute(f"""
					SELECT * FROM {self.course} WHERE uid={self.uid}
				""")
				result=c.fetchone()
				result_data=dict()
				if result is None:
					result_data["Error"]= "Invalid UID Number, Please Enter Proper UID and Course."
					return result_data
				if self.course=="Bsc":
					index=0
					for i in self.Bsc:
						result_data[i]=result[index]
						index+=1
				elif self.course=="Bcom":
					index=0
					for i in self.Bcom:
						result_data[i]=result[index]
						index+=1
				elif self.course=="BBA":
					index=0
					for i in self.BBA:
						result_data[i]=result[index]
						index+=1
				else:
					return "Invalid Course"
				result_data["Error"]=None
				return result_data

		except sq.OperationalError as sqO:
			return f"Invalid Table name : {self.course}"
	def get_failures_data(self):
		with conn:
			c=conn.cursor()
			c.execute(f"""
				SELECT uid,name FROM {self.course} WHERE Result="Fail"
			""")
			result=c.fetchall()
			return result
	def get_passed_data(self):
		with conn:
			c=conn.cursor()
			c.execute(f"""
				SELECT uid,name FROM {self.course} WHERE Result="Pass"
			""")
			result=c.fetchall()
			return result
