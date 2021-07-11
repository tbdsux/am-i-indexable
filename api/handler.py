from hanapin import Google, Bing, DuckDuckGo, Ask

# define search engines
__SEARCH_ENGINES = {
    "google": Google,
    "bing": Bing,
    "duckduckgo": DuckDuckGo,
    "ask": Ask,
}


def search(website: str, query: str):
    try:
        hp = __SEARCH_ENGINES[website]
    except KeyError:
        return "Search Engine not yet supported"

    q = hp(query=query)

    return q.results()


def validate(query: str, results: list) -> bool:
    return any(query in i["link"] for i in results)
