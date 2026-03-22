import hashlib
import time
import json

class BlockchainEntry:
    def __init__(self, user_id, entry_type, status):
        self.timestamp = time.time()
        self.user_id = user_id
        self.entry_type = entry_type  # GUEST, COURIER, SERVICE
        self.status = status
        self.hash = self._generate_hash()

    def _generate_hash(self):
        """Her giriş denemesini zincire hash'lenmiş bir kayıt olarak işler."""
        block_string = json.dumps({
            "ts": self.timestamp,
            "uid": self.user_id,
            "type": self.entry_type,
            "st": self.status
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class DecentralizedLedger:
    def __init__(self):
        self.__chain = []  # Private chain to prevent direct manipulation

    def record_access(self, user_id, entry_type, status="AUTHORIZED"):
        """Giriş hareketlerini otonom ve değiştirilemez olarak kaydeder."""
        new_entry = BlockchainEntry(user_id, entry_type, status)
        self.__chain.append(new_entry)
        return new_entry.hash

    def get_all_logs(self):
        """Şeffaf ve denetlenebilir kayıt listesi sunar."""
        return [vars(entry) for entry in self.__chain]

# Singleton instance
ledger = DecentralizedLedger()
