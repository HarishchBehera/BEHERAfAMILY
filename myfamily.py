# +++++-----------------BEHERA FAMILY-------------------+++++

class BeheraFamily:
    def __init__(self, name, age, relationship):
        self.name = name
        self.age = age
        self.relationship = relationship

    def __str__(self):
        return f'{self.relationship}: {self.name}, Age: {self.age}'

class Family:
    def __init__(self):
        self.members = []

    def add_meb(self, name, age, relationship):
        new_member = BeheraFamily(name, age, relationship)
        self.members.append(new_member)

    def get_meb(self):
        return [str(member) for member in self.members]

    def get_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return str(member)
        return None



my_family = Family()
my_family.add_meb('Chandrakanti Behera', 42, 'Mother')
my_family.add_meb('Paramananda Behera', 51, 'Father')
my_family.add_meb('Harish Chandra Behera', 25, 'Son')
my_family.add_meb('Deepanjali Behera',28,'Daughter')

print("Family Members:")
for member in my_family.get_meb():
    print(member)

