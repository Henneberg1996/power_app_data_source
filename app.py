from flask import Flask, jsonify
import inspect
from invoke import task

data = [
    {
        "customer_no": "10000",
        "name": "Imperial Speeder Bike",
        "model": "74-Z speeder bike",
        "manufacturer": "Aratech Repulsor Company",
        "cost_in_credits": "8000",
        "length": "3",
        "max_atmosphering_speed": "360",
        "crew": "1",
        "passengers": "1",
        "cargo_capacity": "4",
        "consumables": "1 day",
        "vehicle_class": "speeder",
        "sales_lines": [
            {
             "Line_Object_No": "1000",
             "Line_Type": "Item",
             "Quantity": "1000"},
            {
             "Line_Object_No": "1000",
             "Line_Type": "Item",
             "Quantity": "1000"
             }
        ],
        "pilots": [
            "https://swapi.dev/api/people/1/",
            "https://swapi.dev/api/people/5/"
        ],
        "films": [
            "https://swapi.dev/api/films/3/"
        ],
        "created": "2014-12-18T11:20:04.625000Z",
        "edited": "2014-12-20T21:30:21.693000Z",
        "url": "https://swapi.dev/api/vehicles/30/"
    },
    {
        "customer_no": "10000",
        "name": "Imperial Speeder Bike",
        "model": "74-Z speeder bike",
        "manufacturer": "Aratech Repulsor Company",
        "cost_in_credits": "8000",
        "length": "3",
        "max_atmosphering_speed": "360",
        "crew": "1",
        "passengers": "1",
        "cargo_capacity": "4",
        "consumables": "1 day",
        "vehicle_class": "speeder",
        "sales_lines": [
            {
                "Line_Object_No": "1000",
                "Line_Type": "Item",
                "Quantity": "1000"},
            {
                "Line_Object_No": "1000",
                "Line_Type": "Item",
                "Quantity": "1000"
            }
        ],
        "pilots": [
            "https://swapi.dev/api/people/1/",
            "https://swapi.dev/api/people/5/"
        ],
        "films": [
            "https://swapi.dev/api/films/3/"
        ],
        "created": "2014-12-18T11:20:04.625000Z",
        "edited": "2014-12-20T21:30:21.693000Z",
        "url": "https://swapi.dev/api/vehicles/30/"
    }
]


# Fix the inspect.getargspec deprecation warning
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

app = Flask(__name__)

# Define a route for the root URL ('/') and specify the allowed methods
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)