from flask import Flask, render_template, request, redirect, url_for, session, abort
from utils import validateValues

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# /generate-csr : GET
@app.route('/generate-csr')
def generate_csr():
    return render_template('generate-csr.html')


# /generate-certificate : POST
# params:
#   Common Name: string
#   Organization: string
#   Country: string (two letter code)
#   State: string
#   City: string

@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    common_name = request.form['cn']
    organization = request.form['organization']
    country = request.form['country']
    state = request.form['state']
    city = request.form['city']
    print(common_name, organization, country, state, city)

    # validate values and return error if invalid
    if not validateValues([common_name, organization, country, state, city]):
        # return html error page
        return render_template('error.html')
    
    # TODO: generate certificate

    return redirect(url_for('index'))
