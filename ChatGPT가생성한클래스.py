# Person 클래스 정의
class Person:
    def __init__(self, person_id, name):
        # Person 클래스의 생성자. id와 name을 초기화함.
        self.id = person_id
        self.name = name

    def printInfo(self):
        # Person 객체의 정보를 출력하는 메서드
        print(f"ID: {self.id}, Name: {self.name}")


# Manager 클래스 정의 (Person 상속)
class Manager(Person):
    def __init__(self, person_id, name, title):
        # Manager 클래스의 생성자. Person 클래스의 생성자를 호출하고, title을 추가로 초기화함.
        super().__init__(person_id, name)
        self.title = title

    def printInfo(self):
        # Manager 객체의 정보를 출력하는 메서드. Person의 정보를 출력한 뒤 title을 추가로 출력함.
        super().printInfo()
        print(f"Title: {self.title}")


# Employee 클래스 정의 (Person 상속)
class Employee(Person):
    def __init__(self, person_id, name, skill):
        # Employee 클래스의 생성자. Person 클래스의 생성자를 호출하고, skill을 추가로 초기화함.
        super().__init__(person_id, name)
        self.skill = skill

    def printInfo(self):
        # Employee 객체의 정보를 출력하는 메서드. Person의 정보를 출력한 뒤 skill을 추가로 출력함.
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
if __name__ == "__main__":
    # 테스트 1: Person 객체 생성 및 출력
    # Person 클래스의 객체를 생성하고 정보를 출력.
    p1 = Person(1, "Alice")
    p1.printInfo()  # ID와 Name 출력
    print()  # 줄바꿈

    # 테스트 2: Manager 객체 생성 및 출력
    # Manager 클래스의 객체를 생성하고 정보를 출력.
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()  # ID, Name, Title 출력
    print()

    # 테스트 3: Employee 객체 생성 및 출력
    # Employee 클래스의 객체를 생성하고 정보를 출력.
    e1 = Employee(3, "Charlie", "Python Developer")
    e1.printInfo()  # ID, Name, Skill 출력
    print()

    # 테스트 4: Manager의 title 변경 및 확인
    # Manager 객체의 title 속성을 변경한 뒤 다시 출력.
    m1.title = "Senior Project Manager"  # Title 변경
    m1.printInfo()  # 변경된 Title 확인
    print()

    # 테스트 5: Employee의 skill 변경 및 확인
    # Employee 객체의 skill 속성을 변경한 뒤 다시 출력.
    e1.skill = "Java Developer"  # Skill 변경
    e1.printInfo()  # 변경된 Skill 확인
    print()

    # 테스트 6: 여러 Manager 객체 생성 및 출력
    # 두 개의 Manager 객체를 추가로 생성하고 정보를 출력.
    m2 = Manager(4, "Diana", "HR Manager")
    m3 = Manager(5, "Edward", "Sales Manager")
    m2.printInfo()  # 첫 번째 Manager 정보 출력
    print()
    m3.printInfo()  # 두 번째 Manager 정보 출력
    print()

    # 테스트 7: 여러 Employee 객체 생성 및 출력
    # 두 개의 Employee 객체를 추가로 생성하고 정보를 출력.
    e2 = Employee(6, "Fiona", "Data Analyst")
    e3 = Employee(7, "George", "Network Engineer")
    e2.printInfo()  # 첫 번째 Employee 정보 출력
    print()
    e3.printInfo()  # 두 번째 Employee 정보 출력
    print()

    # 테스트 8: Person, Manager, Employee 혼합 출력
    # 다양한 객체(Person, Manager, Employee)를 하나의 리스트에 담아 순차적으로 출력.
    persons = [p1, m1, e1, m2, e3]
    for person in persons:
        person.printInfo()  # 각 객체의 정보를 출력
        print()

    # 테스트 9: Manager 객체 리스트 관리
    # 여러 Manager 객체를 리스트로 관리하며 각각의 정보를 출력.
    managers = [m1, m2, m3]
    for manager in managers:
        print(f"Manager {manager.name} - Title: {manager.title}")

    # 테스트 10: Employee 객체 리스트 관리
    # 여러 Employee 객체를 리스트로 관리하며 각각의 정보를 출력.
    employees = [e1, e2, e3]
    for employee in employees:
        print(f"Employee {employee.name} - Skill: {employee.skill}")
