# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


wind_dir = 264

for wind_dir in range(260,287,1):
    Connect()    

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1103, 933]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.OrientationAxesVisibility = 0
    renderView1.CenterOfRotation = [427427.5277206513, 6149678.262833696, 4000.0]
    renderView1.StereoType = 0
    renderView1.CameraPosition = [427427.5277206513, 6149678.262833696, 22647.459536353832]
    renderView1.CameraFocalPoint = [427427.5277206513, 6149678.262833696, 4000.0]
    renderView1.CameraParallelScale = 26028.6380742443
    renderView1.Background = [0.32, 0.34, 0.43]

    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------

    # create a new 'PVD Reader'
    hornsrev_254p00_8p00pvd = PVDReader(FileName='/gpfs/projects/swept2/workarea/ARCHER/HORNSREV/hornsrev_'+str(wind_dir)+'p00_8p00_P40_OUTPUT/hornsrev_'+str(wind_dir)+'p00_8p00.pvd')


    for i in range(70,80,10):
        print 'Generating slice: '+str(i)
        # create a new 'Slice'
        slice1 = Slice(Input=hornsrev_254p00_8p00pvd)
        slice1.SliceType = 'Plane'
        slice1.SliceOffsetValues = [0.0]

        # init the 'Plane' selected for 'SliceType'
        slice1.SliceType.Origin = [428200.0, 428200.0, float(i)]
        slice1.SliceType.Normal = [0.0, 0.0, 1.0]

        # create a new 'Clean to Grid'
        cleantoGrid1 = CleantoGrid(Input=slice1)

        # create a new 'Cell Data to Point Data'
        cellDatatoPointData1 = CellDatatoPointData(Input=cleantoGrid1)

        # ----------------------------------------------------------------
        # setup color maps and opacity mapes used in the visualization
        # note: the Get..() functions create a new object, if needed
        # ----------------------------------------------------------------

        # get color transfer function/color map for 'V'
        vLUT = GetColorTransferFunction('V')
        vLUT.RGBPoints = [3.76021692129622, 0.0, 0.0, 0.0, 8.252343303314754, 1.0, 1.0, 1.0]
        vLUT.ColorSpace = 'RGB'
        vLUT.NanColor = [1.0, 0.0, 0.0]
        vLUT.ScalarRangeInitialized = 1.0

        # get opacity transfer function/opacity map for 'V'
        vPWF = GetOpacityTransferFunction('V')
        vPWF.Points = [3.7602169212962195, 0.0, 0.5, 0.0, 8.252343303314754, 1.0, 0.5, 0.0]
        vPWF.ScalarRangeInitialized = 1

        # ----------------------------------------------------------------
        # setup the visualization in view 'renderView1'
        # ----------------------------------------------------------------

        # show data from cellDatatoPointData1
        cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
        # trace defaults for the display properties.
        cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'V']
        cellDatatoPointData1Display.LookupTable = vLUT
        cellDatatoPointData1Display.ScalarOpacityUnitDistance = 541.7746100694166

        Render()

        # save screenshot
        SaveScreenshot('slice_'+str(wind_dir)+'_'+str(i)+'.png')

    Disconnect()
