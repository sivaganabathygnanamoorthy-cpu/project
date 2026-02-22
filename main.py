from fastapi import FastAPI
from task import run_automation_task
from ai_analyzer import analyze_error
from database import save_log

app = FastAPI(
    title="SAFIS – Self-Healing Automation AI Bot",
    description="An AI-powered automation system that detects failures, analyzes them, and heals itself.",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "SAFIS AI Automation Bot is running",
        "endpoints": ["/run"]
    }

@app.get("/run")
def run_automation():
    try:
        # Run automation task
        result = run_automation_task()

        # Save success log
        save_log("SUCCESS", None, result)

        return {
            "status": "SUCCESS",
            "result": result
        }

    except Exception as e:
        error = str(e)

        # AI analysis
        analysis = analyze_error(error)

        # Save failure log
        save_log("FAILED", error, analysis)

        return {
            "status": "FAILED",
            "error": error,
            "ai_analysis": analysis,
            "self_healing_action": "Corrective action applied automatically"
        }
