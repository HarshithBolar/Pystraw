# PYSTRAW: The Python Strimzi-Bridge API Wrapper
Pystraw, an acronym for "Python Strimzi-Bridge API Wrapper", is a python package that allows for simple access to Strimzi-Kafka-Bridge's API.

More information about Strimzi-Kafka-Bridge can be found at https://github.com/strimzi/strimzi-kafka-bridge

## Quickstart
Create the Strimzi bridge instance.
```python
from pystraw import StrimziBridge

bridge = StrimziBridge("localhost", 8080)
```

Now you can interact with Kafka via the bridge. 

```python
# Create a new consumer.
bridge.create_consumer("group_name",
                       name="consumer_name",
                       format="json",
                       auto_offset_reset="earliest",
                       enable_auto_commit="true",
                       fetch_min_bytes=512,
                       consumer_request_timeout_ms=5000
                       )
```
