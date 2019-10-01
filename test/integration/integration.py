import json
from pathlib import Path
import subprocess
from time import sleep

import pytest
import requests

WAIT_LIMIT = 30


# If all fails it might mean there is a problem with local docker.

@pytest.fixture(scope="session", autouse=True)
def initiliazer(request):
    request.addfinalizer(finalizer)
    workdir = Path(__file__).parents[2]

    subprocess.run(["docker-compose", "down"], cwd=workdir)
    subprocess.run(["docker-compose", "build"], cwd=workdir)
    subprocess.Popen(["docker-compose", "up"], cwd=workdir)

    for _ in range(WAIT_LIMIT):
        try:
            requests.get(url="http://localhost/calc")
            break
        except Exception:
            print("Waiting 1 second until the server is up.")
            sleep(1)

    print("Starting the test")


def finalizer():
    workdir = Path(__file__).parents[2]
    subprocess.run(["docker-compose", "down"], cwd=workdir)


def test_get():
    r = requests.get(url="http://localhost/calc")
    assert r.status_code == 405, "GET should not be allowed."


def test_empty_post():
    r = requests.post(url="http://localhost/calc")
    assert r.status_code == 400, "Empty POST should not be allowed."


def test_different_address():
    r = requests.post(url="http://localhost/")
    assert r.status_code == 404, "Other adresses should not exist."


def test_invalid():
    r = requests.post(url="http://localhost/calc", json={"expression": "-1-"})
    assert r.status_code == 400, "This should give an invalid expression error."


def test_add():
    r = requests.post(url="http://localhost/calc", json={"expression": "1+1"})
    assert r.status_code == 200, "Expression should be valid."
    assert json.loads(r.text)["result"] == 2, "Result should be 2."
