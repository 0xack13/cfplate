import json
import sys
from jinja2 import Environment, FileSystemLoader

def template(template, **kwargs):
    print("started template")
