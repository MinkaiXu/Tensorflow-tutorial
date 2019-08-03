import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

keep_prob = tf.placeholder(dtype=tf.float32)

lr = tf.Variable(0.001, dtype=tf.float32)

W1 = tf.Variable(tf.truncated_normal([784, 512], stddev=0.1))
b1 = tf.Variable(tf.zeros([1, 512]) + 0.1)
L1_Wx_plus_b = tf.matmul(x, W1) + b1
L1 = tf.nn.relu(L1_Wx_plus_b)
L1_drop = tf.nn.dropout(L1, keep_prob)

W2 = tf.Variable(tf.truncated_normal([512, 10], stddev=0.1))
b2 = tf.Variable(tf.zeros([1, 10]) + 0.1)
L2_Wx_plus_b = tf.matmul(L1, W2) + b2

prediction = tf.nn.softmax(L2_Wx_plus_b)

# loss = tf.reduce_mean(tf.square(prediction - y))
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    labels=y, logits=prediction))
optimizer = tf.train.AdamOptimizer(lr)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        sess.run(tf.assign(lr, 0.001 * (0.95 ** epoch)))
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train, feed_dict={x: batch_xs,
                                       y: batch_ys,
                                       keep_prob: .65})

        test_acc = sess.run(accuracy, feed_dict={
            x: mnist.test.images,
            y: mnist.test.labels,
            keep_prob: 1.})
        train_acc = sess.run(accuracy, feed_dict={
            x: mnist.train.images,
            y: mnist.train.labels,
            keep_prob: 1.})

        print('Iter' + str(epoch) + ', Testing Accuracy ' + str(test_acc) +
              ', Training Accuracy ' + str(train_acc))
