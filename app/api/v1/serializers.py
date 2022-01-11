from typing import Union, Optional

from pydantic import BaseModel


class ResponseSerializer(BaseModel):
    status: int
    message: Optional[str]
    data: Union[dict, list]
