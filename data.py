```python
import pandas as pd
import random
import time

def generate_data(n=100):
    users = ["Resident", "Guest", "Courier"]
    locations = ["Gate A", "Gate B", "Parking", "Lobby"]
    
    data = []
    
    for _ in range(n):
        user = random.choice(users)
        location = random.choice(locations)
        
        qr_valid = random.choice([True, False])
        attempt_delay = random.randint(0, 60)  # saniye
        
        # risk hesaplama (basit model)
        if qr_valid and attempt_delay < 20:
            risk = random.randint(1, 30)
            status = "Approved"
        else:
            risk = random.randint(60, 100)
            status = "Denied"
        
        data.append({
            "user_type": user,
            "location": location,
            "qr_valid": qr_valid,
            "scan_delay_sec": attempt_delay,
            "risk_score": risk,
            "status": status,
            "timestamp": int(time.time()) - random.randint(0, 10000)
        })
    
    return pd.DataFrame(data)
```
