
def analyse(words):

    # v1
    return {
        "consumer_score": 0,
        "prosumer_score": 1,
        "self_serve_score": 2,
        "sales_assisted_score": 3,
    }

    # v2
    return {
        "consumer": {
            "score" : 1,
            "words": {
                "foo",
                "bar",
            }
        },
        "prosumer": {
            "score" : 1,
            "words": {
                "foo",
                "bar",
            }
        },
        "self_serve": {
            "score" : 1,
            "words": {
                "foo",
                "bar",
            }
        },
        "sales_assisted": {
            "score" : 1,
            "words": {
                "foo",
                "bar",
            }
        },
    }

