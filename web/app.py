from flask import Flask, render_template, request
import json
import math
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="landing_page")
 

@app.route('/compute', methods = ['POST'])
def compute():
    #collecting sample1 and sample2 texts from the front end
    sample1 = request.form['sample1']
    sample2 = request.form['sample2']

    #converting to lower case
    sample1 = sample1.lower()
    sample2 = sample2.lower()

    #creating a list of words for sample texts with split function
    a = sample1.split()
    b = sample2.split()

    #removing all the punctuations and extra whitespaces
    a = [''.join(c for c in s if c not in string.punctuation) for s in a]
    a = [s for s in a if s]
    b = [''.join(c for c in s if c not in string.punctuation) for s in b]
    b = [s for s in b if s]

    #Creating a dictionary of words with thier counts i.e number of times appeared in the texts
    a2,b2 = {}, {}
    for c in range(len(a)):
        a2[a[c]] = a.count(a[c])
    for c in range(len(b)):
        b2[b[c]] = b.count(b[c])

    #Cosine function to find similarity between the 2 texts
       
    #removing duplicates using sets and taking the common words between the texts
    k1, k2 = set(a2.keys()), set(b2.keys())
    intrsct = k1 & k2

    #calculating the numerator of the cosine formula
    num = ([a2[x] * b2[x] for x in intrsct])
    num_val = sum(num)

    #summing up the vectors which are part of the denominator
    s1 = sum([a2[x] ** 2 for x in list(a2.keys())])
    s2 = sum([b2[x] ** 2 for x in list(b2.keys())])

    #Denominator value of the Cosine function using squreroot and multiplying
    den_val = math.sqrt(s1) * math.sqrt(s2)

    #The final similarity score bewtween the two texts
    fnl_scr = float(num_val) / den_val

    #checking for the denominator value not to be zero
    if not den_val:
        fnl_scr = 0.0
    else:
        fnl_scr = float(num_val) / den_val

    #Printing the final value
    return "The similarity score between the 2 text samples is {}".format(str(fnl_scr))


if __name__ == "__main__":
 app.run(host="localhost", debug=True)