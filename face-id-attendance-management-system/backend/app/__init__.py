# app/__init__.py

from app.routes import auth_routes, user_routes, attendance_routes, admin_routes

__all__ = [
    "auth_routes",
    "user_routes",
    "attendance_routes",
    "admin_routes"
]
