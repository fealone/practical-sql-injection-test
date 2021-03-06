from typing import List

from fastapi import APIRouter, Depends, HTTPException

from libs.database import get_db

from sqlalchemy.orm import Session


router = APIRouter()


request_error = HTTPException(
        status_code=404,
        detail="Not found"
        )


@router.get("/inject/list", tags=["users"])
async def get_list(db: Session = Depends(get_db)) -> List[str]:
    query = "select name from public limit 10;"
    result = db.execute(query)
    return [item[0] for item in result]


@router.get("/inject/list/{name}", tags=["users"])
async def get_item(name: str,
                   db: Session = Depends(get_db)) -> List[str]:
    query = "select name from public where name='{name}' limit 10;"
    try:
        result = db.execute(query.format(name=name))
        res = [item[0] for item in result]
    except Exception:
        raise request_error
    if not res:
        raise request_error
    return res
