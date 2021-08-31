# Pose-Estimation

## How to Use

- Clone this repo to your machine ```git clone https://github.com/Rajrup/Pose-Estimation.git```
- Install the python dependencies (see below)
- Download the checkpoints(see below)
- Double check the model paths
- Ready to run ```pipeline.py```

## Checkpoint Preparation

- Find all the models: [Google Drive](https://drive.google.com/drive/folders/1rXR2cjYWJIYWtULXe8tNJseJnlgatdmw?usp=sharing)
- Extract the Tensorflow model files into ```models/``` folder.
  - OpenPose: Path will look this - ```./models/graph/cmu/graph_opt.pbb```
  - PoseRecognition: Path will look this - ```./models/pose_recognition/trained_classifier.pickle```

## Requirements

This code has been tested in ```Python 3.7```.
See ```requirements.txt``` for python packages.

```bash
sudo apt install swig
cd tf_pose/pafprocess
swig -python -c++ pafprocess.i && python setup.py build_ext --inplace
cd ../../
pip install -r requirements.txt
```

## Running Pipeline

- Tensorflow Pipeline:

    ```python
    python pipeline.py
    ```

- Tensorflow Serving Pipeline: TODO

## Components

One module's output will go to the next one

- Video Reader
- Pose Estimation ([OpenPose](https://github.com/ZheC/tf-pose-estimation))
- Pose Recognition ([PoseRecognition](https://github.com/felixchenfy/Realtime-Action-Recognition))
