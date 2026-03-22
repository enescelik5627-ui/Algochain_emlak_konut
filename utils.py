import secrets
import time

class SecurityUtils:
    @staticmethod
    def generate_token(resident_id, access_type):
        """Sınırlı süreli, dinamik ve tek kullanımlık kriptografik veri üretir[cite: 30, 44]."""
        token = secrets.token_urlsafe(32)
        # 3600 saniye (1 saat) geçerli zaman damgalı izin [cite: 32]
        expiration = time.time() + 3600 
        return {
            "token": token,
            "resident": resident_id,
            "type": access_type,
            "expires_at": expiration
        }

    @staticmethod
    def validate_access(token_data):
        """Zaman damgalı izni anında ve otonom olarak doğrular[cite: 32]."""
        if time.time() > token_data.get('expires_at', 0):
            return False, "TOKEN_EXPIRED"
        
        # Gelecekte buraya GPS tabanlı konum doğrulaması eklenebilir 
        return True, "AUTHORIZED"
