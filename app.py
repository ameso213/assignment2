from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')

def  basic():
    
    return '<h1>am am imie </h1>'

@app.route('/about')
def  about():
    return render_template('about.html')



@app.route('/contacts')
def  contacts():
    return render_template('contacts.html')


@app.route('/forms')
def  forms():
    return render_template('forms.html')


@app.route('/thankyou')
def  thankyou():
    return render_template('thankyou.html')




@app.route('/user')
def  user():
    return render_template('user.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        #for data processing 
        return render_template('thankyou.html', name=name, email=email)
    return render_template('form.html')
if __name__=='main_':
    app.run(debug=True)




