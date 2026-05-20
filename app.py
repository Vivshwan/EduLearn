from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)


# Load course data
def load_courses():
    try:
        with open('data/courses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Routes
@app.route('/')
def home():
    """Homepage - Landing page"""
    courses = load_courses()[:3]  # Show only top 3 courses on homepage
    return render_template('index.html', courses=courses, active='home')


@app.route('/about')
def about():
    """About page - Company info, mission, team"""
    return render_template('about.html', active='about')


@app.route('/courses')
def courses():
    """Courses/Services page - All available courses"""
    all_courses = load_courses()
    return render_template('courses.html', courses=all_courses, active='courses')


@app.route('/blog')
def blog():
    """Blog page - Educational articles"""
    blogs = [
        {
            'title': 'Why Learn Python in 2024?',
            'date': 'May 15, 2024',
            'author': 'John Doe',
            'excerpt': 'Python continues to dominate the programming world...',
            'image': 'python.jpg'
        },
        {
            'title': 'The Future of AI in Education',
            'date': 'May 10, 2024',
            'author': 'Jane Smith',
            'excerpt': 'How artificial intelligence is transforming learning...',
            'image': 'ai.jpg'
        },
        {
            'title': 'Top 10 Web Development Trends',
            'date': 'May 5, 2024',
            'author': 'Mike Johnson',
            'excerpt': 'Stay ahead with these web development trends...',
            'image': 'webdev.jpg'
        }
    ]
    return render_template('blog.html', blogs=blogs, active='blog')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page - Contact form"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would send email or save to database
        print(f"Contact Form Submission: {name}, {email}, {message}")

        return render_template('contact.html', success=True, active='contact')

    return render_template('contact.html', success=False, active='contact')


@app.route('/course/<int:course_id>')
def course_detail(course_id):
    """Individual course detail page"""
    courses = load_courses()
    course = next((c for c in courses if c['id'] == course_id), None)
    return render_template('course_detail.html', course=course, active='courses')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
