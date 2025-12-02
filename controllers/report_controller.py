from fastapi import APIRouter, status
from typing import Annotated
from sqlmodel import Session
from fastapi import Depends

from schemas.report_schema import ReportCreate, ReportResponse
from repositories.report_repository import ReportRepository
from services.report_service import ReportService
from database import get_session


router = APIRouter(prefix="/reports", tags=["reports"])


def get_report_service(session: Session = Depends(get_session)) -> ReportService:
    repository = ReportRepository(session)
    return ReportService(repository)


@router.post("/", response_model=ReportResponse, status_code=status.HTTP_201_CREATED)
def create_report(
    report: ReportCreate, service: Annotated[ReportService, Depends(get_report_service)]
):
    """Create a new report"""
    return service.create_report(report)


@router.get("/", response_model=list[ReportResponse])
def list_reports(
    service: Annotated[ReportService, Depends(get_report_service)],
    skip: int = 0,
    limit: int = 100,
):
    """List all reports with pagination, sorted by date (newest first)"""
    return service.list_reports(skip=skip, limit=limit)
