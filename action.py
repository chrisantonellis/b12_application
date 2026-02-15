import urllib


def generate_request_body():
    {
        "timestamp": "2026-01-06T16:59:37.571Z",
        "name": "Your name",
        "email": "you@example.com",
        "resume_link": "https://pdf-or-html-or-linkedin.example.com",
        "repository_link": "https://link-to-github-or-other-forge.example.com/your/repository",
        "action_run_link": "https://link-to-github-or-another-forge.example.com/your/repository/actions/runs/run_id"
    }


# url = 'https://httpbin.org/post' # A URL to test POST requests

# # 1. Prepare the data as a dictionary
# values = {'name': 'John Doe', 'location': 'Anytown'}

# # 2. Encode the data to a URL-encoded string, then to bytes
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes

# # 3. Create a Request object. The presence of 'data' implies a POST request.
# req = urllib.request.Request(url, data=data)

# # 4. Open the URL and send the request
# try:
#     with urllib.request.urlopen(req) as response:
#         response_content = response.read()
#         print(response_content.decode('utf-8'))
# except urllib.error.URLError as e:
#     print(f"Error: {e.reason}")


def main():
    print("executing github action")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        exit(e)