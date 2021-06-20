import tensorflow as tf

one = tf.constant(1)
zero = tf.constant(0)

var1 = tf.Variable(2)

update = tf.add(one, zero)
var1 = tf.assign(var1, update)

var_init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(var_init)

print(sess.run(var1))

print('\n')
for x in range(5):
    var1 = tf.assign(var1, x)
    print(sess.run(var1))

print('\n')
hello = tf.constant('Hello')
world = tf.constant('TensorWorld')
hello_world = tf.add(hello, world)

print(sess.run(hello_world))
sess.close()