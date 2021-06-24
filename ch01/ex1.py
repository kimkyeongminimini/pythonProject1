import tensorflow as tf

a=tf.eye(3)
print(a)
b=tf.constant([1,2,3,4,5,6,7,8,9,10])
print(tf.reduce_sum(b))
print(tf.reduce_max(b))
print(tf.reduce_min(b))
print(tf.reduce_mean(b))
print(b+5)