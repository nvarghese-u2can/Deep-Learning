import tensorflow as tf

graph = tf.get_default_graph()
operations = graph.get_operations()
print(operations)

one = tf.constant(3, name='a')
two = tf.constant(5, name='b')
three = tf.constant(6, name='c')

print(three)
operations = graph.get_operations()
print(operations)

for op in operations:
    print(op.name)
