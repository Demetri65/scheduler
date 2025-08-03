"""
FastAPI router for /v1/schedule
"""
import os
from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from agents import Runner
from ..agent_setup import build_agent
load_dotenv()

# -----------------------------------------------------------------------------
# Auth helper
# -----------------------------------------------------------------------------
API_TOKEN: str = os.getenv("API_TOKEN", "change-me")   # load once at startup

def auth(x_api_key: str | None = Header(default=None, alias="X-API-KEY")) -> None:
    """Simple header-based authentication."""
    if API_TOKEN == "change-me":
        raise RuntimeError(
            "API_TOKEN env-var not set.  Define it in .env or deployment secrets."
        )
    if x_api_key != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

# -----------------------------------------------------------------------------
# Request/response models
# -----------------------------------------------------------------------------
class ScheduleReq(BaseModel):
    prompt: str

class ScheduleResp(BaseModel):
    reply: str

# -----------------------------------------------------------------------------
# FastAPI router & app
# -----------------------------------------------------------------------------
router = APIRouter(prefix="/v1")
_agent = build_agent()                  # singleton reused across requests

@router.post("/schedule", response_model=ScheduleResp, dependencies=[Depends(auth)])
async def schedule(req: ScheduleReq) -> ScheduleResp:
    result = await Runner.run(_agent, input=req.prompt)
    return ScheduleResp(reply=result.final_output)

app = FastAPI(title="Calendar Scheduler API")
app.include_router(router)