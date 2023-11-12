# functionA.py
import requests
from flask import jsonify
import functions_framework


@functions_framework.http
def listen(request):
    # Assuming functionB is exposed as an HTTP trigger
    response = requests.get("http://localhost:8080/functionB")
    result_from_B = response.json()["result_from_B"]

    return jsonify(
        {"result_from_A": "This is from functionA", "result_from_B": result_from_B}
    )
