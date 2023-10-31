from flask import Flask, request, render_template

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

application = Flask(__name__)
app = application

@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route("/review", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            searchstring = request.form['content'].replace(" ", "")
            ebay_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=" + searchstring
            uclient = uReq(ebay_url)
            ebaypage = uclient.read()
            uclient.close()
            ebay_html = bs(ebaypage, "html.parser")
            bigboxes = ebay_html.findAll("div", {"class": "s-item__wrapper clearfix"})
            del bigboxes[0:1]
            box = bigboxes[0]
            productlink = box.div.div.a['href']
            productreq = requests.get(productlink)
            prod_html = bs(productreq.text, "html.parser")
            #print(prod_html)
            comment_box = prod_html.find_all("div", {"class": "fdbk-container__details__comment"})
            reviews = []
            reviews1 = []
            for comment in comment_box:
                try:
                    feedback = comment.text
                except:
                    feedback = 'No feedback'

                mydict = {"Feedback": feedback}
                reviews.append(mydict)

            comment_box = prod_html.find_all("ul", {"class": "fdbk-container__details__info__divide"})
            for comment in comment_box:
                try:
                    time_of_comment = comment.text
                    print((time_of_comment))
                except:
                    time_of_comment = "No Time"

                mydict1 = {"Time_of_comment": time_of_comment}
                reviews1.append(mydict1)
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)], reviews1 = reviews1[0:(len(reviews1) - 1)])

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
