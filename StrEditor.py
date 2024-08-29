class String_Editting:
    def __init__(self, total_str, old_substr, new_substr):
        self.total_str_ = total_str
        self.old_substr_ = old_substr
        self.new_substr_ = new_substr
        self.new_str = total_str
        result = self.find()

        if result == False:
            print('your substr is not in total str')
        else:
            self.new_str = self.replace(result[0], result[1])

    def find(self):
        i = 0
        j = 0

        start = 0
        end = 0
        while i < len(self.total_str_):
            if self.total_str_[i] == self.old_substr_[j]:

                if j == 0:
                    start = i
                if j == len(self.old_substr_) - 1:
                    end = i
                    return start, end
                i += 1
                j += 1
            else:
                i += 1
                j = 0

        return False

    def replace(self, start, end):
        return self.total_str_[:start] + self.new_substr_ + self.total_str_[end + 1:]

    def get(self):
        return self.new_str


obj = String_Editting('I am Iman', 'Iman', 'Fazel')
print(obj.get())
