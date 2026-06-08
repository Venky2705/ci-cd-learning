from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD Learning Project"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/company/{company_name}")
def get_company(company_name: str):
    return {
        "company": company_name,
        "industry": "Technology",
        "employees": 1000,
        "website": f"www.{company_name.lower()}.com"
    }