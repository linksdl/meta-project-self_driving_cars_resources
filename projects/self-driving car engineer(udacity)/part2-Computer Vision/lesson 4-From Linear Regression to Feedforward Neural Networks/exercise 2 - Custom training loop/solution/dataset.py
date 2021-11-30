from tensorflow.keras.preprocessing import image_dataset_from_directory


def get_datasets(imdir):
    train_dataset = image_dataset_from_directory(imdir, 
                                       image_size=(32, 32),
                                       batch_size=64,
                                       validation_split=0.1,
                                       subset='training',
                                       seed=123)
    val_dataset = image_dataset_from_directory(imdir, 
                                        image_size=(32, 32),
                                        batch_size=64,
                                        validation_split=0.1,
                                        subset='validation',
                                        seed=123)

    return train_dataset, val_dataset