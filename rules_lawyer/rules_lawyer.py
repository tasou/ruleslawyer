from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')


# This function name is what you defined when you create an
# AWS Lambda function. By default, AWS calls this function
# lambda_handler.
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)


if __name__ == '__main__':
    app.run(debug=True)
