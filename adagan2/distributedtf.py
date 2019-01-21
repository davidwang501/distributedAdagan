'''
Created on Jul 18, 2017

@author: david
'''
import tensorflow as tf


cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})

x = tf.constant(2)


'with tf.device("/job:local/task:1"):
 with tf.Session("grpc://localhost:2223") as sess:
    print "compute y2 on task 1"
    y2 = x - 66
    

'with tf.device("/job:local/task:0"):
with tf.Session("grpc://localhost:2222") as sess:    
    print "compute y1 and y on task 0"
    y1 = x + 300
    y = y1 + y2
  


with tf.Session("grpc://localhost:2222") as sess:
    print "master"
    result = sess.run(y)
    print(result)
    
    