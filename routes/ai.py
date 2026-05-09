from fastapi import APIRouter
from controller.query import get_query_answer

router=APIRouter(prefix='/ai')

@router.get("/query/")
def query(q:str):
    return get_query_answer(q)