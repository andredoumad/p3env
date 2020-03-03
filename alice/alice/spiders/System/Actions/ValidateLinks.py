

# We want some coloration so we import the tool do to that :)
from PyFunceble import initiate_colorama, Fore, Style
# We import the tool to print the colored CLI historyo.
from PyFunceble.cli_core import CLICore
# We import the configuration loader.
from PyFunceble import load_config
# We import the test method of the PyFunceble API.
from PyFunceble import url_test as PyFunceble




def print_result(subject, status):
    """
    Given the subject and its status, we print it to STDOUT.

    :param str subject: The subject we are going to print.
    :param str status: The status of the domain.
    """

    if status == "ACTIVE":
        print(f"{Fore.GREEN + Style.BRIGHT}{domain} is {status}")
    elif status == "INACTIVE":
        print(f"{Fore.RED + Style.BRIGHT}{domain} is {status}")
    else:
        print(f"{Fore.CYAN + Style.BRIGHT}{domain} is {status}")

for url in URLS:
    # We loop through the list of domain.

    # And we print the domain and status with the right coloration!
    print_result(url, PyFunceble(url))
2