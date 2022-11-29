import json

from fastapi import APIRouter

from ..models.district_capitals_model import Capital as Capitals

router = APIRouter(tags=["District Capitals"], prefix="/district_capitals")


@router.get("/")
def get_all_district_capitals():
    response = json.loads(Capitals.objects().to_json())

    return response


@router.get("/{id}")
def get_district_capitals_by_id(id: int):
    response = json.loads(Capitals.objects(COV_DIST_1=id).to_json())
    return response
