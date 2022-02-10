import json
from pprint import pprint

import requests

DOMAIN_NAME = "api.github.com/users"
DOMAIN_NAME_WITH_HTTPS = "https://api.github.com/users"
REPOS = "/repos"


def parse_input(string_input):
    print("parsing input")
    return create_url(string_input)


def remove_domain(string_input):
    return string_input.split(DOMAIN_NAME)[-1]


def create_url(string_input):
    filtered_url = remove_domain(string_input)
    if filtered_url[0] == "/":
        return DOMAIN_NAME_WITH_HTTPS + filtered_url + REPOS
    return DOMAIN_NAME_WITH_HTTPS + "/" + remove_domain(string_input) + REPOS


def req(url):
    print("reqing")
    s = requests.get(url)
    print("reqing done")
    try:
        if json.loads(s.content)["message"] == "Not Found":
            print("empty")
            return []
    except TypeError:

        return [{"name": i["full_name"].split("/")[1], "url": i["html_url"], "desc": i["description"]} for i in
                json.loads(s.content)]


def get_repos(data):
    return req(parse_input(data))
