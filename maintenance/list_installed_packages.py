# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python (SurfaceTopography)
#     language: python
#     name: surfacetopography
# ---

print("### IPython.sys_info() ###")
import IPython
print(IPython.sys_info())


import pprint
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print("### pkg_resources.working_set ###")
pprint.pprint(installed_packages_list)
