

from roboflow import Roboflow
rf = Roboflow(api_key="1bARVgGsbhM8xIlC4qgw")
project = rf.workspace("agroia").project("pest-detection-ntbss-vcggi")
version = project.version(1)
dataset = version.download("yolov8")
                