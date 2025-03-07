# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .beta_text_block import BetaTextBlock
from .beta_thinking_block import BetaThinkingBlock
from .beta_tool_use_block import BetaToolUseBlock
from .beta_redacted_thinking_block import BetaRedactedThinkingBlock

__all__ = ["BetaRawContentBlockStartEvent", "ContentBlock"]

ContentBlock: TypeAlias = Annotated[
    Union[BetaTextBlock, BetaToolUseBlock, BetaThinkingBlock, BetaRedactedThinkingBlock],
    PropertyInfo(discriminator="type"),
]


class BetaRawContentBlockStartEvent(BaseModel):
    content_block: ContentBlock

    index: int

    type: Literal["content_block_start"]
