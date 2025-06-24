from fastapi import APIRouter, Query
from agents.support_agent import SupportAgent
from agents.dashboard_agent import DashboardAgent

router = APIRouter()

# Instantiate agents
support_agent = SupportAgent()
dashboard_agent = DashboardAgent()

@router.get("/support")
def support_query(q: str = Query(..., description="Query for support agent")):
    result = support_agent.handle_query(q)
    return {"response": result}

@router.get("/dashboard")
def dashboard_query(q: str = Query(..., description="Query for dashboard agent")):
    result = dashboard_agent.handle_query(q)
    return {"response": result}
