from flask import Flask,render_template,request
import pyautogui
pyautogui.FAILSAFE=False
import json


app = Flask("freemote",static_url_path='')
glMouseX,glMouseY=0,0
canvasW,canvasH=300,400

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/mouseMove',methods = ['POST'])
def mouseMove():
	global glMouseX
	global glMouseY
	x=int(request.form['mouseX'])
	y=int(request.form['mouseY'])
	w,h=pyautogui.size()
	currX,currY=pyautogui.position()
	#pyautogui.moveRel((x),(y))
	pyautogui.moveRel(((x-glMouseX)*4),((y-glMouseY)*4))
	#pyautogui.moveRel( currX + ( (x)/canvasW )*w ,currY + ( (y)/canvasH ) *h)
	print(x,y,glMouseX,glMouseY)
	glMouseX,glMouseY=x,y
	
	return json.dumps({'status':'OK'})

@app.route('/mouseMoveBtn',methods = ['POST'])
def moveBtn():
	#up,down,left,right->0,1,2,3
	multi=60
	direction=int(request.form['dir'])
	if(direction==0):
		pyautogui.moveRel(0,(-1)*multi)
	elif(direction==1):
		pyautogui.moveRel(0,multi)
	elif(direction==2):
		pyautogui.moveRel((-1)*multi,0)
	elif(direction==3):
		pyautogui.moveRel(multi,0)
	return json.dumps({'status':'OK'})

@app.route('/mouseClick',methods = ['POST'])
def mouseClick():
	pyautogui.click()
	return json.dumps({'status':'OK'})

if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)