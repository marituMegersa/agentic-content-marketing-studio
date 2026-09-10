from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.content_marketing_studio.schemas import AgenticContentMarketingStudioSessionCreate, AgenticContentMarketingStudioSessionResponse
from app.domain.content_marketing_studio.service import AgenticContentMarketingStudioService

router = APIRouter(prefix="/api/v1/content_marketing_studio", tags=["Agentic Content Marketing Studio Domain"])

@router.post("/sessions", response_model=AgenticContentMarketingStudioSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticContentMarketingStudioSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Content Marketing Studio.
    """
    return AgenticContentMarketingStudioService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticContentMarketingStudioSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticContentMarketingStudioService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
