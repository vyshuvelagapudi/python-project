import os
import flask
from flask import request, render_template, redirect, url_for, flash
from flask_cors import CORS


from api.foggyController import foggyPrediction

cwd = os.getcwd()

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = flask.Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config["DEBUG"] = True
CORS(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/', methods = ['GET','POST'])  
def index():  
    context={'method':request.method}
    
    if request.method == 'POST':
        context = predict()
        context['method'] =request.method
        # print(context)
        
    return render_template("index.html", context=context)  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        context = {'success': False}

        # if 'file' not in request.files:
		#     flash('No file part')
		#     return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect("/")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            #print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below')

            print(path)
            context['filename'] = filename
            context['path'] = path

            # predicting images
            result = foggyPrediction(path)
            context['result'] = result

            
            context['success'] = True
            # return redirect("/")
            return render_template("success.html", context=context)

        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return redirect("/")

 
def predict():  
    context = {'success': False}

    # if 'file' not in request.files:
    #     flash('No file part')
    #     return redirect(request.url)
    #     context['msg'] =  "No file part "
    #     return context

    file = request.files['file']
    if file.filename == '':
        # flash('No image selected for uploading')
        context['msg'] =  "No image selected for uploading"
        return context

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        #print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded and displayed below')
        context['msg'] =  "Image successfully uploaded and displayed below"

        # print(path)
        context['filename'] = filename
        context['path'] = path

        # predicting images
        result = foggyPrediction( path)
        context['result'] = result

        
        context['success'] = True
        # return redirect("/")
        return context

    else:
        # flash('Allowed image types are -> png, jpg, jpeg, gif')
        context['msg'] = 'Allowed image types are -> png, jpg, jpeg, gif'
        
        return context

  

@app.route('/display/<filename>')
def display_image(filename):
	# print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)  # pass DEBUG param</pre>
