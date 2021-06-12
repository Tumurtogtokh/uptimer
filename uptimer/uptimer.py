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
@click.argument("url")
def check(url):
    status_code = check_url(url)
    if status_code:
        colorize_status(url, status_code)


def colorize_status(url, status):
    colours = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
        -1: "magenta"
    }
    click.secho(f"{url} --> {status}", fg=colours.get(status // 100, -1))


if __name__ == "__main__":
    check()
