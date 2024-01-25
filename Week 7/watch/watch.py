import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        if url_pattern := re.search(
            r"(https?)*:\/\/(www\.)?(youtube\.com)\/embed\/([a-zA-Z0-9]+)", s
        ):
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()
