import requests


class StrimziBridge:
    def __init__(self, domain_name, port):
        self._base_url = f"http://{domain_name}:{port}"

    @staticmethod
    def _make_api_call(http_method, url, headers, kwargs):
        response = None
        if http_method == "POST":
            response = requests.post(url, json=kwargs, headers=headers)

        if response is not None:
            print(response.status_code)
            print(response.content)

    def create_consumer(self, group_name, consumer_name=None, **kwargs):
        url = f"{self._base_url}/consumers/{group_name}"
        header = {"content-type": "application/vnd.kafka.v2+json"}
        body = {}

        if consumer_name is not None:
            body['name'] = consumer_name

        # Change underscores to Kafka property names with periods
        for key, value in kwargs.items():
            if "_" in key:
                body[key.replace("_", ".")] = kwargs[key]

        self._make_api_call("POST", url, header, body)

    def subscribe(self, group_name, consumer_name, topics):
        url = f"{self._base_url}/consumers/{group_name}/instances/{consumer_name}/subscription"
        header = {"content-type": "application/vnd.kafka.v2+json"}
        body = {"topics": topics}

        self._make_api_call("POST", url, header, body)
