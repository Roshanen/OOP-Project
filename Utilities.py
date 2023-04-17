import hashlib

class IdGenerator:
    @staticmethod
    def generate_id(to_hash):
        id = hashlib.md5(str(to_hash).encode()).hexdigest()
        return id