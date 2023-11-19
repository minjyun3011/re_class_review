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
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        elif 75 <= self.age:
            return 500
        
    def info_csv(self):
        self.info_csv =  f"{self.full_name}, {self.age}, {self.entry_fee()}"
        return self.info_csv
    
    def info_tab(self):
        self.info_tab = f"{self.full_name}  {self.age}  {self.entry_fee()}"
        return self.info_tab
    
    def info_psv(self):
        self.info_psv = f"{self.full_name} | {self.age} | {self.entry_fee()}"
        return self.info_psv


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)
seiichi = Customer(first_name="Kato", family_name="Seiichi", age=86)

print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())
michelle.full_name() #bound method info_csv等のメソッドを出力するときにfull_nameメソッドを呼び出す必要がある
print(seiichi.full_name())


print(ken.age)  # 15 という値を出力
print(tom.age) # 57 という値を出力
print(ieyasu.age) # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力

print(michelle.entry_fee())

print(seiichi.entry_fee())

print(ken.info_tab())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_tab())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_tab())
print(michelle.info_tab())
print(seiichi.info_tab())


print(ken.info_psv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_psv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_psv())
print(michelle.info_psv())
print(seiichi.info_psv())
