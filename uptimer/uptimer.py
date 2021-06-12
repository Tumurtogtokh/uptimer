import requests
import click


def check_url(url):
    response = requests.head(url)
    return response.status_code


@click.command()
@click.argument("url")
def check(url):
    status_code = check_url(url)
    print(status_code)


if __name__ == "__main__":
    check()
