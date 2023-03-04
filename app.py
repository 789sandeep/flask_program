from flask import Flask , render_template, request,jsonify
app = Flask(__name__,template_folder='template')


@app.route("/",methods=['GET','POST'])
def home_page1():
    return render_template("index.html")


@app.route("/math",methods=['POST'])
def math_opration():
    if(request.method=='POST'):
        op=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if op=='add':
            r=num1+num2
            result=str(r)
        elif op=="subtract":
              r=num1-num2
              result=str(r)
        elif op=="divide":
              r=num1/num2
              result=str(r)
        elif op=="multiply":
              r=num1*num2
              result=str(r)          
    return render_template("result.html",result=result)

# @app.route("/")
# def home_page():
#     return "hello,word"

if __name__=="__main__":
      app.run(debug=True)





