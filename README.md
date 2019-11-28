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
# Create a new consumer. Except group_name, all other parameters are optional
response = bridge.create_consumer(group_name="group_name",
                                  consumer_name="consumer_name",
                                  format="json",
                                  auto_offset_reset="earliest",
                                  enable_auto_commit="true",
                                  fetch_min_bytes=512,
                                  consumer_request_timeout_ms=5000
                                  )
                 
# Subsribe to a list of topics
response = bridge.subscribe(group_name="group_name", 
                            consumer_name="consumer_name", 
                            topics=["test1", "test2"]
                            )

# Read data from the subscribed topic
response = bridge.read_records(group_name="group_name", 
                               consumer_name="consumer_name", 
                               msg_format="json"
                               )

```
