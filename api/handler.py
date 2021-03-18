from hanapin import Google, Bing, DuckDuckGo

# define search engines
__SEARCH_ENGINES = {
    "google": Google,
    "bing": Bing,
    "duckduckgo": DuckDuckGo
}


def search(website: str, query: str):
    try:
        hp = __SEARCH_ENGINES[website]
    except KeyError:
        return "Search Engine not yet supported"

    q = hp(query=query)

    return q.results()


def validate(query: str, results: list) -> bool:
    for i in results:
        if query in i["link"]:
            return True

    return False