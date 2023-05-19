from fastapi import APIRouter, Depends

from scripts.api import EndPoints
from scripts.core.handlers.ut_handler import UTHandler
from scripts.logging import logger
from scripts.schemas.response_models import DefaultFailureResponse, DefaultResponse

from scripts.schemas.ut_schema import GetSample
from scripts.utils.cookie_decorator import MetaInfoCookie, MetaInfoSchema
from scripts.utils.security_utils.decorators import CookieAuthentication

ut_router = APIRouter(prefix=EndPoints.api_ut, tags=["UT Sample Service"])
auth = CookieAuthentication()
get_cookies = MetaInfoCookie()


@ut_router.post(EndPoints.api_get_sample)
async def get_sample_data(
    request_data: GetSample, meta: MetaInfoSchema = Depends(get_cookies)
):
    """
    API to get sample data
    """
    try:
        ut_handler = UTHandler(project_id=meta.project_id)
        response = await ut_handler.get_sample_data(request_data)
        return DefaultResponse(message="Success", data=response)
    except Exception as e:
        logger.exception(f"Exception while getting sample data: {e}")
        return DefaultFailureResponse(
            message="Failed to get sample", error=str(e)
        ).dict()
