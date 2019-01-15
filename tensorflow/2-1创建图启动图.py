import tensorflow as tf

w1 = tf.constant([[3, 3]])
w2 = tf.constant([[3],
                  [3]])
w3 = tf.matmul(w1, w2)

with tf.Session() as sess:
    result = sess.run(w3)
    print(result)
