from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = kernel.respond(message)
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7001))
    app.run(host='0.0.0.0', port=port, debug=True)
