import tensorflow as tf
from ggutils.gg_verbosity import GGVerbosePrinting

GGPrint = GGVerbosePrinting(2)

tf_major_version = int(tf.__version__.split('.')[0])
GGPrint.print('tf.__version__: {}'.format(tf.__version__))
GGPrint.print('tf_major_version: {}'.format(tf_major_version))
if tf_major_version >= 2:
    GGPrint.print('from tensorflow_addons.image import rotate')
    from tensorflow_addons.image import rotate
elif tf_major_version >= 1 and tf_major_version < 2:
    GGPrint.print('import tensorflow.contrib.image.rotate as rotate')
    from tensorflow.contrib.image import rotate
else:
    raise ImportError('TensorFlow with major version {} is not available for SmallTrain')


