from flask import Flask, jsonify, request
 
from MachineLearning.analyze_question import AnalysisQuestion
from KnowledgeGraph.get_answer import Get_answer

app = Flask(__name__)

aq = AnalysisQuestion()
ga = Get_answer()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/query", methods=["POST"])
def query(): 
    request_data = request.get_json()
    question = request_data.get("question", "")
    answer=''
    if question:
        index, params = aq.analysis_question(question)
        answers = ga.get_data(index, params)

        for ans in answers:
            answer+=(ans[0]+',')
 
        # answer = bot.chat_main(question, user_id='000')
        # answer = request_data.get("question", "")
    else:
        answer = "Sorry, what did you say?"
    return jsonify({"answer": answer})