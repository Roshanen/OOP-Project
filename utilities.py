import hashlib


class IdGenerator:
    @staticmethod
    def generate_id(to_hash):
        id = hashlib.md5(str(to_hash).encode()).hexdigest()
        return id

import re
class GameDBSupport:
    @staticmethod
    def get_sys_req(s):
        result = {}
        splitted = re.split(": |\n", s)
        for i in range(0,len(splitted) - 1,2):
            print(i)
            result[splitted[i]] = splitted[i+1]

        return result

s = """Processor: Intel Core i5
Memory: 2 GB RAM
Graphics: NVIDIA GeForce GTX 550/equivalent or higher
DirectX: Version 10
Storage: 738 MB available space"""
print(GameDBSupport.get_sys_req(s))