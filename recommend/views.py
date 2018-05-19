from django.shortcuts import render

from recommend.models import Recommend

import random
import numpy as np
# Create your views here.


class Reocmmends():

    def __init__(self, article_id):
        self.article_id = int(article_id)
        self.count = Recommend.objects.latest('id').id
        self.article_str = Recommend.objects.get(article_id=self.article_id).all_be_like
        self.article = self.or_len(self.article_str)

    def recommend(self):
        list1 = []
        count = 0
        while len(list1) < 2:
            count += 1
            num = random.randint(1, self.count)
            temp1 = Recommend.objects.get(id=num).all_be_like
            temp_list = self.or_len(temp1)
            if num != self.article_id and self.article is not False and temp_list is not False\
                    and self.compare(self.article, temp_list) and num not in list1:
                n = Recommend.objects.get(id=num).article_id
                list1.append(n)
            if count > 10:
                break
        return list1

    @classmethod
    def compare(cls, article, temp):
        max_num = max(max(temp), max(article))
        article_zero = cls.array_to_zero(article, max_num)
        temp_zero = cls.array_to_zero(temp, max_num)
        x = np.array(article_zero)
        y = np.array(temp_zero)
        Lx = np.sqrt(x.dot(x))
        Ly = np.sqrt(y.dot(y))
        cos_angle = x.dot(y)/(Lx*Ly)
        return True if cos_angle > 0.5 else False

    @staticmethod
    def array_to_zero(array, max_num):
        zero = [0] * max_num
        for i in array:
            zero[i-1] = 1
        return zero

    @staticmethod
    def or_len(array_str):
        if len(array_str) == 1:
            temp = [int(i) for i in array_str]
        elif len(array_str) == 0:
            temp = False
        else:
            temp = [int(i) for i in array_str.split(',')]
        return temp

