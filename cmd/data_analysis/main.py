
def analyse(words):

    consumer_keywords = ['html', 'list', 'consumer', 'html', 'hello', 'html', 'html']
    consumer_score = word_loop(words, consumer_keywords)

    prosumer_keywords = ['html', 'list', 'consumer', 'html', 'hello', 'some']
    prosumer_score = word_loop(words, prosumer_keywords)

    self_serve_keywords = ['list', 'consumer', 'hello']
    self_serve_score = word_loop(words, self_serve_keywords)

    sales_assisted_keywords = ['list', 'consumer', 'html', 'hello']
    sales_assisted_score = word_loop(words, sales_assisted_keywords)

    return {
        "consumer_score": consumer_score,
        "prosumer_score": prosumer_score,
        "self_serve_score": self_serve_score,
        "sales_assisted_score": sales_assisted_score,
    }

def word_loop(words, keywords):

    counter = 0

    for i in words:
        if i in keywords:
            counter += 1

    return counter






    # v1
    # return {
    #     "consumer_score": 0,
    #     "prosumer_score": 1,
    #     "self_serve_score": 2,
    #     "sales_assisted_score": 3,
    # }

    # v2
    # return {
    #     "consumer": {
    #         "score" : 1,
    #         "words": {
    #             "foo",
    #             "bar",
    #         }
    #     },
    #     "prosumer": {
    #         "score" : 1,
    #         "words": {
    #             "foo",
    #             "bar",
    #         }
    #     },
    #     "self_serve": {
    #         "score" : 1,
    #         "words": {
    #             "foo",
    #             "bar",
    #         }
    #     },
    #     "sales_assisted": {
    #         "score" : 1,
    #         "words": {
    #             "foo",
    #             "bar",
    #         }
    #     },
    # }

