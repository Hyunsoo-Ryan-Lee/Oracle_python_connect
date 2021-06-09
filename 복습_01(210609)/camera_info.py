class Camera:

    def __init__(self, brand, model, price, format):
        self.brand = brand
        self.model = model
        self.price = price
        self.setFormat(format)

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price

    def getFormat(self):
        return self.format

    def setBrand(self,n_brand):
        self.brand = n_brand

    def setModel(self,n_model):
        self.model = n_model

    def setPrice(self, n_price):
        self.price = n_price

    def setFormat(self, n_format):
        if n_format == 135 or n_format == 120:
            self.format = n_format
        else:
            self.format = "해당 없음"

