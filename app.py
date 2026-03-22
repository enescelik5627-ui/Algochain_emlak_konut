from data import ledger
from utils import SecurityUtils
from model import AnalyticalEngine

def process_gate_entry(qr_payload):
    """IoT terminali üzerinden gelen giriş isteğini yönetir."""
    print("\n[SİSTEM] Kriptografik doğrulama başlatıldı...")
    
    # 1. Kriptografik Doğrulama [cite: 28]
    is_valid, msg = SecurityUtils.validate_access(qr_payload)
    
    # 2. Blockchain Kaydı [cite: 38]
    status = "AUTHORIZED" if is_valid else "UNAUTHORIZED"
    tx_hash = ledger.record_access(qr_payload['resident'], qr_payload['type'], status)
    
    print(f"[ONAY] Durum: {status}")
    print(f"[BLOCKCHAIN] İşlem Hash: {tx_hash}")
    return is_valid

if __name__ == "__main__":
    # Test Senaryosu: Bir kurye girişi
    engine = AnalyticalEngine(ledger)
    
    # Sakin uygulama üzerinden kurye kodu üretir [cite: 30]
    courier_qr = SecurityUtils.generate_token("Daire_42", "COURIER")
    
    # Giriş işlemi
    process_gate_entry(courier_qr)
    
    # Yönetici Paneli Özeti [cite: 48]
    report = engine.analyze_risk()
    print(f"\n--- YÖNETİCİ PANELİ ÖZETİ ---")
    print(f"Genel Risk Puanı: {report['score']} ({report['status']})")
    print(f"Toplam Blockchain Kaydı: {report['total_entries']}")
