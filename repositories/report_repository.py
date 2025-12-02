from sqlmodel import Session, select
from models.report import Report


class ReportRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, report: Report) -> Report:
        self.session.add(report)
        self.session.commit()
        self.session.refresh(report)
        return report

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Report]:
        statement = (
            select(Report).order_by(Report.date.desc()).offset(skip).limit(limit)
        )
        return list(self.session.exec(statement).all())
