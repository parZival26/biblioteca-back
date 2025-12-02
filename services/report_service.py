from repositories.report_repository import ReportRepository
from models.report import Report
from schemas.report_schema import ReportCreate


class ReportService:
    def __init__(self, repository: ReportRepository):
        self.repository = repository

    def create_report(self, report_data: ReportCreate) -> Report:
        report = Report(**report_data.model_dump())
        return self.repository.create(report)

    def list_reports(self, skip: int = 0, limit: int = 100) -> list[Report]:
        return self.repository.get_all(skip, limit)
