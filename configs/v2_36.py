# imgloss + tmploss + featureloss
import numpy as np
height = 288
width = 512
batch_size = 10
initial_learning_rate = 2e-4
feature_mul = 10 * width
theta_mul = 400
regu_mul = 30
img_mul = height * width * 1
temp_mul = height * width * 10 
black_mul = 300000
id_mul = 10
training_iter = 100000
step_size = 40000
train_data_size = 27000#4000
test_data_size = 2500#600
crop_rate = 1
before_ch = 6
after_ch = 0
tot_ch = before_ch + after_ch + 1
test_batches = 10
random_crop_rate = 0.9
max_crop_rate = 0.6
disp_freq = 100
test_freq = 500
save_freq = 5000
no_theta_iter = 1000000
do_temp_loss_iter = 5000
do_theta_10_iter = -1
do_black_loss_iter = 1000
do_theta_only_iter = 100
tfrecord_item_num = 10
log_dir = 'log/v2_36/'
model_dir = 'models/v2_36/'
data_dir = 'data9_/'
rand_H_max = np.array([[1.1, 0.1, 0.9], [0.1, 1.1, 0.9], [0.1, 0.1, 1]])
rand_H_min = np.array([[0.9, -0.1, -0.9], [-0.1, 0.9, -0.9], [-0.1, -0.1, 1]])
max_matches = 3000
input_mask = True
do_crop_rate = 0.8
indices = [0, 1, 2, 4, 8, 16, 32]
rand_H_change_rate = 0.2
distortion_mul = 250
consistency_mul = 500
grid_h = 9
grid_w = 16
grid_theta_mul = 0#1000
grid_max_move = 1
