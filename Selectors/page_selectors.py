class justJoinIt:
    all_links = "div.css-1macblb > div > div"
    city = "div.css-1ihx907"
    bar_scroll = "div.css-1macblb"
    date_posted = "div.css-v6uxww div"
    position = "div.css-wjfk7i"

class linkedin:
    all_links =  "ul.jobs-search__results-list li"
    city = "span.job-result-card__location"
    bar_scroll = "html"
    date_posted = "time.job-result-card__listdate--new"
    position = "h3.result-card__title.job-result-card__title"
    #-----main.py used-----#
    search_results = "span.results-context-header__job-count"
    final_button = "button[class='infinite-scroller__show-more-button infinite-scroller__show-more-button--visible']"

class nofluffjobs: #// requests-html + bs4
    links = "a[data-cy='nfjPostingListItem']"
    pages = "a[class='page-link']"
    new = "sup[class='text-danger text-uppercase new-label hide-mobile']"
    position = "h4.posting-title__position"

class pracuj:
    links = "div#results > ul.results__list-container > li.results__list-container-item"
    next_page = "i[class='mdi mdi-chevron-right pagination_element-icon']"
    day = "span.offer-actions__date"
    position = "a.offer-details__title-link"