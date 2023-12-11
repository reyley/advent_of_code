def read_file(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x.strip()


def read_file_not_strip(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x.strip("\n")
