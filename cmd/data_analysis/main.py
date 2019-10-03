
def analyse(words):

    consumer_keywords = ["individual", "student", "on-demand", "entertainment", "free", "licence", "premium", "family",
                         "multiple devices", "privacy", "game", "streaming", "utility", "security", "proxy",
                         "anti-virus", "productivity", "note", "notes", "to-do list"]
    consumer_score = word_loop(words, consumer_keywords)

    prosumer_keywords = ["professional", "productivity", "tool", "design", "music", "video", "rendering", "production",
                         "developer", "development", "code", "render", "professional licence", "free trial", "price",
                         "pricing", "pro"]
    prosumer_score = word_loop(words, prosumer_keywords)

    self_serve_keywords = ["business", "team", "organisation", "project", "team dashboard", "one seat", "starter",
                           "basic", "per user", "growth", "free trial", "pay as you go", "credits", "price", "pricing",
                           "trial"]
    self_serve_score = word_loop(words, self_serve_keywords)

    sales_assisted_keywords = ["custom", "enterprise", "business", "talk to us", "speak to us", "sales team",
                               "let's talk", "scale", "price", "pricing", "Contact Sales", "Request Demo",
                               "chat with us", "package", "contact us", "proposal"]
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

