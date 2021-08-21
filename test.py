import requests, schedule
def indo():
    api_url="https://api.kawalcorona.com/indonesia/"
    # api_url="https://covid19.mathdro.id/api/countries/indonesia"
    rstl= requests.get(api_url).json()
    print(rstl)

def maluku():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    # api_url="https://indonesia-covid-19.mathdro.id/api/provinsi/32"
    rstl= requests.get(api_url).json()
    cek= rstl[31]
    ambil_dict= cek["attributes"]
    a=[ambil_dict]
    print(a)

r_indo= schedule.every(2).seconds.do(indo)
r_malut= schedule.every(2).seconds.do(maluku)

while True:
    schedule.run_pending()

data_indo = indo()
print(data_indo)

mal = maluku()
print(mal)