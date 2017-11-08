import re

class Convert:
    @staticmethod
    def get_number(text):
        text = re.sub(r'^[a-zA-Z\s]*', "", text)
        match_obj = re.match(r'^(\+?\-?)(\d+)(\.?\d*)(.*)', text)

        if match_obj:
            return match_obj.group(1) + match_obj.group(2) + match_obj.group(3)
        else:
            return 0

