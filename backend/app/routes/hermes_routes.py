from fastapi import APIRouter
from app.services.hermes_service import HermesService
from app.models.run_record import RunRecord

router = APIRouter()
hermes_service = HermesService()


@router.get("/")
def read_root():
    return {"Hello World"}


@router.post("/weight")
def create_weight_record():
    print("**1**")
    response = hermes_service.create_weight_record()
    return response


@router.get("/weight")
def get_all_weight():
    return hermes_service.get_all_weight_records()


@router.post("/run_record")
def create_run_record(run_record: RunRecord):
    return hermes_service.create_run_record(run_record)


@router.get("/run_records")
def get_all_run_records():
    return hermes_service.get_all_run_records()
