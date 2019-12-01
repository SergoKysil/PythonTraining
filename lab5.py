# class MyClass:
#     variable = "blah"
#
#     def function(self):
#         print("This message will be printed")
#
#
# myobjectx = MyClass()
#
# myobjectx.function()
# myobjecty = MyClass()
# myobjecty.function()
#
# myobjecty = MyClass()
#
# myobjecty.variable = "Yaric"
#
# print(myobjecty.variable)
# print(myobjectx.variable)


class Cup:
    color = ""
    size = 0.250
    value = 25.00
    def cost_of_cups(self):
        desc_str = "This cup of %s color, space %s milliliters is worth $%.2f." % (self.color, self.size, self.value)
        return desc_str


cup1 = Cup()
cup1.color = "blue"
cup1.size = 0.250
cup1.value = 3

cup2 = Cup()
cup2.color = "red"
cup2.size = 0.250
cup2.value = 2.50

cup3 = Cup()
cup3.color = "green"
cup3.size = 0.200
cup3.value = 5

print(cup1.cost_of_cups())
print(cup2.cost_of_cups())
print(cup3.cost_of_cups())
