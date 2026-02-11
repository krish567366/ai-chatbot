from fastapi import APIRouter

router = APIRouter(prefix="/calls", tags=["calls"])


@router.get("/")
async def list_calls():
	return []