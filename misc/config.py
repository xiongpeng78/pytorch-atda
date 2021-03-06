"""Config for ATDA."""

# params for dataset and data loader
data_root = "data"
source_dataset = "MNIST"
target_dataset = "MNIST-M"
dataset_mean_value = 0.5
dataset_std_value = 0.5
dataset_mean = (dataset_mean_value, dataset_mean_value, dataset_mean_value)
dataset_std = (dataset_std_value, dataset_std_value, dataset_std_value)
batch_size = 128
image_size = 28
num_classes = 10

# params for encoder (F)
model_trained = {
    "pretrain": True,
    "domain_adapt": True
}

model_restore = {
    # "F": "snapshots/pretrain-F-final.pt",
    # "F_1": "snapshots/pretrain-F_1-final.pt",
    # "F_2": "snapshots/pretrain-F_2-final.pt",
    # "F_t": "snapshots/pretrain-F_t-final.pt"
    "F": "snapshots/adapt-F-80.pt",
    "F_1": "snapshots/adapt-F_1-80.pt",
    "F_2": "snapshots/adapt-F_2-80.pt",
    "F_t": "snapshots/adapt-F_t-80.pt"
}

# params for classifier(F1, F2, Ft)
dropout_keep = {
    "F_1": 0.5,
    "F_2": 0.5,
    "F_t": 0.2,
}

# params for training network
num_gpu = 1
num_epochs_pre = 5
num_epochs_adapt = 5
num_epochs_k = 100
num_target_init = 5000
num_target_max = 40000
log_step = 100
save_step = 10
manual_seed = None
model_root = "snapshots"
eval_only = False

# params for optimizing models
learning_rate = 1e-4
beta1 = 0.9
beta2 = 0.999
