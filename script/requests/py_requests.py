import requests as rq
import json
import sys

url_list_users = "https://reqres.in/api/users?page=2"
url_single_user = "https://reqres.in/api/users/"


def req_fundamentals(url):
    res = rq.get(url)
    print(res.status_code)  # get status code
    print("Type: ", type(res.text), res.text)  # get json string response
    data = json.loads(res.text)  # decode json string into python data structure (e.g: list, dict)
    print("Type: ", type(data), data)
    print("Type: ", type(json.dumps(data)), json.dumps(data))  # convert to json string


def get_data_from_res(url):
    res = rq.get(url)
    data = json.loads(res.text)
    user = data['data']
    print("ID: ", user["id"])
    print("Email: ", user["email"])
    print("First Name: ", user["first_name"])
    print("Last Name: ", user["last_name"])


if __name__ == "__main__":
    user_id = sys.argv[1]  # get input value from terminal
    #req_fundamentals(url_single_user+user_id)

    # get data from json response
    get_data_from_res(url_single_user+user_id)

