from pyfiglet import figlet_format
from random import randint
from termcolor import colored
import requests


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "magenta"

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


def do_request(topic):
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": topic}
    )
    if response.status_code == 200:
        data = response.json()
        return data
    return None


def show_one_result_random(results, topic):
    number_jokes = len(results)
    # En la solución lo hace con choice sobre la lista de results
    random_index = randint(0, number_jokes)
    print(f"I've got {number_jokes} about {topic}. Here's one: ")
    print(results[random_index]["joke"])


def main():
    print_art("Dad Joke 3000", color="magenta")
    topic = input("Let me tell you a joke! Give me a topic: ")
    result_req = do_request(topic)

    if result_req is None:
        print("There was a problem in the request")
        return

    results = result_req["results"]
    if len(results) == 0:
        print(f"Sorry, I don't have any jokes about {topic}! Please try again")
    elif len(results) == 1:
        print("I've got one joke about fruit. Here it is:")
        print(results[0]["joke"])
    else:
        show_one_result_random(results, topic)


if __name__ == "__main__":
    main()
