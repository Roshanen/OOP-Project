import hashlib

class IdGenerator:
    @staticmethod
    def generate_id(to_hash):
        id = hashlib.md5(to_hash.encode()).hexdigest()
        return id