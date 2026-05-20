from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html', active='home')

# About page
@app.route('/about')
def about():
    return render_template('about.html', active='about')

# Courses page
@app.route('/courses')
def courses():
    return render_template('courses.html', active='courses')

# Blog page
@app.route('/blog')
def blog():
    return render_template('blog.html', active='blog')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you can add code to send email or save to database
        print(f"Contact: {name}, {email}, {message}")
        return render_template('contact.html', success=True, active='contact')
    return render_template('contact.html', success=False, active='contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
