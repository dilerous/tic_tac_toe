app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

sse.publish({"message": datetime.datetime.now()}, type='publish')


source = new EventSource("{{ url_for('sse.stream') }}");
    source.addEventListener('publish', function(event) {
        data = JSON.parse(event.data);
        console.log("The server says " + data.message);
    }, false);
    source.addEventListener('error', function(event) {
        console.log("Error"+ event)
        alert("Failed to connect to event stream. Is Redis running?");
    }, false);
