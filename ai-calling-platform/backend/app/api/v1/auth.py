from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db import get_db
from app.models.tenant import User
from app.utils.security import verify_password, create_jwt

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(email: str, password: str, db: Session = Depends(get_db)):
	stmt = select(User).where(User.email == email)
	user = db.execute(stmt).scalars().first()
	if not user or not verify_password(password, user.password_hash):
		raise HTTPException(status_code=401, detail="Invalid credentials")
	return {"access_token": create_jwt(sub=str(user.id), tenant_id=user.tenant_id), "token_type": "bearer"}