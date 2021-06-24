import tensorflow as tf
a=tf.constant([[1,2],[3,4]])
b=tf.constant([[5,6],[7,8]])
c=tf.matmul(a,b)
print(c)
d=tf.constant([[1,2,3]])
e=tf.constant([[10],[20],[30]])
print(tf.add(d,e))
print(tf.subtract(d,e))