class AnalyticalEngine:
    def __init__(self, ledger_instance):
        self.ledger = ledger_instance

    def analyze_risk(self):
        """Davranış analitiği ile Genel Risk Puanı hesaplar[cite: 57, 74]."""
        logs = self.ledger.get_all_logs()
        risk_score = 12  # Düşük risk başlangıç puanı [cite: 58]
        
        # Aynı QR kod ile mükerrer başarısız deneme analizi [cite: 65]
        failed_attempts = [l for l in logs if l['status'] == "UNAUTHORIZED"]
        
        if len(failed_attempts) >= 3:
            risk_score += 45  # Kritik risk artışı
            
        return {
            "score": min(risk_score, 100),
            "status": "CRITICAL" if risk_score > 50 else "LOW",
            "total_entries": len(logs)
        }

    def get_realtime_density(self):
        """Gerçek zamanlı yoğunluk tahmini verilerini döner[cite: 49, 50]."""
        # Mock data: Gerçek sistemde blok bazlı giriş sayısından çekilir
        return {"A_Block": 10, "B_Block": 25, "C_Block": 15}
