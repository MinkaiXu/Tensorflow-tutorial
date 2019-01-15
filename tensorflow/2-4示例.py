import tensorflow as tf
import numpy as np

x_data = np.random.rand(1, 100)
y_data = x_data**3 + x_data**2 - 3*x_data + 5

b = tf.Variable(0.)
k1 = tf.Variable(0.)
k2 = tf.Variable(0.)
k3 = tf.Variable(0.)
y = k1*(x_data**3) + k2*(x_data**2) + k3*x_data + b

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.2)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(30000):
        sess.run(train)
        if step%100 == 0:
            print(sess.run(k1), sess.run(k2), sess.run(k3), sess.run(b))
