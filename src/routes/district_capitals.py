import json

from fastapi import APIRouter, HTTPException, status
from mongoengine.queryset.visitor import Q

from ..models.district_capitals_model import Capital as Capitals

router = APIRouter(tags=["District Capitals"], prefix="/district_capitals")


@router.get("/")
def get_all_district_capitals():

    response = json.loads(Capitals.objects().to_json())

    if len(response) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Items not found")

    return response


@router.get("/{name}")
def get_district_capitals_by_name_or_district(name: str):
    try:
        response = json.loads(
            Capitals.objects(Q(NAMECAP__icontains=name) | Q(DISTRICT__icontains=name)).to_json()
        )
        # if len(response) == 0:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND, detail=f"No Item Found with name {name}"
        #     )

        return response
    except AttributeError as e:

        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Item Found with that name"
        )


@router.get("/{id}")
def get_district_capitals_by_id(id: int):
    response = json.loads(Capitals.objects(COV_DIST_1=id).to_json())
    return response
