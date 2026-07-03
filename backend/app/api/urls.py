import random
import string
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.url import URL
from app.schemas.url import URLCreate, URLResponse 
from fastapi.responses import RedirectResponse
from app.auth import get_current_user

router = APIRouter(prefix="/urls", tags=["urls"])

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@router.post("/shorten", response_model=URLResponse)
def shorten_url(url_create: URLCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    short_code = generate_short_code()

    new_url = URL(original_url=url_create.original_url, short_code=short_code, owner_email=current_user["email"])

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url

@router.get("/my", response_model=List[URLResponse])
def get_my_urls(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    urls = db.query(URL).filter(URL.owner_email == current_user["email"]).all()
    return urls

@router.delete("/{url_id}")
def delete_url(url_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    url = db.query(URL).filter(URL.id == url_id).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    if url.owner_email != current_user["email"]:
        raise HTTPException(status_code=403, detail="Not your URL")

    db.delete(url)
    db.commit()

    return {"message": "URL deleted successfully"}

@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url = url.original_url)
    