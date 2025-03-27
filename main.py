from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from authentication.routes import router
from chatbot.bot import  bot_router
from screener.stock_search import stock_search_router
from stock_comparison.comparison import comparison_router
from news_service.news_service import router as news_router

app = FastAPI()

app.include_router(router)
app.include_router(bot_router)
app.include_router(stock_search_router)
app.include_router(comparison_router)
app.include_router(news_router)

origins = [
    "https://investiq-frontend-2zg9xqrv8-sarthakkad2005-gmailcoms-projects.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 👈 Add your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
@app.head("/")
def read_root():
    return {"message": "Backend is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
