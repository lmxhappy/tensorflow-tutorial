#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
模块功能描述：

@author Liu Mingxing
@date 2019/11/19
'''
import tensorflow as tf

with tf.variable_scope('cltdevelop'):
    var2_1 = tf.Variable(initial_value=[0], name='var_1')
    var2_2 = tf.Variable(initial_value=[0], name='var_1')
    var2_3 = tf.Variable(initial_value=[0], name='var_1')

print(var2_1.name)
print(var2_2.name)
print(var2_3.name)
