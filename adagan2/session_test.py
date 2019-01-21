'''
Created on Jul 20, 2017

@author: david
'''
import tensorflow as tf

x = tf.constant(2)
y1 = x + 300
y2 = x - 66
y = y1 + y2
y=y+1

with tf.Session() as sess:
    result1 = sess.run(y)
    result2 = sess.run(y)
    
    print(result2)