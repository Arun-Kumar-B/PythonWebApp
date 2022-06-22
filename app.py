from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 

 
@app.route('/login', methods=['POST', 'GET'])
def login():
    render_template("login.html", title = 'login')
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
      
@app.route('/')
def projects():
    return render_template("login.html", title = 'login')
 
@app.route('/home')
def home():
   return render_template("home.html")
 
if __name__ == '__main__':
   app.run()
  
  
