import sqlite3 as sq
from flask import*
from get_data import GetResult
app=Flask(__name__)
@app.route('/')
def res():
	a=GetResult(1100,'Bsc')
	note=['Bsc UIds: 1001-1100','Bcom UIDs: 2001-2100','BBA UIDs: 3001-3100']
	show=False
	return render_template("index.html",show=show,note=note)
@app.route('/',methods=['POST'])
def get_res():
	uid=request.form['uid']
	course=request.form['course']
	result=GetResult(uid,course)
	result=result.getResult()
	if result['Error'] is None:
		keys=list(result.keys())
		st_details=keys[0:2]
		marks_details=keys[2:6]
		final_result=keys[6:8]
		res=keys[8]
		note=None
		return render_template("index.html",title=uid,note=note,st_details=st_details,marks_details=marks_details,final_result=final_result,res=res,result=result,show=True)
	note=['Bsc UIds: 1001-1100','Bcom UIDs: 2001-2100','BBA UIDs: 3001-3100']
	return render_template("index.html",result=result,show=True,note=note)
if __name__=='__main__':
	app.run(debug=True)
