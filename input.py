import random

random.seed(0)

ndarray = [[random.random() for _ in range(46)], [random.random()
                                                      for _ in range(46)]]

with open("./assets/input-data.txt", "w") as f:
    for _ in range(10000):
        data = '{ "data": { ' \
            + '"ndarray":' + '[[' + ', '.join(str(random.random()) for x in range(46)) \
            + '],[' + ', '.join(str(random.random()) for x in range(46)) + ']]' \
            + '}}\n'
        f.write(data)
