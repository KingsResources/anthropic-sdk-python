# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BetaInputJSONDelta"]


class BetaInputJSONDelta(BaseModel):
    partial_json: str

    type: Literal["input_json_delta"]
