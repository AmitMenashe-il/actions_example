import requests
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def CharCSV():
    BASE_URL = "https://rickandmortyapi.com/api"

    base_url = requests.get(BASE_URL)

    # get characters
    char_url = base_url.json()['characters']
    characters = requests.get(char_url).json()['results']

    # Human Alive Earth list
    charsPicked = []
    species = 'Human'
    status = 'Alive'
    origin = 'Earth'

    for character in characters:
        if (character['species'] == species and character['status'] == status and character['origin'][
            'name'].startswith(
                'Earth')):
            charsPicked.append(character)

    # Name Location Image list

    filteredData=[]

    for character in charsPicked:
        filteredData.append([character['name'], character['location'], character['image']])

    return flask.jsonify(filteredData), 200


@app.route('/healthcheck', methods=['GET'])
def Healthcheck():
    return flask.jsonify({"status": "healthy"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
