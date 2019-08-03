import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

batch_size = 100
n_batch = mnist.train.num_examples // batch_size

tf.reset_default_graph()

# image_num = 3000
# embedding = tf.Variable(tf.stack(mnist.test.images[:image_num]), trainable=False, name="embedding")

with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y = tf.placeholder(tf.float32, [None, 10], name='y-input')

# with tf.name_scope("reshape"):
#     image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
#     tf.summary.image("input", image_shaped_input, 10)

with tf.name_scope('layer'):
    with tf.name_scope('weight'):
        W = tf.Variable(tf.random_normal([784, 10]), name='w')
    with tf.name_scope('bias'):
        b = tf.Variable(tf.zeros([1, 10]), name='b')
    with tf.name_scope('Wx_plus_b'):
        Wx_plus_b = tf.matmul(x, W) + b
    with tf.name_scope('softmax'):
        prediction = tf.nn.softmax(Wx_plus_b)

#loss = tf.reduce_mean(tf.square(prediction - y))
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
        labels=y, logits=prediction))
    tf.summary.scalar("loss", loss)
optimizer = tf.train.GradientDescentOptimizer(0.2)
with tf.name_scope('train'):
    train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.name_scope('accuracy'):
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar("acc", accuracy)

merged = tf.summary.merge_all()

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(r'log/', sess.graph)
    for epoch in range(99):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            summary, _ = sess.run([merged,train], feed_dict={x: batch_xs, y: batch_ys})
        
        writer.add_summary(summary, epoch)
        acc = sess.run(accuracy, feed_dict={
                       x: mnist.test.images, y: mnist.test.labels})
        print('Iter' + str(epoch) + ', Testing Accuracy ' + str(acc))
