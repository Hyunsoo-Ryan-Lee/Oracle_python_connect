class Book:
    def __init__(self, title, author, price):
        # 멤버 변수 선언
        self.title = title
        self.author = author
        # self.price = price # 이 경우 100 미만 가격도 포함되므로 fail
        # self.setPrice(price) # 유효성 로직 처리 필수! 따라서 이미 구현되어 있는 method 호출
        # 이런식으로 init 선언해도 되네....
        self.price = 0 # 멤버 변수 선언, 유효한 값만 대입 예정

        if price > 100:  # 유효성 검증 코드
            self.price = price

    def getTitle(self):
        return self.title

    def setTitle(self, new_title):
        self.title = new_title

    def getAuthor(self):
        return self.author

    def setAuthor(self, new_author):
        self.author = new_author
    
    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        if new_price >= 100:
            self.price = new_price
        else:
            self.price = 0

