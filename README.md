# Wikipedia [citation needed] scraper

A simple python web scraper script with two functions relating to the [citation needed] tag on wikipedia. One counts the number of appearances of the tag and the other returns a formatted string with each sentence that needs citation. Created using the requests library and the BeautifulSoup4 library, as well as regex.

* `get_citations_needed_count`
  * Counts the number of [citation needed] tags in a given wikipedia article.
  * Parameter: A string containing the URL to a wikipedia page.
  * Returns: An integer equal to the number of [citation needed] tags that appear in the article.
* `get_citations_needed_report`
  * Returns a formatted string with all sentences that need citation in a given wikipedia page.
  * Parameter: A string containing the URL to a wikipedia page.
  * Returns: A string with all sentences and sentence fragments that are followed by [citation needed] in the article.