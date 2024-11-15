This is the modified code of our team. In order to prevent the code from running wrong after deleting some files and not deleting any baseline files, I will cover what is useful and what is not in each file in this readme
# config
Contains five folders base, inspose,petr,soit,wifi

base:The folder is used to adjust the base Settings such as dataset, where relevant to the project is the base/default_runtime file used to adjust some run hyperparameters, There are also base/dataset/wifi_key_point.py adjusting dataset locations. Other files are public data sets such as coco, crowpose Settings, but baseline does not provide these data sets. It has little to do with the project

The setting of the remaining inspose, petr and soit cited in other literatures has nothing to do with the baseline of our study and the operation of the project
## config/wifi
One of the most important folders that contains the various config files used to configure and tune loss

The most important thing is the four python files under the wifi folder, which are good config files used by the project. Our team ran all of them and finally decided to use MSEloss_64x2_lr_1e_5.py and made modifications based on this file. Because this file is the most stable and the results are not bad
