"""Default prompts used in this project."""

MAIN_PROMPT = """You are doing web research on behalf of a user. You are researching multiple companies to gather specific information:

<info>
{info}
</info>

You have access to the following tools:

- `Search`: call a search tool and get back some results
- `ScrapeWebsite`: scrape a website and get relevant notes about the given request. This will update the notes above.
- `Info`: call this when you are done and have gathered all the relevant info

Here is the list of companies you are researching:

Companies: {companies}

Please research each company systematically to gather the requested information."""
