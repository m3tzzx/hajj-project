from flask import Flask, render_template, jsonify, request
from sqlalchemy import text
from database import engine

app = Flask(__name__)

def load_pilgrims_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from pilgrims"))
    pilgrims = []
    for row in result.all():
      pilgrims.append(row._mapping)
    return pilgrims

@app.route("/")
def hello():
    return render_template('index.html')
  
@app.route("/client.html")
def hello_client():
    return render_template('client.html')
  
@app.route("/user.html")
def hello_user():
    pilgrims = load_pilgrims_from_db()
    return render_template('user.html')



@app.route('/get_data', methods=['POST'])
def get_data():
    user_input = request.json.get('input')  # Get input from the request

    pilgrims = load_pilgrims_from_db()


    pilgrim = pilgrims[int(user_input) - 1]  # Assuming the input is the index of the pilgrim in the list 
    pilgrim_id = pilgrim['id']
    pilgrim_name = pilgrim['pilgrim_name']
    pilgrim_camp = pilgrim['camp']
    
    
    # If result is found, return it, otherwise return an error message
    if pilgrim:
        return jsonify({"pilgrim_id": str(pilgrim_id)}, {"pilgrim_name": str(pilgrim_name)}, {"pilgrim_camp": str(pilgrim_camp)})
    else:
        return jsonify({"output": "No data found for this input."})

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

# , {"pilgrim-name": pilgrim['pilgrim_name']}, {"pilgrim-camp": pilgrim['camp']}