from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login')
def projects():
    return render_template("login.html", title = 'login')
 
@app.route('/')
def home():
   return render_template("home.html")
 
if __name__ == '__main__':
   app.run()
  
  
