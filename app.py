import os
import statistics

import requests
from flask import Flask, render_template, jsonify, redirect
from dotenv.main import load_dotenv

load_dotenv()
app = Flask(__name__)

api_url = os.environ['POKEAPI_URL']
print(api_url)
response = requests.get(f'{api_url}/berry')
data = response.json()


def countBerries(berries):
    berries_count = len(berries)
    return berries_count


@app.route('/')
def index():
    return redirect('/allBerryStats')

#GRAPHS
@app.route('/allBerryStats', methods=['GET'])
def allBerryStats():
    try:
        if response.status_code == 200:
            berries = [berry['name'] for berry in data['results']]
            berry_stats = {
                "berries_names": berries,
            }
            growth_time_list = []

            for berry_id in range(1, len(berries) + 1):
                berry_url = f"{api_url}/berry/{berry_id}"
                try:
                    berry_response = requests.get(berry_url)

                    if berry_response.status_code == 200:
                        berry_data = berry_response.json()
                        growth_time_list.append(berry_data["growth_time"])


                        berry_stats[f"min_growth_time_{berry_id}"] = min(growth_time_list)
                        berry_stats[f"median_growth_time_{berry_id}"] = statistics.median(growth_time_list)
                        berry_stats[f"max_growth_time_{berry_id}"] = max(growth_time_list)
                        if len(growth_time_list) >= 2:
                            berry_stats[f"variance_growth_time_{berry_id}"] = statistics.variance(growth_time_list)
                        else:
                            berry_stats[f"variance_growth_time_{berry_id}"] = None
                        berry_stats[f"mean_growth_time_{berry_id}"] = statistics.mean(growth_time_list)
                        berry_stats[f"frequency_growth_time_{berry_id}"] = berry_data['growth_time']
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred while fetching berry {berry_id}: {str(e)}")
                    continue


            return render_template('index.html', berry_stats=berry_stats)

        else:
            return jsonify({'error': 'Failed to fetch berry stats'}), response.status_code, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500, {'Content-Type': 'application/json'}



#JSON


@app.route('/allBerryStats/headers', methods=['GET'])
def addHeaders():
    try:
        if response.status_code == 200:
            response.headers['Content-Type'] = 'application/json'

            headers = {'Content-type': 'content_type_value'}
            berries = [berry['name'] for berry in data['results']]
            berry_stats = {
                "berries_names": berries,
            }
            growth_time_list = []

            for berry_id in range(1, len(berries) + 1):
                berry_url = f"{api_url}/berry/{berry_id}"
                try:
                    berry_response = requests.get(berry_url, headers=headers)

                    if berry_response.status_code == 200:
                        berry_data = berry_response.json()
                        growth_time_list.append(berry_data["growth_time"])

                        berry_stats[f"min_growth_time_{berry_id}"] = min(growth_time_list)
                        berry_stats[f"median_growth_time_{berry_id}"] = statistics.median(growth_time_list)
                        berry_stats[f"max_growth_time_{berry_id}"] = max(growth_time_list)
                        if len(growth_time_list) >= 2:
                            berry_stats[f"variance_growth_time_{berry_id}"] = statistics.variance(growth_time_list)
                        else:
                            berry_stats[f"variance_growth_time_{berry_id}"] = None
                        berry_stats[f"mean_growth_time_{berry_id}"] = statistics.mean(growth_time_list)
                        berry_stats[f"frequency_growth_time_{berry_id}"] = berry_data['growth_time']
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred while fetching berry {berry_id}: {str(e)}")
                    continue
            dictionary={'berries_names':berries,
                        'min_growth_time':berry_stats[f"min_growth_time_{berry_id}"],
                        'median_growth_time_': berry_stats[f"median_growth_time_{berry_id}"],
                        'max_growth_time_': berry_stats[f"max_growth_time_{berry_id}"],
                        'variance_growth_time_': berry_stats[f"variance_growth_time_{berry_id}"],
                        'mean_growth_time_': berry_stats[f"mean_growth_time_{berry_id}"],
                        'frequency_growth_time_': berry_stats[f"frequency_growth_time_{berry_id}"]
                        }


            return jsonify(dictionary)

        else:
            error_message = {'error': 'Failed to fetch berry stats'}
            return jsonify(error_message), response.status_code

    except Exception as e:
        error_message = {'error': 'An error occurred: ' + str(e)}
        return jsonify(error_message), 500




@app.route("/berries", methods=['GET'])
def berries():
    try:
        if response.status_code == 200:
            berries = [berry['name'] for berry in data['results']]
            berry_stats = {
                "berries_names": berries,
            }
            return render_template('berries.html', berry_stats=berry_stats)

        else:
            return jsonify({'error': 'Failed to fetch berry stats'}), response.status_code, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500, {'Content-Type': 'application/json'}





if __name__ == '__main__':
    app.run(debug=True)


