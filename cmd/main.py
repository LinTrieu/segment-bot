from inquirer import List, Text, Password, prompt
from data_collection.main import collect
from data_analysis.main import analyse

def getUrl() -> str:
    questions = [
        Text(
            'url',
            'Enter a URL',
        ),
    ]
    answers = prompt(questions, raise_keyboard_interrupt=True)

    return answers['url']


def handle() -> None:
    url = getUrl()
    words = collect(url)
    print(analyse(words))


if __name__ == "__main__":
    handle()
