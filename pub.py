#!/usr/local/bin//python3
def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    yield b"hello from publisher\n"

