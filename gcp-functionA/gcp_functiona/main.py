# functionA.py
import requests
from flask import jsonify
import functions_framework


import debugpy

debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()
debugger = 1  # Add this line


@functions_framework.http
def listen(request):
    # Assuming functionB is exposed as an HTTP trigger
    # response = requests.get("http://localhost:8080", timeout=10)
    result_from_B = "B"  # response.json()["result_from_B"]

    return jsonify(
        {"result_from_A": "This is from functionA", "result_from_B": result_from_B}
    )
