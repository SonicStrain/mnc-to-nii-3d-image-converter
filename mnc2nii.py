import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import shutil

minc = nib.load("data/mncdata/t1.mnc.gz")
basename = minc.get_filename().split(os.extsep, 1)[0]

affine = np.array([[0, 0, 1, 0],
                   [0, 1, 0, 0],
                   [1, 0, 0, 0],
                   [0, 0, 0, 1]])

data = nib.Nifti1Image(minc.get_fdata(), affine=affine)
nib.save(data, basename + '.nii.gz')

img_load = data.get_fdata()

print(img_load.shape)

img = img_load[:,:,150]
plt.imshow(img)
plt.show()


shutil.move("data/mncdata/t1.nii.gz", "data/niidata/t1.nii.gz")

