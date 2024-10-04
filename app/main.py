from flask import Blueprint,render_template,request

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

# @main.route('/Home')
# def index():
#     return render_template('index.html')

@main.route('/Our_Story')
def Our_Story():
    return render_template('Our_Story.html')

@main.route('/Our_Project')
def Our_Project():
    return render_template('Our_Project.html')

@main.route('/ComputerLiteracy')
def ComputerLiteracy():
    return render_template('ComputerLiteracy.html')

@main.route('/secondary_education')
def secondary_education():
    return render_template('secondary_education.html')

@main.route('/self_employement')
def self_employement():
    return render_template('self_employement.html')

@main.route('/Skill_Development')
def Skill_Development():
    return render_template('Skill_Development.html')

@main.route('/JCH')
def JCH():
    return render_template('JCH.html')

@main.route('/CoronaVirusRelief')
def CoronaVirusRelief():
    return render_template('CoronaVirusRelief.html')

@main.route('/school_infrastructure')
def school_infrastructure():
    return render_template('school_infrastructure.html')

@main.route('/donate')
def donate():
    return render_template('donate.html')

@main.route('/gallery')
def gallery():
    return render_template('gallery.html')

@main.route('/Media_Press')
def Media_Press():
    return render_template('Media_Press.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')