import tensorflow as tf

b=tf.constant([[10,11],[20,21],[30,31]])
c=tf.slice(b,[1,0],[2,2])
d=tf.slice(b,[1,0],[1,2])
print(b)
print(c)
print(d)