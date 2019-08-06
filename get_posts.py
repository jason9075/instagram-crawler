import csv
import json
import os

from inscrawler import InsCrawler

NUMBER = 200


def main():
    name_list = []
    with open('0805_IG_Jason.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)

        for row in rows:
            name_list.append(row[0].split('/')[-2])

    for name in name_list:
        output_path = os.path.join('output', f'{name}.json')
        if os.path.exists(output_path):
            continue

        print(f'process {name}')
        data = get_posts_by_user(name, NUMBER)
        if data is not None:
            output(data, output_path)
        else:
            output([], output_path)


def get_posts_by_user(username, number):
    ins_crawler = InsCrawler(has_screen=False)
    return ins_crawler.get_user_posts(username, number)


def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)
    if filepath:
        with open(filepath, "w", encoding="utf8") as f:
            f.write(out)
    else:
        print(out)


if __name__ == '__main__':
    main()
