class String:

    @staticmethod
    def left(s, amount):
        return s[:amount]

    @staticmethod
    def right(s, amount):
        return s[-amount:]

    @staticmethod
    def mid(s, offset, amount):
        return s[offset:offset+amount]
