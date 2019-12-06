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




########################
def preview(xds, variable='image', stokes=0, channel=0):
    """
    Preview the selected image component
    
    Parameters
    ----------
    xds : xarray Dataset
        input image dataset
    variable : str
        dataset variable to plot.  Default is image
    stokes : int
        stokes dimension index to plot.  Defualt is 0
    channel : int
        channel dimension index to plot.  Default is 0
        
    Returns
    -------
      Open matplotlib window
    """
    import matplotlib.pyplot as plt
    
    if xds[variable].ndim > 4:
        print("ERROR: expecting 4d image component")
        return
    
    plt.clf()
    thinfactor = np.max(np.array(np.ceil(np.array(xds[variable].shape[:2])/500), dtype=int))
    xds[variable][:,:,0,0].thin(int(thinfactor)).plot.imshow()
    plt.show(block=False)