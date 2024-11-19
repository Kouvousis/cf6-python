class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def main():
    st = Student("Bob", "M.")
    print("Firstname:", st.firstname)
    print("Lastname:", st.lastname)
    

if __name__ == "__main__":
    main()