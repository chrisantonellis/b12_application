import os
import urllib

GITHUB_SERVER_URL = os.getenv("GITHUB_SERVER_URL")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_RUN_ID = os.getenv("GITHUB_RUN_ID")


# def _generate_request_body():
#     {
#         "timestamp": "2026-01-06T16:59:37.571Z",
#         "name": "Christopher Antonellis",
#         "email": "christopher.antonellis@gmail.com",
#         "resume_link": "https://drive.google.com/file/d/1AyxaOHK4_O6KwUruJg3S9N_57-ROF3lp/view?usp=drive_link",
#         "repository_link": "https://github.com/chrisantonellis/b12_application",
#         "action_run_link": "https://link-to-github-or-another-forge.example.com/your/repository/actions/runs/run_id"

#     WORKFLOW_URL="$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID"

#     }



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
    print(GITHUB_SERVER_URL)
    print(GITHUB_REPOSITORY)
    print(GITHUB_RUN_ID)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        exit(e)