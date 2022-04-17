import requests
import pandas as pd
import xmltodict

apikey1 = '5Q9%2BfAqH1XCYPQpg8IFfbPwNbxhULkhy8GwmgFTA6JkBcqjJ79oNy7osituTTYXfoTLNrnmN9D10R9The9YKZg%3D%3D'
apikey2 = '5Q9+fAqH1XCYPQpg8IFfbPwNbxhULkhy8GwmgFTA6JkBcqjJ79oNy7osituTTYXfoTLNrnmN9D10R9The9YKZg=='
endpoint = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'

url = 'https://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

api_url = url+'?ServiceKey='+apikey1

start_date = '20200101'
api_url2 = f'{url}?ServiceKey={apikey1}&startCreateDt={start_date}'

res = requests.get(api_url)
res_dict = xmltodict.parse(res.text)