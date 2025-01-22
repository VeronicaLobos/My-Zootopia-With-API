import requests

REQUEST_URL =  "https://www.wikipedia.com/"

def preview_html_file(html_file_name, chrs_to_display):
    with open(html_file_name, 'r') as handle:
        content = handle.read()

    print(content[:chrs_to_display])


def create_html_file(html_file_name, url_text):
    with open(html_file_name, 'w', encoding="utf-8") as handle:
        handle.write(url_text)


def main():
    res = requests.get(REQUEST_URL)
    print(res.status_code)
    get_url_text = res.text
    html_file_name = "wikipedia_html_template.html"
    create_html_file(html_file_name, get_url_text)
    preview_html_file(html_file_name, 150)


if __name__ == "__main__":
    main()