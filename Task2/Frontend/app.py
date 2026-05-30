from flask import Flask,request,render_template
import requests


app=Flask(__name__)

BACKEND_URL='http://0.0.0.0:5000'

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
    requests.post(BACKEND_URL + '/submit',json=form_data)
    return 'Submission Successful'

if __name__=='__main__':
    app.run(debug=True, port=8000,host='0.0.0.0')