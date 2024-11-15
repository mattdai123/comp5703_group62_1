import torch
import torch.nn as nn
import torch.nn.functional as F


class ContrastiveLoss(nn.Module):
    def __init__(self, margin=1.0, loss_weight=1.0):
        super().__init__()
        self.margin = margin
        self.loss_weight = loss_weight

    def forward(self, joint_embeddings, non_joint_embeddings, joint_labels):
        positive_distances = []
        negative_distances = []

        num_joints = joint_embeddings.shape[0]

        # Loop over joint pairs for joint-to-joint comparisons
        for i in range(num_joints):
            for j in range(i + 1, num_joints):
                if joint_labels[i] == joint_labels[j]:
                    # Positive comparison (same joint type)
                    dist = F.pairwise_distance(joint_embeddings[i].unsqueeze(0), joint_embeddings[j].unsqueeze(0))
                    positive_distances.append(dist)
                else:
                    # Negative comparison (different joint types)
                    dist = F.pairwise_distance(joint_embeddings[i].unsqueeze(0), joint_embeddings[j].unsqueeze(0))
                    negative_distances.append(dist)

        # Joint-to-Non-Joint comparisons
        joint_to_non_joint_distances = F.pairwise_distance(joint_embeddings[:, None, :], non_joint_embeddings[None, :, :])

        # Calculate losses
        positive_distances = torch.cat(positive_distances) if positive_distances else torch.tensor(0.0)
        negative_distances = torch.cat(negative_distances) if negative_distances else torch.tensor(0.0)

        positive_loss = torch.mean(positive_distances ** 2)  # Minimize positive distances
        negative_loss = torch.mean(F.relu(self.margin - negative_distances) ** 2)  # Maximize negative distances
        joint_to_non_joint_loss = torch.mean(F.relu(self.margin - joint_to_non_joint_distances) ** 2)  # Maximize joint-to-non-joint distances

        return self.loss_weight * (positive_loss + negative_loss + joint_to_non_joint_loss)

# 调用ContrastiveLoss的示例函数
def loss_contrastive(joint_embeddings, non_joint_embeddings, joint_labels, margin=1.0):
    contrastive_loss_fn = ContrastiveLoss(margin=margin)
    return contrastive_loss_fn(joint_embeddings, non_joint_embeddings, joint_labels)
