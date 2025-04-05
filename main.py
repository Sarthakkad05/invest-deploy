from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from authentication.routes import router
from chatbot.bot import  bot_router
from screener.stock_search import stock_search_router
from stock_comparison.comparison import comparison_router
from news_service.news_service import router as news_router

app = FastAPI()

# origins = [
#     "https://www,investiq.com",
#     "https://investiq-frontend-2zg9xqrv8-sarthakkad2005-gmailcoms-projects.vercel.app",
#     "https://investiq-frontend-846ovx94x-sarthakkad2005-gmailcoms-projects.vercel.app",
#     "https://iinvest-iq.netlify.app"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(router)
app.include_router(bot_router)
app.include_router(stock_search_router)
app.include_router(comparison_router)
app.include_router(news_router)




@app.get("/")
@app.head("/")
def read_root():
    return {"message": "Backend is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
