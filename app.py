from flask import Flask, render_template, make_response
import requests, schedule

app = Flask(__name__)
def indo():
    api_url="https://api.kawalcorona.com/indonesia/"
    # api_url="https://covid19.mathdro.id/api/countries/indonesia"
    rstl= requests.get(api_url).json()
    return rstl

def maluku():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    # api_url="https://indonesia-covid-19.mathdro.id/api/provinsi/32"
    rstl= requests.get(api_url).json()
    cek= rstl[32]
    ambil_dict= cek["attributes"]
    a=[ambil_dict]
    return a

def jateng():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    # api_url="https://indonesia-covid-19.mathdro.id/api/provinsi/32"
    rstl= requests.get(api_url).json()
    cek= rstl[13]
    ambil_dict= cek["attributes"]
    a=[ambil_dict]
    return a

r_indo= schedule.every(2).seconds.do(indo)
r_malut= schedule.every(2).seconds.do(maluku)
r_jateng= schedule.every(2).seconds.do(jateng)

data_indo = indo()
data_malut = maluku()
data_jateng = jateng()


@app.route("/")
def index():
    return render_template("index.html", data_indo=data_indo, data_malut=data_malut, data_jateng=data_jateng)

if __name__ == "__main__":
    app.run(debug=True)