def get_uri():
    import json
    import os

    data = json.loads(os.getenv('VCAP_SERVICES'))['cleardb'][0]['credentials']

    return "{driver}://{user}:{password}@{host}/{dbname}".format(
        driver = 'mysql',
        user = data['username'],
        password = data['password'],
        host = data['hostname'],
        dbname = data['name']
    )
