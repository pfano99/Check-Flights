from flask import Flask, render_template, redirect, url_for
from api import Flights

from forms import FlightForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisis the key'

IATA_CODES = {
    'OR Tambo International Airport':'JNB',
    'Cape Town International Airport':'CPT', 
    'King Shaka International Airport':'DUR',
    'Port Elizabeth Airport':'PLZ', 
    'East London Airport':'ELS'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    title='Flights'
    form = FlightForm()
    data = None
    if form.validate_on_submit():
        # print(, IATA_CODES[form.arrival.data])
        flight = Flights()
        resp = flight.get_flights(
                IATA_CODES[form.departure.data],
                IATA_CODES[form.arrival.data]
        )
        if resp:
            data =flight.clean_json(resp)

        return render_template('index.html', form=form, title=title, data=data)
    return render_template('index.html',form=form, data=data, title=title)


if __name__=='__main__':
    app.run(debug=True)


