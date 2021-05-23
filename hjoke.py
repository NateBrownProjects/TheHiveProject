import requests
import hive
def hjoke():
    res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )

    if res.status_code == requests.codes.ok:
        print(str(res.json()['joke']))
    else:
        print('oops!I ran out of jokes')