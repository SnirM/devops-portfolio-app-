from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/version")
def version():
    return {"version": "1.0.0"}
