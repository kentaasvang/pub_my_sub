#!/usr/local/bin//python3
def application(env, start_response):
#    content_length = int(env["CONTENT_LENGTH"])
#    post_data = env["wsgi.input"].read(content_length)
#    print()
#    print(post_data)
#    print()
    print(env)
    start_response("200 OK", [("Content-Type", "text/plain")])
    yield b"hello from subscriber\n"
