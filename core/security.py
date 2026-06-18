import jwt
from datetime import UTC, datetime, timedelta
from core.config import settings

def create_access_token(
        username: str
    ) -> str:
        now = datetime.now(UTC)
        
        payload = {
            "sub": username,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=60)).timestamp())
        }
        
        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=["HS256"]
        )
        
def verify_access_token(
    token: str
) -> str:
    payload = jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=["HS256"]
    )
    
    username = payload.get("sub")
    if not username:
        raise ValueError("Invalid token")
    
    return username
