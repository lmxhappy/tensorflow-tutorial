#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf


# #### 1. 定义队列及其操作。

# In[2]:


queue = tf.FIFOQueue(100,"float")
enqueue_op = queue.enqueue([tf.random_normal([1])])
ops = [enqueue_op] * 5
qr = tf.train.QueueRunner(queue, ops)
tf.train.add_queue_runner(qr)
out_tensor = queue.dequeue()


# #### 2. 启动线程。

# In[3]:


with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for _ in range(3):
        # print( sess.run(out_tensor)[0])
        print(sess.run([out_tensor, queue.size()]))
    coord.request_stop()
    coord.join(threads)

