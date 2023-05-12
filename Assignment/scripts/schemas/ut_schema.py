from typing import Optional

from pydantic import BaseModel


class GetSample(BaseModel):
    project_id: str
    sample_id: str
    page_type: Optional[str]
