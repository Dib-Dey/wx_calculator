import math

def press_num(self, event, num):
    if not self.cal_box.get():
        self.cal_box.set(num)
    else:
        self.cal_box.set(str(self.cal_box.get())+str(num))

def evaluate(self, event):
    try:
        self.cal_box.set(str(eval(self.cal_box.get())))
    except Exception:
        print("Error in evaluating")

def clear(self, event):
    self.cal_box.set('')

def num_by_rev(self,event):
    try:
        _value = str('1')+str('/')+str(float(str(self.cal_box.get())))
        self.cal_box.set(str(eval(_value)))
    except Exception:
        print("Error in evaluating")

def square_root(self, event):
    self.cal_box.set(str(math.sqrt(float(self.cal_box.get()))))

def num_power(self, event):
    self.cal_box.set(str(self.cal_box.get()) + str('**'))