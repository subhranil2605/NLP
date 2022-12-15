data = dict(
    c = ["Chinese Beijing Chinese", "Chinese Chinese Shanghai", "Chinese Macao"],
    j = ["Tokyo Japan Chinese"]
)


a = dict()
for key, value in data.items():
    l = []
    for val in value:
        l.extend(val.split())
    a.setdefault(key, []).extend(l)


b = dict()
for key, value in a.items():
    z = dict()
    for i in set(value):
        z.setdefault(i, value.count(i))
    b.setdefault(key, z)


def priors():
    j = dict()
    for key, value in data.items():
        j.setdefault(key, len(value))

    s = 0
    for key, value in j.items():
        s += value

    for key, value in j.items():
        j[key] /= s

    return j


def conditional_prob(word, class_):
    # count of "word" in a class
    count_w_c = b.get(class_).get(word) or 0

    # count of total words in a class
    count_c = sum(b.get(class_).values())

    # count of distinct words
    c = set()
    for key, value in b.items():
        for i in value.keys():
            c.add(i)
    V = len(c)

    return (count_w_c + 1) / (count_c + V)


def predict():
    result = dict()
    for key in data.keys():
        prob = priors().get(key) 
        for word in test_data.split():
            prob *= conditional_prob(word, key)
        result.setdefault(key, prob)
    return result


if __name__ == "__main__":
    test_data = "Chinese Chinese Chinese Tokyo Japan"
    print(predict())
