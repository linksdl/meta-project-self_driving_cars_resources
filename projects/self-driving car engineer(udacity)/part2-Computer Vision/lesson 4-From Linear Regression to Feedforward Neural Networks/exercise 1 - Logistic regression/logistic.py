import tensorflow as tf


def softmax(logits):
    """
    softmax implementation
    args:
    - logits [tensor]: 1xN logits tensor
    returns:
    - soft_logits [tensor]: softmax of logits
    """
    # IMPLEMENT THIS FUNCTION
    exp = tf.exp(logits)
    softmax = exp / tf.math.reduce_sum(exp, 1, keepdims=True)
    return softmax


def cross_entropy(scaled_logits, one_hot):
    """
    Cross entropy loss implementation
    args:
    - scaled_logits [tensor]: NxC tensor where N batch size / C number of classes
    - one_hot [tensor]: one hot tensor
    returns:
    - loss [tensor]: cross entropy 
    """
    # IMPLEMENT THIS FUNCTION
    masked_logits = tf.boolean_mask(scaled_logits, one_hot) 
    return -tf.math.log(masked_logits)


def model(X, W, b):
    """
    logistic regression model
    args:
    - X [tensor]: input HxWx3
    - W [tensor]: weights
    - b [tensor]: bias
    returns:
    - output [tensor]
    """
    # IMPLEMENT THIS FUNCTION
    
    X = tf.reshape(X, (-1, W.shape[0]))
    L = softmax(tf.matmul(X, W) + b)
    return L

def accuracy(y_hat, Y):
    """
    calculate accuracy
    args:
    - y_hat [tensor]: NxC tensor of models predictions
    - y [tensor]: N tensor of ground truth classes
    returns:
    - acc [tensor]: accuracy
    """
    # IMPLEMENT THIS FUNCTION
    # calculate argmax
    argmax = tf.cast(tf.argmax(y_hat, axis=1), Y.dtype)

    # calculate acc
    acc = tf.math.reduce_sum(tf.cast(argmax == Y, tf.int32)) / Y.shape[0]
    return acc

