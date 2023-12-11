import numpy as np
import cv2


class ClipSubstractMean(object):
    def __init__(self, b=104, g=117, r=123):
        self.means = np.array((101.4, 97.7, 90.2))  # B=90.25, G=97.66, R=101.41

    def __call__(self, buffer):
        new_buffer = buffer - self.means
        return new_buffer


class RandomCrop(object):
    """Crop randomly the image in a sample.

    Args:
        output_size (tuple or int): Desired output size. If int, square crop
            is made.
    """

    def __init__(self, output_size=(112, 112)):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size

    def __call__(self, buffer):
        if len(buffer.shape) == 3:
            buffer = np.expand_dims(buffer, axis=0)  # Add batch dimension

        b, h, w, c = buffer.shape
        new_h, new_w = self.output_size

        # Adjust new_h and new_w if they are greater than input image dimensions
        new_h = min(new_h, h)
        new_w = min(new_w, w)

        top = np.random.randint(0, max(1, h - new_h + 1))
        left = np.random.randint(0, max(1, w - new_w + 1))

        new_buffer = np.zeros((b, new_h, new_w, c))
        for i in range(b):
            image = buffer[i, top: top + new_h, left: left + new_w, :]
            new_buffer[i, :, :, :] = image

        return new_buffer.squeeze() if len(buffer.shape) == 3 else new_buffer


class CenterCrop(object):
    """Crop the image in a sample at the center.

    Args:
        output_size (tuple or int): Desired output size. If int, square crop
            is made.
    """

    def __init__(self, output_size=(112, 112)):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size

    def __call__(self, buffer):
        h, w = buffer.shape[1], buffer.shape[2]
        new_h, new_w = self.output_size

        top = int(round(h - new_h) / 2.)
        left = int(round(w - new_w) / 2.)

        new_buffer = np.zeros((buffer.shape[0], new_h, new_w, 3))
        for i in range(buffer.shape[0]):
            image = buffer[i, :, :, :]
            image = image[top: top + new_h, left: left + new_w]
            new_buffer[i, :, :, :] = image

        return new_buffer


class RandomHorizontalFlip(object):
    """Horizontally flip the given Images randomly with a given probability.

    Args:
        p (float): probability of the image being flipped. Default value is 0.5
    """

    def __call__(self, buffer):
        if np.random.random() < 0.5:
            for i, frame in enumerate(buffer):
                buffer[i] = cv2.flip(frame, flipCode=1)

        return buffer

