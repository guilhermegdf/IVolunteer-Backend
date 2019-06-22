from flask import Response, json
import requests

def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
        )

def filter_data(data, val):
    return [ res.get(val) for res in data.data ]

def get_lat_long(data):

        address = data.replace(' ', '+')
        url = "https://maps.googleapis.com/maps/api/geocode/json?address={}+View,+BR&key=AIzaSyB4iJ2uzhrIWGtIsOSMdKqHV6aiU8nnAVI".format(address)
        response = requests.get(url)
        response = response.json()
        if response['status'] == 'ZERO_RESULTS':
                return {'lat': '-23,5486','lng': '-46,6392'}
        else:
                return response['results'][0]['geometry']['location']