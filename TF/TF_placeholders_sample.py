import tensorflow as tf

ph = tf.placeholder(tf.int32)
result = ph**2
dictionary = {ph: [[1, 2, 3], [4, 5, 6]]}
with tf.Session() as sess:
    #data = sess.run(result, feed_dict={ph: [3, 4, 5]})
    data = sess.run(result, feed_dict=dictionary)
    print(data)



print('\n')

# with tf.Session as sess1:
#     data = sess1.run(result, feed_dict=dictionary)
#     print(data)

