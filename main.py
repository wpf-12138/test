import tensorflow as tf
import numpy as np

# 添加层
def add_layer(inputs,in_size,out_size,activation_function=None)
    # add one more layer and return the output of this year
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    bias = tf.Variable(tf.zeros([1,out_size]))