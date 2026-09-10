from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.content_marketing_studio.models import AgenticContentMarketingStudioSession, AgenticContentMarketingStudioItem
from app.domain.content_marketing_studio.schemas import AgenticContentMarketingStudioSessionCreate, AgenticContentMarketingStudioItemCreate

class AgenticContentMarketingStudioService:
    @staticmethod
    def create_session(db: Session, data: AgenticContentMarketingStudioSessionCreate) -> AgenticContentMarketingStudioSession:
        db_obj = AgenticContentMarketingStudioSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticContentMarketingStudioSession:
        return db.query(AgenticContentMarketingStudioSession).filter(AgenticContentMarketingStudioSession.id == session_id).first()
