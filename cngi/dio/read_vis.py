#   Copyright 2019 AUI, Inc. Washington DC, USA
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


#############################################
def read_vis(infile, ddi=0):
    """
  Read zarr format Visibility data from disk to xarray Dataset

  Parameters
  ----------
  infile : str
      input Visibility filename
  ddi : int
      Data Description ID of Visibility data to read. Defaults to 0

  Returns
  -------
  xarray.core.dataset.Dataset
      New xarray Dataset of Visibility data contents
  """
    import os
    from xarray import open_zarr

    infile = os.path.expanduser(infile)
    xds = open_zarr(infile + "/" + str(ddi))
    return xds
