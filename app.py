from flask import Flask, render_template, request, redirect, jsonify,url_for, send_from_directory, send_file
from charts import bar_chart, line_chart, stacked_chart, polar_chart
from maps import current_location
import webbrowser


# Create Flask app
app = Flask(__name__)

# Define home route
@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        latitude, longitude = current_location()
        bar_chart_data = bar_chart()
        line_chart_data = line_chart()
        stacked_chart_data = stacked_chart()
        polar_chart_data = polar_chart()
        return render_template('index.html', lat=latitude, lng=longitude, bar_chart_data=bar_chart_data, line_chart_data=line_chart_data, stacked_chart_data=stacked_chart_data, polar_chart_data=polar_chart_data)

    except:
        # Handle any other exceptions
        return render_template('pages-error-404.html'), 500


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        return render_template('pages-login.html')
    except:
        # Handle any other exceptions
        return render_template('pages-error-404.html'), 500
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        return render_template('pages-register.html')
    except:
        # Handle any other exceptions
        return render_template('pages-error-404.html'), 500
    
    
@app.route('/video_feed')
def video_feed():
    return send_file('static/assets/video.mp4', mimetype='video/mp4')

@app.route('/dock_feed1')
def dock_feed1():
    return send_file('static/assets/dock1.mp4', mimetype='video/mp4')

@app.route('/dock_feed2')
def dock_feed2():
    return send_file('static/assets/dock2.mp4', mimetype='video/mp4')

@app.route('/dock_feed3')
def dock_feed3():
    return send_file('static/assets/dock3.mp4', mimetype='video/mp4')

@app.route('/dock_feed4')
def dock_feed4():
    return send_file('static/assets/dock4.mp4', mimetype='video/mp4')

@app.route('/dock_feed5')
def dock_feed5():
    return send_file('static/assets/dock5.mp4', mimetype='video/mp4')

@app.route('/dock_feed6')
def dock_feed6():
    return send_file('static/assets/dock6.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed1')
def CCTV_feed1():
    return send_file('static/assets/CCTV1.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed2')
def CCTV_feed2():
    return send_file('static/assets/CCTV2.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed3')
def CCTV_feed3():
    return send_file('static/assets/CCTV3.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed4')
def CCTV_feed4():
    return send_file('static/assets/CCTV4.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed5')
def CCTV_feed5():
    return send_file('static/assets/CCTV5.mp4', mimetype='video/mp4')

@app.route('/CCTV_feed6')
def CCTV_feed6():
    return send_file('static/assets/CCTV6.mp4', mimetype='video/mp4')

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True, port=5000)