import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request
import json
import math
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="landing_page")
 

@app.route('/compute', methods = ['POST'])
def compute():

    sample1 = request.form['sample1']
    sample2 = request.form['sample2']
    a = sample1.split()
    a = [''.join(c for c in s if c not in string.punctuation) for s in a]
    a = [s for s in a if s]
    b = sample2.split()
    b = [''.join(c for c in s if c not in string.punctuation) for s in b]
    b = [s for s in b if s]

    a2,b2 = {}, {}
    for c in range(len(a)):
        a2[a[c]] = a.count(a[c])
    for c in range(len(b)):
        b2[b[c]] = b.count(b[c])

    k1, k2 = set(a2.keys()), set(b2.keys())
    intrsct = k1 & k2
    num = ([a2[x] * b2[x] for x in intrsct])
    num_val = sum(num)

    s1 = sum([a2[x] ** 2 for x in list(a2.keys())])
    s2 = sum([b2[x] ** 2 for x in list(b2.keys())])

    den_val = math.sqrt(s1) * math.sqrt(s2)
    fnl_scr = float(num_val) / den_val

    if not den_val:
        fnl_scr = 0.0
    else:
        fnl_scr = float(num_val) / den_val

    return "The similarity score is {}".format(str(fnl_scr))


if __name__ == "__main__":
 app.run(host="localhost", debug=True)
