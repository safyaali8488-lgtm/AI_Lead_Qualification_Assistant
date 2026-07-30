import sys
from pathlib import Path

# Ensure lead_scorer.py (and its own "from rubric import MAX_SCORE") resolves
# regardless of the working directory the API is launched from.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lead_scorer import score_lead  # signature: score_lead(lead: dict) -> tuple[int, str]

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

AGENT_NAME = "AI Lead Qualification & Sales Assistant"


class LeadRequest(BaseModel):
    name: str
    company: str
    customer_message: str


@app.post("/lead-score")
def lead_score(payload: LeadRequest):
    input_data = payload.model_dump()

    try:
        # score_lead() only reads lead["message"]; name/company are passed
        # through for parity with the original sample_leads.json shape.
        lead = {
            "name": payload.name,
            "company": payload.company,
            "message": payload.customer_message,
        }
        score, next_action = score_lead(lead)

        return {
            "agent": AGENT_NAME,
            "input": input_data,
            "output": {
                "score": score,
                "next_action": next_action,
            },
            "status": "success",
        }
    except Exception as exc:
        return {
            "agent": AGENT_NAME,
            "input": input_data,
            "output": None,
            "status": "error",
            "message": str(exc),
        }
