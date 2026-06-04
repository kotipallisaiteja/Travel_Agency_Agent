from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.ai_agent import ask_gemini
from backend.data_loader import get_data
from backend.root_cause_engine import get_business_insights
from backend.recommendation_engine import generate_recommendations

df = get_data()

insights = get_business_insights(df)

recommendations = generate_recommendations(
    insights
)

insights_text = f"""
Total Revenue: {insights['total_revenue']:,.2f}

Total Profit: {insights['total_profit']:,.2f}

Average Occupancy:
{insights['avg_occupancy']:.2f}%

Average Delay:
{insights['avg_delay']:.2f} mins

Average Customer Rating:
{insights['avg_rating']:.2f}

Average Profit Margin:
{insights['avg_profit_margin']:.2f}%
"""

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(data: ChatRequest):

    answer = ask_gemini(
        data.question,
        insights_text,
        recommendations
    )

    return {
        "answer": answer
    }
@app.get("/")
def home():
    return {"message": "BusinessInsight AI Running"}