from fastapi import APIRouter
from app.services.hermes_service import HermesService
from app.models.run_record import RunRecord
from app.models.weight_record import WeightRecord
from typing import List

hermes_service = HermesService()


weight_router = APIRouter(prefix="/weight", tags=["Weight"])


@weight_router.post("/", response_model=WeightRecord)
def create_weight_record(weight_record: WeightRecord):
    """Route method to Create a new weight record"""
    hermes_service.create_weight_record(weight_record)
    return weight_record


@weight_router.get("/", response_model=List[WeightRecord])
def get_all_weight():
    """Route method to Read all new weight records"""
    return hermes_service.get_all_weight_records()


@weight_router.put("/{weight_record_id}", response_model=WeightRecord)
def update_weight_record(record_id: int, weight_record: WeightRecord):
    """Route method to Update a weight record"""
    hermes_service.update_weight_record(
        weight_record_id=record_id, weight_record=weight_record)
    return weight_record


@weight_router.delete("/{weight_record_id}")
def delete_weight_record(weight_record_id: int):
    """Route method to Delete a weight records"""
    response = hermes_service.delete_weight_record(
        weight_record_id=weight_record_id)
    return response


run_router = APIRouter(prefix="/run", tags=["Run Records"])


@run_router.post("/run_record")
def create_run_record(run_record: RunRecord):
    return hermes_service.create_run_record(run_record)


@run_router.get("/run_records")
def get_all_run_records():
    return hermes_service.get_all_run_records()
