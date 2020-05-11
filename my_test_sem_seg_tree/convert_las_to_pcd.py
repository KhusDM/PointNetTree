import laspy
import numpy as np
import pypcd

filename = 'data_las/den.las'
inFile = laspy.file.File(filename, mode='r')
inHeader = laspy.header.HeaderManager(inFile.header, inFile.reader)
points_count = inHeader.count
x_offset, y_offset, z_offset = inHeader.offset
x_scale, y_scale, z_scale = inHeader.scale

print("count: {0}".format(points_count))

points = []
step = 50
for i in range(0, points_count, step):
    point = [inFile.X[i] * x_scale + x_offset, inFile.Y[i] * y_scale + y_offset,
             inFile.Z[i] * z_scale + z_offset]
    points.append(point)

points = np.array(points)
pc = pypcd.make_xyz_point_cloud(points)
pc.save_pcd('forest2_convert.pcd')
