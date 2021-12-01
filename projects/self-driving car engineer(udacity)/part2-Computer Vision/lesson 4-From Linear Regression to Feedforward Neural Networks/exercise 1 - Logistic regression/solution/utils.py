import tensorflow as tf 


def check_softmax(func):
    logits = tf.constant([[0.5, 1.0, 2.0, 0.3, 4.0]])
    tf_soft = tf.nn.softmax(logits)
    soft = func(logits)
    l1_norm = tf.norm(tf_soft - soft, ord=1)
    assert l1_norm < 1e-5, 'Softmax calculation is wrong'
    print('Softmax implementation is correct!')


def check_ce(func):
    logits = tf.constant([[0.5, 1.0, 2.0, 0.3, 4.0]])
    scaled_logits = tf.nn.softmax(logits)
    one_hot = tf.constant([[0, 0, 0, 0, 1.0]])
    tf_ce = tf.nn.softmax_cross_entropy_with_logits(one_hot, logits)
    ce = func(scaled_logits, one_hot)
    l1_norm = tf.norm(tf_ce - ce, ord=1)
    assert l1_norm < 1e-5, 'CE calculation is wrong'
    print('CE implementation is correct!')


def check_model(func):
    # only check the output size here
    X = tf.random.uniform([28, 28, 3])
    num_inputs = 28*28*3
    num_outputs = 10
    W = tf.Variable(tf.random.normal(shape=(num_inputs, num_outputs),
                                    mean=0, stddev=0.01))
    b = tf.Variable(tf.zeros(num_outputs))
    out = func(X, W, b)
    assert out.shape == (1, 10), 'Model is wrong!'
    print('Model implementation is correct!')


def check_acc(func):
    y_hat = tf.constant([[0.8, 0.2, 0.5, 0.2, 5.0], [0.8, 0.2, 0.5, 0.2, 5.0]]) 
    y = tf.constant([4, 1])
    acc = func(y_hat, y)
    assert acc == tf.cast(tf.constant(0.5), dtype=acc.dtype), 'Accuracy calculation is wrong!'
    print('Accuracy implementation is correct!')    