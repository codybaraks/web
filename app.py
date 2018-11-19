from flask import Flask ,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
   return render_template("index.html")



if __name__ == '__main__':
    app.run()


#count females
   # SELECT COUNT(*) FROM students WHERE gender='female'
#select females
   # SELECT * FROM `students` WHERE gender='female'

#count people born after 1998
   # SELECT COUNT(*) FROM students WHERE dob >= 1998
#count people whose names start with letter M
   # SELECT COUNT(*) FROM students WHERE names<='M%'

#count unique course
   # SELECT COUNT(DISTINCT course) FROM students

#delate person whose id = 1000
   # DELETE FROM `students` WHERE id=1000
