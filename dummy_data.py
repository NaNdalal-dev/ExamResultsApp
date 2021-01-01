import random as r
import pandas as pd
import sqlite3 as sq
df=pd.read_csv('names.csv')
con=sq.connect('results.db')
def mark_sheet():
	marks=[]
	flag=1
	total=0
	for i in range(4):
		random_marks=[r.randint(10,34),r.randint(35,99)]
		res=r.choices(random_marks,weights=[5,80])[0]
		marks.append(res)
		total+=res
		if res<35:
			flag=0
	if flag==1:
		result='Pass'
	else:
		result='Fail'	
	percentage=(total/400)*100
	final_result={
	'Marks':marks,
	'Result':result,
	'Total':total,
	'Percentage':round(percentage,2)
	}
	return final_result
def Insert(uid_start,course="Bcom"):
	names=list(df['Names'])
	r.shuffle(names)
	for i in range(100):
		final_result=mark_sheet()
		final_result['UID']=uid_start
		final_result['Name']=names[i]
		c=con.cursor()
		try:
			c.execute(f"""
			INSERT INTO {course} VALUES({final_result['UID']},'{final_result['Name']}',
			{final_result['Marks'][0]},
			{final_result['Marks'][1]},
			{final_result['Marks'][2]},
			{final_result['Marks'][3]},
			{final_result['Total']},{final_result['Percentage']},'{final_result['Result']}')
			""")
		except sq.IntegrityError as sqI:
			return "Error These UIDs already exists"
		except:
			return "Opps something went wrong check the table names."
		con.commit()
		uid_start+=1
#Insert(3001,"BBA")
