from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app import crud, schemas
from app.auth import create_access_token, verify_password, get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ------------------- Existing Code (Unchanged) -------------------

@router.post("/register", response_model=schemas.UserOut)
def register_user(
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing = crud.get_user_by_email(db, email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, full_name, email, password)
    crud.log_action(db, "user_register", f"Registered user: {email}")
    return user


@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    crud.log_action(db, "user_login", f"{user.email} logged in")
    return {"access_token": token, "token_type": "bearer"}

# ------------------- ✨ New Admin Login Route (Added) -------------------

@router.post("/admin/login")
def admin_login(
    username: str = Form(...),
    password: str = Form(...)
):
    """
    Separate route for Admin Login.
    Uses static credentials or can be later connected to a DB table.
    """
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid admin credentials")

    # ✅ Generate JWT token for admin
    token = create_access_token({"sub": username, "role": "admin"})

    return {"access_token": token, "token_type": "bearer", "role": "admin"}
