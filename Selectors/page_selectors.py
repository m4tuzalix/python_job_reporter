class justJoinIt:
    all_links = "div.css-1macblb > div > div"
    city = "div.css-1ihx907"
    bar_scroll = "div.css-1macblb"
    date_posted = "div.css-v6uxww div"

class linkedin:
    all_links =  "ul.jobs-search__results-list li"
    city = "span.job-result-card__location"
    bar_scroll = "html"
    date_posted = "time.job-result-card__listdate--new"
    #-----main.py used-----#
    search_results = "span.results-context-header__job-count"
    final_button = "button[class='infinite-scroller__show-more-button infinite-scroller__show-more-button--visible']"

class nofluffjobs: #// requests-html + bs4
    links = "a[data-cy='nfjPostingListItem']"
    pages = "a[class='page-link']"
    new = "sup[class='text-danger text-uppercase new-label hide-mobile']"

class pracuj:
    links = "ul.results__list-container > li.results__list-container-item"
    pages = "a.pagination_trigger"
    day = "span.offer-actions__date"