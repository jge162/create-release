import requests
import json

url = "https://github.com/jge162/create-release/actions/workflows/create_release.yml"

payload = {
    "ref": "main",
    "inputs": {
        "input1": "<value1>",
        "input2": "<value2>"
    }
}
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer WORKFLOW_SECRET",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 204:
    print("Workflow dispatched successfully!")
else:
    print(f"Error dispatching workflow: {response.status_code}")
