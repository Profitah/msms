class Student:
    def __init__(self, class_name, name, grade, student_number, sex, address, phone_number, year): # self, class_name, name, grade, student_number,
                                                                                                    # sex, address, phone_number, year을 매개 변수로 지정
        self.class_name = class_name
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year

    # 출력문
    def introduce_class_name(self):                            
        print('객체 명을 입력하시오 (단, 영문으로) : %s' % self.class_name)

    def introduce_name(self):
        print('이름을 입력하시오 (단, 한글로) : 이름은 %s 이다.' % self.name)

    def introduce_grade(self):
        print('학년을 입력하시오 (단, 숫자로):  학년은 %s 이다.' % self.grade)
       
    def introduce_student_number(self):
        print('학번을 입력하시오 (단, 숫자로): 학번은 %s 이다.' % self.student_number)

    def introduce_sex(self):
        print('성별을 입력하시오:  %s 이다.' % self.sex)

    def introduce_address(self):
        print('주소를 입력하시오 (~시까지만): 주소는 %s 이다.' % self.address)
       
    def introduce_phone_number(self):
        print('전화번호를 입력하십시오(모를때는 모른다고 입력) : %s 이다.' % self.phone_number)

    def introduce_year(self):
        print('멋사 몇 년 차인가요? (단 숫자로): 멋사 %s 년차' % self.year)

#input함수를 이용해 값을 입력받음
while True:
    class_name = input('객체 명을 입력하시오. (단, 영문으로): ')
    if class_name == '종료':
        break
    name = input('이름을 입력하시오 (단, 한글로) ')
    grade = int(input('학년을 입력하시오 (단, 숫자로) '))
    student_number = int(input('학번을 입력하시오 (단, 숫자로) '))
    sex = input('성별을 입력하시오 (모를때는 모른다고 입력) ')
    address = input('주소를 입력하시오 (~시까지만) ')
    phone_number = input('전화번호를 입력하십시오(모를때는 모른다고 입력) ')
    year = int(input('멋사 몇 년 차인가요? (단 숫자로) '))
    # phone_number에 대한 if 조건문
    if phone_number == '모른다':
        phone_number = 'None'
    # sex에 대한 if 조건문
    if sex == '모른다':
        sex = 'None'
   
    # 입력받은 값을 저장    
    student = Student(class_name, name, grade, student_number, sex, address, phone_number, year)
    student.introduce_class_name()
    student.introduce_name()
    student.introduce_grade()
    student.introduce_student_number()
    student.introduce_sex()
    student.introduce_address()
    student.introduce_phone_number()
    student.introduce_year()
    # year에 관한 if 조건문
    if year == 1:
         print("와 아기사자다!")
    else:
        print("와 운영진이다!")
    print("")