class Employee:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender
        self.major = new_major
        self.id = new_id

    def get_gender(self):
        return self.__gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('====請傳入"M"或"F"====')

    def borrow_resources(self):
        pass

    def check_auth(self):
        pass


class Student(Employee):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def join_class(self):
        pass

    def quit_class(self):
        pass