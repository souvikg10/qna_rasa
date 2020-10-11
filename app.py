import flask
from flask import request
from allennlp.predictors.predictor import Predictor


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.predictor = Predictor.from_path(
    "https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2020.03.19.tar.gz"
)


@app.route("/chat", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        question = data["question"]
        answer = _predict_answer(question)
        response = {"answer": answer}
    return response


def _predict_answer(question):
    content = """
    In software testing, test automation is the use of software separate from the software being tested to control the execution of tests and the comparison of actual outcomes with predicted outcomes.[1] Test automation can automate some repetitive but necessary tasks in a formalized testing process already in place, or perform additional testing that would be difficult to do manually. Test automation is critical for continuous delivery and continuous testing.
    There are many approaches to test automation, however below are the general approaches used widely:
    - Graphical user interface testing. A testing framework that generates user interface events such as keystrokes and mouse clicks, and observes the changes that result in the user interface, to validate that the observable behavior of the program is correct.
    - API driven testing. A testing framework that uses a programming interface to the application to validate the behaviour under test. Typically API driven testing bypasses application user interface altogether. It can also be testing public (usually) interfaces to classes, modules or libraries are tested with a variety of input arguments to validate that the results that are returned are correct.
    One way to generate test cases automatically is model-based testing through use of a model of the system for test case generation, but research continues into a variety of alternative methodologies for doing so.[citation needed] In some cases, the model-based approach enables non-technical users to create automated business test cases in plain English so that no programming of any kind is needed in order to configure them for multiple operating systems, browsers, and smart devices.[2]
    What to automate, when to automate, or even whether one really needs automation are crucial decisions which the testing (or development) team must make.[3] A multi-vocal literature review of 52 practitioner and 26 academic sources found that five main factors to consider in test automation decision are: 1) System Under Test (SUT), 2) the types and numbers of tests, 3) test-tool, 4) human and organizational topics, and 5) cross-cutting factors. The most frequent individual factors identified in the study were: need for regression testing, economic factors, and maturity of SUT.[4]
    A growing trend in software development is the use of unit testing frameworks such as the xUnit frameworks (for example, JUnit and NUnit) that allow the execution of unit tests to determine whether various sections of the code are acting as expected under various circumstances. Test cases describe tests that need to be run on the program to verify that the program runs as expected.
    """
    predict = app.predictor.predict(passage=content, question=question)
    return predict["best_span_str"]


app.run(host="0.0.0.0")
