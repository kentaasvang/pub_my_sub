# A Toy Implementation Of a Pub/Sub

### Minimal Vial Product

- Subscribers send messages with a topic to publisher
- Publisher send messages to all subcribers subscribing on that topic

### Publisher
* List of topics
  * each topic has list of subscribers to that topic

**Listens to**
* POST /subscribe
* DELETE /subscribe

**Usage:**
Preferably no code needed, only config and startup

### Subscriber
* List of topics

**Listens to**
* POST/message

**Usage:**

_my\_sub.py_
```
from pub\_my\_sub import client

# publish a messagr
client.publish(topic="temperature", message="cold as hell")

# sub to topic
client.subscribe("/temperatures")

```

