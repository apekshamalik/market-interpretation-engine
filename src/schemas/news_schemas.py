from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

# FINNHUB
class MarketNewsArticleRequest(BaseModel):
    category: str = Field(..., description="The category of news to retrieve. Possible values include: general, forex, crypto, merger")
    minId: Optional[int] = Field(None, description="The minimum news article ID to retrieve. This can be used for pagination.")

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

