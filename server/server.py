from flask import Flask,request,jsonify
import util
app=Flask(__name__)



#we need two routine 1.locations of bangalore city - columns.json
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.getlocation()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    
    response=jsonify({
        'estimated_price':util.get_price(location,total_sqft,bhk,bath)
    })
    
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__ == '__main__':
    print("Start Setver for home Price Prediction")
    util.load_save_data()
    app.run()