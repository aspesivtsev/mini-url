from flask import Flask, url_for, render_template, request
import url_creator

app = Flask (__name__)

@app.route('/')
def api_root():
    return '<form action="/url" method="GET"><input name="url"><input type="submit" value="Create Small Url"></form>'
    #return render_template('input_form.html')


@app.route('/url')
def api_url():
    orig_url = request.args.get('url', '')
    return "Your new short URL is: " + url_creator.smallurl(orig_url)
    #return "You said: " + request.args.get('url', '')
    #return 'Url requester' + url_for('api_url')




if __name__=="main":
    app.run()
