import tensorflow as tf
a=tf.constant([[1.0,2],[3,4],[5,6]])
b=tf.constant([[10,11],[20,21],[30,31]])
c=tf.cast(a,tf.int32)
print(tf.add(c,b))