from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class MarketAuxArticleRequest(BaseModel):
    apiKey = str = Field("API Token")
    symbols: list[str] | None = Field(default = None, description = "Tickers mentioned")
    industries: list[str] | None = Field(default = None, description = "Technology, Industries")
    published_after: Optional[datetime] | None = Field(default = None, description = "Set day by day")
    limit = Optional[str] = Field(default = None, description = "Number of articles to return")

class MarketNewsArticleResponse(BaseModel):
    category: str

    datetime: datetime
    headline: str
    id: int
    image: str
    related: Optional[str] = None
    source: str
    summary: str
    url: str

# ALPHA VANTAGE

class AlphaVantageNewsArticleRequest(BaseModel):
    function: str = Field("NEWS_SENTIMENT", description="The function parameter specifies the type of data to retrieve. For news sentiment analysis, use NEWS_SENTIMENT.")
    tickers: Optional[List[str]] = Field(None, description="A comma-separated list of stock tickers to filter news articles by. For example: AAPL,MSFT,GOOGL.")
    # tickers=IBM will filter for articles that mention the IBM ticker; tickers=COIN,CRYPTO:BTC,FOREX:USD will filter for articles that simultaneously mention Coinbase (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) in their content.
    topics: Optional[List[str]] = Field(None, description="A comma-separated list of news topics to filter articles by. For example: technology,finance,health.")
    time_from: Optional[str]
    time_to: Optional[str]
    relevance: Optional[str]
    limit: Optional[int]
    apikey = str

