import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count(url):
    """
    Counts the number of [citation needed] tags in a given wikipedia article.

    :param url: A string containing the URL to a wikipedia page.
    :return: Integer equal to the number of [citation needed] tags that appear in the article.
    """
    # grab page content and turn it into a beautifulSoup object
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # find all the locations where the wikipedia page for citation needed is linked.
    results = soup.find_all(href="/wiki/Wikipedia:Citation_needed")
    # count how many results were found and return it.
    return results.__len__()


def get_citations_needed_report(url):
    """
    Returns a formatted string with all sentences that need citation in a given wikipedia page.

    :param url: A string containing the URL to a wikipedia page.
    :return: String with all sentences and sentence fragments that are followed by [citation needed] in the article.
    """
    report = ""
    # grab page content and turn it into a beautifulSoup object
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # Check if the page has any [citation needed]'s. if it does, proceed
    if soup.text.__contains__("[citation needed]"):
        result_list = []
        # create a list from the page text split by [citation needed] tags.
        split = soup.text.split("[citation needed]")
        # iterate through this list.
        for chunk in split:
            # use regex to split each chunk into a list of sentences, by splitting on a period followed by a space,
            # or a newline, or a period followed by (a) citation(s) (1-4 digits between square brackets, repeated one
            # or more times, followed by a space). The period must not be preceded by another period (implying
            # ellipsis), and must not be preceded by "i.e" or "e.g"
            sentences = re.split("(?<!i\.e)(?<!e\.g)(?<!\.)\. |\n|[^\.]\.(\[\d{1,4}\])+ ", chunk)
            # Append the last sentence of the chunk (the one with the [citation needed] tag) to result list.
            result_list.append(sentences[-1].strip())
        # With this method there's no semantic differentiation between an article that ends with a [citation needed]
        # and one that does not. Manually check if the last sentence of the final chunk should be included or not. If
        # the article doesn't end with the tag, then pop the last sentence from the results list.
        if not soup.text.endswith("[citation needed]"):
            result_list.pop(-1)
        # Concatenate the list to a string
        for i, result in enumerate(result_list):
            # Use the index to create a numbered list.
            report += str(i + 1) + ". " + result
            # Add two newlines between each sentence to clearly separate them.
            report += "\n\n"
        # The final two newlines aren't needed and are removed.
        report = report[:-2]
    # if the page doesn't have any [citation needed]'s, deliver a custom message saying as much.
    else:
        report = "No \"[citation needed]\" tags found in this document."
    # return the cleaned report to the user
    return report
