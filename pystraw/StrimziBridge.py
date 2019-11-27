import requests

class StrimziBridge:
    def __init__(self, domain_name, port):
        self._base_url = f"http://{domain_name}:{port}"
        self.domain_name = domain_name
        self.port = port

    def _make_api_call(self, http_method, url, headers, kwargs):
        response = None
        if http_method == "POST":
            response = requests.post(url, json=kwargs, headers=headers)

        if response is not None:
            print(response.status_code)
            print(response.json())

    def create_consumer(self, group_name, **kwargs):
        url = f"{self._base_url}/consumers/{group_name}"
        header = {"content-type": "application/vnd.kafka.v2+json"}

        # Change underscores to Kafka property names with periods
        for key, value in kwargs.items():
            if "_" in key:
                kwargs[key.replace("_", ".")] = kwargs.pop(key)

        self._make_api_call("POST", url, header, kwargs)