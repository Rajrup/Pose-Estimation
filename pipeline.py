import cv2
from module_pose.pose_openpose_tf import PoseOpenpose
from module_pose.pose_recognition_tf import PoseRecognition

input_file = "./images/exercise.avi"
output_file = "./images/exercise_pose.mp4"

in_reader = cv2.VideoCapture(input_file)

frame_height = int(in_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(in_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = in_reader.get(cv2.CAP_PROP_FPS)

out_writer = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

pose = PoseOpenpose()
pose.Setup()

recog = PoseRecognition()
recog.Setup()

output_frames = []
predict_labels = []

frame_id = 1
while True:
  try:
    ret, image = in_reader.read()

    if ret == False:
      break
    
    pose.PreProcess(image)
    pose.Apply()
    humans = pose.PostProcess()
    # print(humans)

    recog.PreProcess(humans)
    recog.Apply()
    predict_label = recog.PostProcess()

    ## OTUPUT ##
    print("Processing %dth image" % frame_id)
    print("Pose: {}".format(predict_label))

    output_frames.append(image)
    predict_labels.append(predict_label)

    frame_id += 1

  except KeyboardInterrupt:
    break

for image, predict_label in zip(output_frames, predict_labels):
  cv2.putText(image, predict_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0, 0, 255), thickness=2)
  out_writer.write(image)

in_reader.release()
out_writer.release()