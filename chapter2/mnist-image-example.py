import sys
import keras
from tensorflow.keras.datasets import mnist


def load():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    print('train shape: {}'.format(train_images.shape))
    print('train labels len: {}'.format(len(train_labels)))
    print('test shape: {}'.format(test_images.shape))
    print('test labels len: {}'.format(len(test_labels)))


def main():
    load()
    return


if __name__ == '__main__':
    main()
