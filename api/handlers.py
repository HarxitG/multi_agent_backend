from fastapi import APIRouter
from agents.support_agent import SupportAgent
from agents.dashboard_agent import DashboardAgent

router = APIRouter()
support_agent = SupportAgent()
dashboard_agent = DashboardAgent()

@router.get("/support")
def support_query(q: str):
    return support_agent.handle_query(q)

@router.get("/dashboard")
def dashboard_query(q: str):
    return dashboard_agent.handle_query(q)
