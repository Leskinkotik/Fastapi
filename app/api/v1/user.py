from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return [{"user_name" : "Adriane"}, {"user_name" : "Lesia"}]

@router.get("/user_all")
async def get_all():
    calc = 2 + 5
    return[{"CouCou" : "Hello World"}, {"All" : "super"}, {"calc":calc}]
