import torch
from visualization import visualize_scannet_label

data = torch.load("data.pt")
points = data["points"]
preds = data["preds"]
labels = data["labels"]
gt_points = points + torch.Tensor([[0, 150, 0, 0]])
points = torch.cat([points, gt_points], dim=0)
labels = torch.cat([preds, labels], dim=0)

visualize_scannet_label(points[:, 1:] * 0.05, labels)
