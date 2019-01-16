# Up to tensorboard, then cnn&LSTM should be studied 

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.placeholder(tf.float32, [None, 10], name='y-input')

W = tf.Variable(tf.random_normal([784, 10]))
b = tf.Variable(tf.zeros([1, 10]))
Wx_plus_b = tf.matmul(x, W) + b
prediction = tf.nn.softmax(Wx_plus_b)

#loss = tf.reduce_mean(tf.square(prediction - y))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    labels=y, logits=prediction))
optimizer = tf.train.GradientDescentOptimizer(0.2)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(r'log/',sess.graph)
    for epoch in range(1):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train, feed_dict={x: batch_xs, y: batch_ys})

        acc = sess.run(accuracy, feed_dict={
                       x: mnist.test.images, y: mnist.test.labels})
        print('Iter' + str(epoch) + ', Testing Accuracy ' + str(acc))
