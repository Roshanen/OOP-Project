import hashlib
import re
from fuzzywuzzy import process


class IdGenerator:
    @staticmethod
    def generate_id(to_hash):
        id = hashlib.md5(str(to_hash).encode()).hexdigest()
        return id


class Search:
    @staticmethod
    def search_profile(user_holder, kwargs):
        # get id and name that user want to search
        found_user = []
        search_id = kwargs.get("search_id")
        search_name = kwargs.get("search_name")

        if search_id:  # if there is id to search
            return user_holder.get_user_by_id(search_id)

        elif search_name:  # if there is name to search
            # the extract return tuple -> (str,similarity)
            found_user_name = process.extract(search_name, user_holder.get_all_user_name())

            # keep the user that have similarity 55 percent or more
            found_user = [user_holder.get_user_by_name(user[0]) for user in found_user_name if user[1] >= 55]

        # if there are no id or name to search
        return found_user

    @staticmethod
    def search_product(product_catalog, search_name):
        if search_name != "":
            found_product_name = process.extract(search_name, product_catalog.get_all_products()["by_name"].keys())
            found_product = [product_catalog.get_product_by_name(product[0]) for product in found_product_name if
                             product[1] > 55]
            if found_product:
                return found_product
        return []


class GameDBSupport:
    @staticmethod
    def get_sys_req(s):
        result = {}
        splitted = re.split(": |\n", s)
        for i in range(0,len(splitted) - 1,2):
            result[splitted[i]] = splitted[i+1]

        return result


class VerifyProductInfo:
    @staticmethod
    def verify(info):
        try:
            info["price"] = float(info["price"])
        except ValueError:
            info["price"] = 0
        sys_req_dict = {}
        list_for_dict = info["system_req"].split(",")
        for i in range(0,len(list_for_dict),2):
            sys_req_dict[i] = list_for_dict[i+1]

        info["system_req"] = sys_req_dict
        try:
            info["discount"] = float(info["discount"])
        except ValueError:
            info["discount"] = 0
