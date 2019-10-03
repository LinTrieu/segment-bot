
def analyse(webpage_string):

    webpage_string =webpage_string.lower()

    consumer_keywords = ["individual", "student", "on-demand", "entertainment", "free", "licence", "premium", "family",
                         "multiple devices", "privacy", "game", "streaming", "utility", "security", "proxy",
                         "anti-virus", "productivity", "note", "notes", "to-do list"]
    consumer_score, consumer_words = word_loop(consumer_keywords, webpage_string)

    prosumer_keywords = ["professional", "productivity", "tool", "design", "music", "video", "rendering", "production",
                         "developer", "development", "code", "render", "professional licence", "free trial", "price",
                         "pricing", "pro"]
    prosumer_score, prosumer_words = word_loop(prosumer_keywords, webpage_string)

    self_serve_keywords = ["business", "team", "organisation", "project", "team dashboard", "one seat", "starter",
                           "basic", "per user", "growth", "free trial", "pay as you go", "credits", "price", "pricing",
                           "trial"]
    self_serve_score, self_serve_words = word_loop(self_serve_keywords, webpage_string)

    sales_assisted_keywords = ["custom", "enterprise", "business", "talk to us", "speak to us", "sales team",
                               "let's talk", "scale", "price", "pricing", "contact sales", "request demo",
                               "chat with us", "package", "contact us", "proposal"]
    sales_assisted_score, sales_assisted_words = word_loop(sales_assisted_keywords, webpage_string)

    return {
        "consumer": {
            "score": consumer_score,
            "words": consumer_words
        },
        "prosumer": {
            "score": prosumer_score,
            "words": prosumer_words
        },
        "self-serve business": {
            "score": self_serve_score,
            "words": self_serve_words
        },
        "sales-assisted business": {
            "score": sales_assisted_score,
            "words": sales_assisted_words
        },
    }

def word_loop(keywords, webpage_string):

    counter = 0
    target_user_words = []

    for i in keywords:
        if i in webpage_string:
            counter += 1
            if i not in target_user_words:
                target_user_words.append(i)

    return counter, target_user_words


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

