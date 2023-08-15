import json
import os

from abaqus import *
import abaqus
import abaqusConstants
import amplitude
import animation
import annotationToolset
import assembly
import caePrefsAccess
import customKernel
import deleteObjectCallback
import displayGroupMdbToolset
import fields
import filter
import inpParser
import interaction
import job
import load
import material
import mesh
import meshEdit
import methodCallback
import odbAccess
import odbMaterial
import odbSection
import optimization
import part
import redentABQ
import regionToolset
import section
import sketch
import step
import symbolicConstants
import visualization
# import calibration
# import mdb
# import displayGroupOdbToolset

modules = [
    caePrefsAccess, step, amplitude, animation, annotationToolset, assembly, part, section,
    odbSection, load, abaqus, interaction, customKernel, displayGroupMdbToolset, meshEdit,
    fields, visualization, filter, inpParser, job, material, odbMaterial, mdb, mesh,
    odbAccess, optimization, regionToolset, sketch, redentABQ, symbolicConstants,
    abaqusConstants, methodCallback, deleteObjectCallback
]

# Determine Abaqus version
version = abaqus.version

f_name = 'abaqus_modules_abq{n}.json'.format(n=version)

with open(f_name, 'w') as f:
    attributes = {}
    for module_i in modules:
        name_i = str(module_i.__name__)
        attributes[name_i] = {}
        for att in dir(module_i):
            attributes[name_i][att] = str(type(getattr(module_i, att)))

    json.dump(attributes, f, sort_keys=True, indent=2)
