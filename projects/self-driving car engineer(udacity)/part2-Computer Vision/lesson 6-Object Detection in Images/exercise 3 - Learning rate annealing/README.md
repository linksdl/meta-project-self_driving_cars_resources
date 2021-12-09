# Exercise 3 - Learning rate annealing 

## Objective

In this exercise, you have to implement two different learning rate annealing (decay)
strategies: step wise annealing and exponential annealing. 

## Details

To do so, you will have to leverage Keras `callbacks`. Callbacks performs various action
at different stages of training. For example, Keras uses a callback to save the models weights at 
the end of each training epoch.

You can either use pre-implemented schedulers (see Tips) or implement a scheduler yourself 
using your own custom decay function, as shown below:

```
def decay(model, callbacks, lr=0.001):
    """ create custom decay that does not do anything """
    def scheduler(epoch, lr):
        return lr 

    callbacks.append(tf.keras.callbacks.LearningRateScheduler(scheduler))

    # compile model
    model.compile()
    
    return model, callbacks 
```

Feel free to use any decay rates as well as a step size of your choice for the stepwise scheduler.

You can run `python training.py` to see the effect of different annealing strategies on your training and model performances. Make sure to feed in the GTSRB dataset as the image directory, and use the Desktop to view the visualization of final training metrics.

## Tips

You can find pre-implemented schedulers (Keras naming convention for learning rate annealing strategies) 
[here](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules).
