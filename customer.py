class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        self.full_name = f"{self.family_name} {self.first_name}"
        return self.full_name
        
    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif (20 <= self.age < 65):
            return 1500
        else:
            return 1200
        
    def info_csv(self):
        return f"{self.full_name()}, {self.age}, {self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)


print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力

print(ken.age)  # 15 という値を出力
print(tom.age) # 57 という値を出力
print(ieyasu.age) # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(ken.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
