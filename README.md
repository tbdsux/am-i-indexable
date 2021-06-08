# Am I Indexable ?

Simple mini-project to check if website is indexed or searchable in `web search engines`.

## What it does?

- It just checks the query if it exists in the search links.
  - Example: **query**: `github.com`, it will be compared to the search results
- If there is a match, it will be returned as `searchable`

**NOTE:** `this is not accurate, it could not return correctly, and it depends on the library scraper if it works well`

### Screenshot

![screenshot](./screenshot.png)

## Development

Use the `vercel` CLI

    $ vercel dev

- Tailwind CSS

  - development css

        $ yarn dev-css

  - production css

        $ yarn build-css

- Run Only Svelte

        $ yarn dev

### Folder Structure

- **`api`** - simple backend api (python, `fastapi`)
- **`public`, `scripts`, `src`** - frontend (`SVELTE`)

##

### &copy; TheBoringDude | 2021
