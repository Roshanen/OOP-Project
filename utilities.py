import hashlib
import re

class IdGenerator:
    @staticmethod
    def generate_id(to_hash):
        id = hashlib.md5(str(to_hash).encode()).hexdigest()
        return id


class GameDBSupport:
    @staticmethod
    def get_sys_req(s):
        result = {}
        splitted = re.split(": |\n", s)
        for i in range(0,len(splitted) - 1,2):
            result[splitted[i]] = splitted[i+1]

        return result