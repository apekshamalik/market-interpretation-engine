# my tech stack

This is going to be a web app developed in Python. 
- FastAPI to serve data (coupled w Pydantic)
- Postgres


Want to tackle raw data, make a more explanatory framework all served in one place. Obviously Bloomberg, AlphaSense, etc., have platforms to serve market data at a very granular level, but they just serve. Though they provide news, I want a more explanatory layer, to understand the world a bit better.Event Ingestion Service — Polls or subscribes to news/data APIs on a schedule. Normalizes heterogeneous source formats into a unified Event schema. Deduplicates across sources. Persists to event store with timestamps.
Market Data Service — Pulls intraday and EOD price data for a defined instrument universe (initially: SPY, QQQ, TLT, VIX, GLD, USO, sector ETFs). Stores snapshots at configurable intervals (e.g., 5-minute bars during market hours). Computes returns over relevant windows.
Interpretation Engine — The core logic. Takes a time window (e.g., today's trading session), retrieves all events and price data within it, and produces an Interpretation object. This is where channel classification, driver ranking, and narrative generation happen. Initial implementation uses rule-based heuristics. Future versions could incorporate an LLM for narrative generation, but the structured reasoning layer should remain deterministic and inspectable.
API Server — Exposes interpretation results, historical archive, and event/market data via REST endpoints. Serves the frontend.
Frontend — Renders the daily briefing. Displays the structured interpretation in a format modeled on a sell-side desk note: concise, scannable, causal. Supports historical browsing and search.

First phase:
Set up schema for events and market data
Build ingestion pipelines

## Documenting Decisions
Why I chose Postgres: I didn't want a NoSQL database, the market and news data I am working with is inherently relational. In querying Claude to get a better understanding of tech stack, I see that querying on nested semi-structured data

Marketaux for financial news
Finnhub ticker prices
NewsAPI for News Data

Marketaux has market data endpints as well as a news endpoint that will act as source of truth, with newsapi providing the human readable context

Use ORM between Pydantic and Postgres ingestion