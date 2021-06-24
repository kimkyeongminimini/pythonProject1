import tensorflow as tf
a=tf.constant([[1,2,3],[4,5,6]])
b=tf.constant([10,11][20,21],[30,31])

#print(tf.add(a,b))

c=tf.reshape(a,[3,2])
print(a)
print(b)
print(c)
print(tf.add(b,c))