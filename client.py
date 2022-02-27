#!/usr/local/bin//python3
def application(env, start_response):
    if env["REQUEST_METHOD"] == "POST":
        uri = env["REQUEST_URI"]
        content_length = int(env["CONTENT_LENGTH"])
        message = env["wsgi.input"].read(content_length)

        if uri == "/message":
            start_response("200 OK", [("Content-Type", "text/plain")])
            yield b"Message received\n"
        else:
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            yield b"Resource doesn't exist\n"

    if env["REQUEST_METHOD"] == "GET":
        print(env)
        start_response("400 Bad Request", [("Content-Type", "text/plain")])
        yield b"get thfuk outta here\n"

