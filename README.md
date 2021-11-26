# A Toy Implementation Of a Pub/Sub

### Minimal Vial Product

Subscribers send messages with a topic to publisher
Publisher send messages to all subcribers subscribing on that topic
Subscribers subscribers to topic by posting to that topic

##### Publisher
* List of topics
  * each topic has list of subscribers to that topic

**Listens to**
* POST /subscribe
* DELETE /subscribe


##### Subscriber
* List of topics

**Listens to**
* POST/message

