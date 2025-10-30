# Dragon Ball API API Example
import requests

url = "https://dragonball-api.com/api/characters?page=2&limit=5"
headers = {
    "Content-Type": "application/json"
}
response = requests.get(url)
data = response.json()
# Pasar a un dataframe pandas
df = pd.DataFrame(data)
print(df)