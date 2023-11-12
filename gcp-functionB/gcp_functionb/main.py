# functionB.py
from flask import jsonify
import functions_framework


@functions_framework.http
def listen(request):
    return jsonify({"result_from_B": "This is from functionB"})
