from flask import Flask, render_template, request, redirect, url_for, session, send_file
from utils import validateValues
from generate_cert import generate_certificate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# /generate-csr : GET
@app.route('/download')
def download():
    return render_template('download.html')

# /download/certificate : GET


@app.route('/download/certificate')
def download_cert():
    print('DOWNLOADING CERTIFICATE...')
    return send_file('certificates/certificate.crt', as_attachment=True)


# /generate-certificate : POST
# params:
#   Common Name: string
#   Organization: string
#   Country: string (two letter code)
#   State: string
#   City: string

@app.route('/generate-certificate', methods=['POST'])
def gen_cert():
    common_name = str(request.form['cn'])
    organization = str(request.form['organization'])
    country = str(request.form['country'])
    state = str(request.form['state'])
    city = str(request.form['city'])
    print(common_name, organization, country, state, city)

    # validate values and return error if invalid
    if not validateValues([common_name, organization, country, state, city]):
        # return html error page
        print("--------Invalid values--------")
        return render_template('error.html')

    generate_certificate(organization, common_name, country, state, city)
    # generate certificate
    # download certificate

    return render_template('download.html')
