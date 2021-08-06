from redis import Redis
import json


redis_client = Redis(host='localhost', port=6379)

user_name = redis_client.get('username')
redis_client.set('password', 'omar19')
print(user_name)
print(redis_client.get('password'))


def set_json():
    data = {
        'name': 'Omar',
        'age': 27,
        'skills': ['C', 'C++', 'Java', 'PHP', 'Python'],
    }
    result = redis_client.set('user_data', json.dumps(data))
    return result


def get_json():
    user_data = redis_client.get('user_data')
    return json.loads(user_data)


if __name__ == '__main__':
    res = set_json()
    print(res)

    data = get_json()
    print(data)



