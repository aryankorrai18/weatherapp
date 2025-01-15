from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=764c1a7a12b2b10160fa6e05da8cee22"
        json_data = requests.get(api).json()
        
        # Process weather data...
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        
        return f"{condition}, {temp}°C"
    return '''
        <form method="post">
            <input type="text" name="city" placeholder="Enter City">
            <button type="submit">Get Weather</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
