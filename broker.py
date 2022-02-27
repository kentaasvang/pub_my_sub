#!/usr/local/bin//python3
import json


def application(env, start_response):

    topics = {}

    if env["REQUEST_METHOD"] == "POST": 
        uri = env["REQUEST_URI"]
        content_length = int(env["CONTENT_LENGTH"])
        query_string = env["wsgi.input"].read(content_length)

        if uri == "/message":
            start_response("200 OK", [("Content-Type", "text/plain")])
            yield b"Message received\n"

        if uri == "/subscribe":
            topic = get_topic(query_string)
            remote_addr = env["REMOTE_ADDR"]

            if topic not in topics.keys():
                start_response("404 Not Found", [("Content-Type", "text/plain")])
                yield b"Topic '%s' does not exist" % topic
            else:
                if remote_addr not in topics[topic]:
                    topics[topic].append(remote_addr)
                    start_response("201 OK", [("Content-Type", "text/plain")])
                    yield b"Successfully subscribed to topic: %s\n" % topic
                else:
                    start_response("409 Conflict", [("Content-Type", "text/plain")])
                    yield b"You're already subscribed to this topic: %s" % topic

        if uri == "/create_topic":
            topic = get_topic(query_string)
            remote_addr = env["REMOTE_ADDR"]
            if topics.has_key(topic):
                if remote_addr not in topics[topic]:
                    topics[topic].append(remote_addr)
            else:
                topics[topic] = [remote_addr]

            start_response("201 OK", [("Content-Type", "text/plain")])
            yield b"Successfully created topic: %s" % topic

    if env["REQUEST_METHOD"] == "GET":
        #test that this works before moving on
        if uri == "/topics":
            topics_json = json.dumps(topics)
            start_response("200 OK", [("Content-Type", "text/json")])
            yield b"%s" % topics_json

    print(env)
    start_response("400 Bad Request", [("Content-Type", "text/plain")])
    yield b"get thfuk outta here\n"


def get_topic(qstr):
    return str.encode(str(qstr).split("=")[1])



