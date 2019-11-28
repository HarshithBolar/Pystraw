import requests


class StrimziBridge:
    def __init__(self, domain_name, port):
        self._base_url = f"http://{domain_name}:{port}"
        self._json_post_header = {"content-type": "application/vnd.kafka.v2+json"}
        self._json_accept_header = {"accept": "application/vnd.kafka.json.v2+json"}
        self._binary_accept_header = {"accept": "application/vnd.kafka.binary.v2+json"}

    @staticmethod
    def _make_api_call(http_method, url, headers, body=None):
        response = None

        if http_method == "GET":
            response = requests.get(url, headers=headers)
        elif http_method == "POST":
            response = requests.post(url, json=body, headers=headers)

        return response

    def create_consumer(self, group_name, consumer_name=None, **kwargs):
        url = f"{self._base_url}/consumers/{group_name}"
        header = self._json_post_header
        body = {}

        if consumer_name is not None:
            body['name'] = consumer_name

        # Change underscores to Kafka property names with periods
        for key, value in kwargs.items():
            if "_" in key:
                body[key.replace("_", ".")] = kwargs[key]
            else:
                body[key] = kwargs[key]

        return self._make_api_call("POST", url, header, body)

    def subscribe(self, group_name, consumer_name, topics):
        url = f"{self._base_url}/consumers/{group_name}/instances/{consumer_name}/subscription"
        header = self._json_post_header
        body = {"topics": topics}

        return self._make_api_call("POST", url, header, body)

    def read_records(self, group_name, consumer_name, msg_format):
        url = f"{self._base_url}/consumers/{group_name}/instances/{consumer_name}/records"

        if msg_format == "json":
            header = self._json_accept_header
        elif msg_format == "binary":
            header = self._binary_accept_header
        else:
            raise ValueError("Invalid 'msg_version'. Valid are 'json' or 'binary'.")

        return self._make_api_call("GET", url, header)
