#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
模块功能描述：

@author Liu Mingxing
@date 2019/11/19
'''
import tensorflow as tf
# with tf.variable_scope("foo"):
#     # 创建新变量
#     v = tf.get_variable("v", [1], initializer=tf.constant_initializer(1.0))
#
# # with tf.variable_scope("foo"):
# # v = tf.get_variable("v", [1])
#
# with tf.variable_scope("foo", reuse=True):
#     # 访问已创建变量
#     v1 = tf.get_variable("v", [1])
# print(v == v1)
# print(v.name)
# print(v1.name)
# # with tf.variable_scope("bar", reuse=True):
# # v = tf.get_variable("v", [1])
#
# print('---------------------------------')
#
# with tf.name_scope("foo"):
#     with tf.variable_scope("var_scope"):
#         v = tf.get_variable("var", [1])
#
# with tf.name_scope("bar"):
#     with tf.variable_scope("var_scope", reuse=True):
#         v1 = tf.get_variable("var", [1])
#
# assert v1 == v
# print(v.name)   # var_scope/var:0
# print(v1.name)  # var_scope/var:0


# with tf.compat.v1.variable_scope("foo"):
#     with tf.compat.v1.variable_scope("bar"):
#         v = tf.compat.v1.get_variable("v", [1])
#         assert v.name == "foo/bar/v:0"



# with tf.name_scope('cltdevelop'):
#     var_1 = tf.Variable(initial_value=[0], name='var_1')
#     var_2 = tf.Variable(initial_value=[0], name='var_1')
#     var_3 = tf.Variable(initial_value=[0], name='var_1')
#
# print(var_1.name)
# print(var_2.name)
# print(var_3.name)


