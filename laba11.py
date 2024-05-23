def a11():
    class Restaurant:
        def __init__(self, rn, ct):
            self.rn = rn
            self.ct = ct

        def describe_restaurant(self):
            print("Restaurant name: ", self.rn)
            print("Cuisine type: ", self.ct)

        def open_restaurant(self):
            print("Restaurant otkrit")

    nRe = Restaurant("LALALA", "Italian")

    print("Restaurant name:", nRe.rn)
    print("Cuisine type:", nRe.ct)

    nRe.describe_restaurant()
    nRe.open_restaurant()
def bc11():
    class Restaurant:
        def __init__(self, rn, ct):
            self.rn = rn
            self.ct = ct
            self.r = 0

        def describe_restaurant(self):
            print("Restaurant name: ", self.rn)
            print("Cuisine type: ", self.ct)
            print("Rating: ", self.r)

        def open_restaurant(self):
            print("Restaurant otkrit")

        def update_rating(self, nr):
            self.r = nr

    Re1 = Restaurant("Vai", "Japanese")
    Re2 = Restaurant("Nam", "Italian")
    Re3 = Restaurant("Pizza", "Mexican")
    Re1.describe_restaurant()
    Re2.describe_restaurant()
    Re3.describe_restaurant()
    Re1.update_rating(4)
    Re1.describe_restaurant()