class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = "/home/guest/XieBailian/proj/stark"  # Base directory for saving network checkpoints.
        self.tensorboard_dir = "/home/guest/XieBailian/proj/stark/tensorboard"  # Directory for tensorboard files.
        self.pretrained_networks = (
            "/home/guest/XieBailian/proj/stark/pretrained_networks"
        )
        self.lasot_dir = "/data/LaSOT"
        self.got10k_dir = "/data/GOT-10k/train"
        self.lasot_lmdb_dir = ""
        self.got10k_lmdb_dir = ""
        self.trackingnet_dir = "/data/TrackingNet"
        self.trackingnet_lmdb_dir = ""
        self.coco_dir = "/data/coco"
        self.coco_lmdb_dir = ""
        self.lvis_dir = ""
        self.sbd_dir = ""
        self.imagenet_dir = ""
        self.imagenet_lmdb_dir = ""
        self.imagenetdet_dir = ""
        self.ecssd_dir = ""
        self.hkuis_dir = ""
        self.msra10k_dir = ""
        self.davis_dir = ""
        self.youtubevos_dir = ""
