"""Wikipedia API exercise."""

import wikipedia
from wikipedia import DisambiguationError, PageError

page_title = input("Enter page title: ").lower()
while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary.strip())
        print(page.url)
        print()
    except DisambiguationError:
        print(f'Page id "{page_title}" does not match any pages. Try another id!')
    except PageError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(page_title))
    page_title = input("Enter page title: ").lower()
print("Thank you.")
