from time import sleep

import requests
import click


def check_url(url):
    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError:
        click.secho(f"ConnectionError: Can't reach {url} URL", fg="blue")
    else:
        return response.status_code


@click.command()
@click.argument("urls", nargs=-1)
@click.option("--daemon", "-d", default=False, is_flag=True)
def check(urls, daemon):
    while True:
        for url in urls:
            status_code = check_url(url)
            if status_code:
                colorize_status(url, status_code)
        if not daemon:
            break
        sleep(3)


def colorize_status(url, status):
    colours = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red"
    }
    click.secho(f"{url} --> {status}", fg=colours.get(status // 100, "magenta"))


if __name__ == "__main__":
    check()
