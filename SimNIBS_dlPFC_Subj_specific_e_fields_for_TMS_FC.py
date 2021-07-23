import warnings
warnings.filterwarnings('ignore')

import os,sys,glob,numpy as np, pandas as pd

from skimage import measure

import nibabel as nib
from nilearn.plotting import plot_surf, plot_surf_stat_map, plot_roi, plot_anat, plot_surf_roi

from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from nilearn.image import index_img

from dipy.core.gradients import gradient_table
from dipy.tracking import utils
from dipy.tracking.local_tracking import LocalTracking
from dipy.tracking.streamline import Streamlines
from dipy.tracking.stopping_criterion import BinaryStoppingCriterion
from dipy.tracking.distances import approx_polygon_track
from dipy.tracking.utils import length
from dipy.io.dpy import Dpy
from dipy.direction import peaks
from dipy.reconst import shm

# from dipy.align.reslice import reslice
# from dipy.viz import fvtk
# from dipy.viz.colormap import line_colors

# from dipy.tracking.utils import connectivity_matrix

import seaborn as sns

import simnibs
from simnibs import mni2subject_coords
from simnibs import sim_struct, run_simnibs


import scipy
import stl
from scipy import sparse

import networkx as nx

from numpy import sin,cos,pi,kron

import matplotlib as mlt
from mpl_toolkits.mplot3d import Axes3D
import itertools

from scipy.ndimage.morphology import binary_dilation

# %matplotlib inline
surfdist_dir = '/external/rprshnas01/kcni/hharita/Code/surfdist'
assert os.path.isdir(surfdist_dir)
sys.path.append(surfdist_dir)

import surfdist as sd
from surfdist.utils import find_node_match
from surfdist.analysis import dist_calc,dist_calc_matrix
from surfdist import viz, load, utils

import matplotlib as mlt
from mpl_toolkits.mplot3d import Axes3D
import itertools

import time
#___________________________________________________________________________________________________________________________________________

# qbatch --options "-C bigmem" -w 4:00:00 run_subj_e_fields_generator.sh

start_time = time.time()

sub_list = ['151526', '162935', '189349', '191437', '214524', '667056', '680957', '725751', '783462', '872764', '912447', '990366']

simnibs_hcp_dir = '/external/rprshnas01/netdata_kcni/jglab/Data/simnibs/simnibs_hcp'

subj_fields_dir = '/external/rprshnas01/netdata_kcni/jglab/Data/SimNIBs_Shrey_fields_II'

#___________________________________________________________________________________________________________________________________________

for i in range(len(sub_list)):
    
    sub = sub_list[i]
    
    os.makedirs(subj_fields_dir +"/%s_SimNIBS_e_fields_F3_dlPFC" % (sub))

    # Initialize Session
    s = sim_struct.SESSION()

    # Name of Head mesh
    s.fnamehead = simnibs_hcp_dir + '/%s/%s.msh' % (sub, sub)

    #O/P folder
    s.pathfem = subj_fields_dir +"/%s_SimNIBS_e_fields_F3_dlPFC/" % (sub)
# -----------------------------------------------------------------------------------------------------------------------------------------
    # Initialize a list of TMS simulations
    tmslist = s.add_tmslist()
    # Select coil
    tmslist.fnamecoil = 'Magstim_70mm_Fig8.nii.gz'
# -----------------------------------------------------------------------------------------------------------------------------------------
    # Initialize a coil position
    pos = tmslist.add_position()
    # Select coil centre
    pos.centre = 'F3'
    # Select coil handle direction
    pos.pos_ydir = 'AF3' #FC3
# -----------------------------------------------------------------------------------------------------------------------------------------
    # Add another position
    pos_superior = tmslist.add_position()
    # Centred at F3
    pos_superior.centre = 'F3'
    # Select coil handle direction
    pos_superior.pos_ydir = 'F5' #F1

# -----------------------------------------------------------------------------------------------------------------------------------------
    # Initialize a tDCS simulation
#     tdcslist = s.add_tdcslist()
#     # Set currents
#     tdcslist.currents = [-1e-3, 1e-3]
# # -----------------------------------------------------------------------------------------------------------------------------------------
#     # Initialize the cathode
#     cathode = tdcslist.add_electrode()
#     # Connect electrode to first channel (-1e-3 mA, cathode)
#     cathode.channelnr = 1
#     # Electrode dimension
#     cathode.dimensions = [50, 70]
#     # Rectangular shape
#     cathode.shape = 'rect'
#     # 5mm thickness
#     cathode.thickness = 5
#     # Electrode Position
#     cathode.centre = 'F1'
#     # Electrode direction
#     cathode.pos_ydir = 'F5'
# # -----------------------------------------------------------------------------------------------------------------------------------------
#     # Add another electrode
#     anode = tdcslist.add_electrode()
#     # Assign it to the second channel
#     anode.channelnr = 2
#     # Electrode diameter
#     anode.dimensions = [30, 30]
#     # Electrode shape
#     anode.shape = 'ellipse'
#     # 5mm thickness
#     anode.thickness = 5
#     # Electrode position
#     anode.centre = 'F2'
# ----------------------------------------------------------------------------------------------------------------------------------------

    # Map the o/ps on to these various spaces .

    s.map_to_fsavg = True #Fs space

    # s.map_to_surf = True #native space
    # s.map_to_MNI = True # mni space
    # s.map_to_vol = True # T1 space
#___________________________________________________________________________________________________________________________________________

    run_simnibs(s)
#___________________________________________________________________________________________________________________________________________

print("Time taken to complete : --- %s seconds ---" % (time.time() - start_time))
   #___________________________________________________________________________________________________________________________________________
#===========================================================================================================================================




















# -----------------------------------------------------------------------------------------------------------------------------------------