import certifi
from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import extensions

app = Flask(__name__)



@app.route('/')
@app.route('/admin', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        datetime_now = datetime.now()
        extensions.user_collection.insert_one({'name' : name, 'date' : datetime_now})
        return redirect('/admin')
    else:
        return render_template('index.html',users = extensions.user_collection.find())


@app.route('/admin/delete/<_id>')
def delete(_id):
    try:
        print(id)
        extensions.user_collection.delete_one({'_id': ObjectId(_id)})
        return redirect('/admin')
      
    except:
        return"There was an issue deleteing existing user"


@app.route('/admin/update/<_id>', methods=['POST', 'GET'])
def update(_id):
    if request.method == 'POST':
        new_name = request.form['name']
        try:
            extensions.user_collection.find_one_and_update({"_id": ObjectId(_id)}, 
                                 {"$set": {"name": new_name}})
            return redirect('/admin')

        except:
            return"There was an issue updating existing user"
        
    else:
        return render_template('update.html', _id = _id)

        
if __name__ == "__main__":
    app.run(debug=True)
    
