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


    @staticmethod
    def get_dictionary(text):
        result_str = re.sub(",", " ", text)
        adb_list = result_str.split("\\r\\n")

        # Prepare the list to convert to dictionary
        index = 0
        for adb_str in adb_list:
            adb_str = adb_str.strip()
            if re.search("=", adb_str):
                adb_str = re.sub("(\s*)=(\s*)", "':'", adb_str)
            elif re.search(":", adb_str):
                adb_str = re.sub("(\s*):(\s*)", "':'", adb_str)
            else:
                adb_str += "':'"
            adb_str = "'" + adb_str + "'"
            adb_list[index] = adb_str
            index += 1
        result_str = ", ".join(adb_list)
        result_str = "{" + result_str + "}"

        # Convert list to dictionary
        try:
            result_dict = ast.literal_eval(result_str)
            return result_dict
        except Exception:
            return None

