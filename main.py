from data_collection.main import collect
from inquirer import List, Text, Password, prompt
from data_analysis.main import analyse
import json

def getUrl() -> str:
    questions = [
        Text(
            'url',
            'Enter a URL',
        ),
    ]
    answers = prompt(questions, raise_keyboard_interrupt=True)

    return answers['url']


def cli_handler() -> None:
    url = getUrl()
    words = collect(url)
    print(analyse(words))


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        "headers": {
            "Content-Type": "application/json",
            "header2Name": "header2Value",
        },
    }

if __name__ == "__main__":
    cli_handler()
