import pathlib
from pydantic import BaseModel
from typing import Union
import pathlib
from typing import Optional
from src.data import load_json_data
from src.schemas.news_schemas import TieredNewsItem

TIER_BIAS_PATH = pathlib.Path("src/data/tiers.json")
TIER_BIAS_INDEX = load_json_data(TIER_BIAS_PATH)

def get_tier_for_source(source_uri: str) -> str | None:
    domain = source_uri.lower()

    return TIER_BIAS_INDEX.get(domain, "REJECTED")

