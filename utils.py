import urllib.request

# Returns session cookie read from file in the form `session=<value>`. The
# newline is automatically stripped.
def _get_session_cookie() -> bytes:
    cookie_file = open("cookie", "r")
    return cookie_file.read().strip()

# Reads the puzzle input for the given day from the official 2023 Advent of Code
# website. Uses my session cookie to log in.
def read_input(day: int) -> str:
    request = urllib.request.Request(
        "https://adventofcode.com/2023/day/{0}/input".format(day)
    )
    request.add_header("Cookie", _get_session_cookie())
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")

# Reads puzzle input from a file with the given filename. Used to locally test
# solutions.
def read_input_file(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()
