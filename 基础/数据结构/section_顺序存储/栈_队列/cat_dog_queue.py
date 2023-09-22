
""" 
实现一个队列，可以进入两种对象，要求可以分别对每种对象以及所有对象进行poll,is_empty操作
思路：
  -这是一个工程问题，而不是算法问题，给每个进入的猫或者狗加上一个时间戳
      在pollAll的时候，比较猫和狗头的时间戳
  -猫和狗是库给的，因此不能修改他们，把他们封装起来，加上时间戳
"""

class Dog:
    def __init__(self):
        pass
class Cat:
    def __init__(self):
        pass
class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count


class DogCatQueue:
    
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.count = 0
    
    def push(self, pet):
        if isinstance(pet, Dog):
            self.dog_queue.append(PetEnterQueue(pet, self.count))
            self.count += 1
        elif isinstance(pet, Cat):
            self.dog_queue.append(PetEnterQueue(pet, self.count))
            self.count += 1
        else:
            print('Wrong type!')

    def poll_all(self):
        if self.dog_queue and self.cat_queue:
            if self.dog_queue[0].count < self.cat_queue[0].count:
                return self.dog_queue.pop(0).pet
            else:
                return self.cat_queue.pop(0).pet
        elif self.dog_queue:
            return self.dog_queue.pop(0).pet
        elif self.cat_queue:
            return self.cat_queue.pop(0).pet
        else:
            print('queue is empty')
    def dog_poll(self):
        if not self.dog_queue:
            print('empty')
            raise Exception
        return self.dog_queue.pop(0).pet
    def cat_poll(self):
        if not self.cat_queue:
            print('empty')
            raise Exception
        return self.cat_queue.pop(0).pet

    def is_empty(self):
        if not self.dog_queue and not self.cat_queue:
            return True
        else:
            return False
    def is_dog_empty(self):
        if not self.dog_queue:
            return True
        else:
            return False
    def is_cat_empty(self):
        if not self.cat_queue:
            return True
        else:
            return False