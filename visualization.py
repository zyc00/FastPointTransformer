import open3d
import open3d.visualization as visual
import matplotlib.pyplot as plt
import numpy as np

SCANNET_COLOR_PALETTE = [
    (174, 199, 232),  # wall
    (152, 223, 138),  # floor
    (31, 119, 180),  # cabinet
    (255, 187, 120),  # bed
    (188, 189, 34),  # chair
    (140, 86, 75),  # sofa
    (255, 152, 150),  # table
    (214, 39, 40),  # door
    (197, 176, 213),  # window
    (148, 103, 189),  # bookshelf
    (196, 156, 148),  # picture
    (23, 190, 207),  # counter
    (247, 182, 210),  # desk
    (219, 219, 141),  # curtain
    (255, 127, 14),  # refrigerator
    (158, 218, 229),  # shower curtain
    (44, 160, 44),  # toilet
    (112, 128, 144),  # sink
    (227, 119, 194),  # bathtub
    (82, 84, 163),  # otherfurn
]

count = 0


def visualize_scannet_label(points, seg_label, color=None):
    pc = open3d.geometry.PointCloud()
    pc.points = open3d.utility.Vector3dVector(points[:, :3])
    if color is None:
        color = np.zeros([seg_label.shape[0], 3])
    else:
        color = color.copy()
    color_palette = np.array(SCANNET_COLOR_PALETTE) / 255.0
    color[seg_label != 255] = color_palette[seg_label[seg_label != 255]]
    pc.colors = open3d.utility.Vector3dVector(color)

    mesh_frame = open3d.geometry.TriangleMesh.create_coordinate_frame(
        size=1.0, origin=[0, 0, 0]
    )
    # open3d.visualization.draw_geometries([pc, mesh_frame])
    vis = open3d.visualization.Visualizer()
    # vis.create_window()
    vis.add_geometry(pc)
    vis.update_geometry(pc)
    vis.poll_events()
    vis.update_renderer()
    global count
    vis.capture_screen_image(f"./vis/{count}.jpg", do_render=False)
    # vis.destroy_window()
    count = count + 1
