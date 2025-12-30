import os
import sys
import math
sys.path.insert(0, os.path.expanduser(r"C:\Users\USER\gsas2full\GSAS-II\GSASII"))
import GSASIIscriptable as G2sc
#from GSASII import GSASIIscriptable as G2sc
import math

# GSAS paths and functions
workdir = r"C:\Users\USER\PhD\IAMM PROJECT\BO" # path where project gets saved
datadir = r"C:\Users\USER\PhD\IAMM PROJECT\BO\GSAS Data\HTO_xray" # path of crystal information
folder = "Task_4-21-2025" # saves GSAS GPX files to this folder in workdir

def makedirs(workdir, folder): # function that creates directories for refList and params to be stored in
    folders = [
        f"{workdir}/{folder}/gpx"
    ]
    for i in folders:
        if not os.path.exists(i):
            os.makedirs(i)
            print(f"Directory '{i}' created.")
        else:
            print(f"Directory '{i}' already exists.")


def gsas(X, iteration):
    # Converting X to typical array
    params = X.squeeze().tolist()

    #params = [0.42, 0, 1.04, 0.04]
    # Main loop for GSAS
    filename = str(iteration)
    # change filename to something constant if you dont want to generate a lot of .gpx files
    makedirs(workdir, folder)

    # Create new project
    gpx = G2sc.G2Project(newgpx=f"{workdir}/{folder}/gpx/{filename}.gpx")

    # Adds phase file to project
    gpx.add_phase(os.path.join(datadir, 'HTO_original.cif'),'Ho2Ti2O7',fmthint='CIF')
    which_hkl = r"cleaned_xtal1_110K.hkl"
    gpx.add_single_histogram(os.path.join(datadir,f"which_hkl{str(1)}/" + which_hkl),0,fmthint='HKLF 4') # connecting exp file to phase

    #Change controls
    gpx.data['Controls']['data']['max cyc'] = 0
    gpx.data['Controls']['data']['UsrReject']['MinExt'] = 0.01
    gpx.data['Controls']['data']['UsrReject']['minF/sig'] = 0
    gpx.data['Controls']['data']['UsrReject']['MaxDF/F'] = 100
    gpx.data['Controls']['data']['UsrReject']['MinD'] = 0.1
    gpx.data['Controls']['data']['F**2'] = True
    gpx.data['Controls']['data']

    # Print statements for testing
    # print("Atoms list length:", len(gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"]))
    print("X:", params)
    #print(fixed_param)
    # Set refinement parameters for each atom
        # here they are set to be empty strings in order to ensure there is no refinement parameter
        # other options are F: fractional occupancy, X: atomic position, U: thermal displacement
        # currently keeping them empty as no refinement is being done
    # Original:
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][0][2] = "" # O1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][1][2] = "" # Ti1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][2][2] = "" # Ho1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][3][2] = "" # O2

    # Edit the structure parameters 
        # Corresponding indices : 3 = x, 4 = y, 5 = z, 6 = frac (fractional occupancy), 10 = Uiso (thermal displacement)
        # Data is selected from Latin Hypercube sampling array of arrays if RANDSAMPLE, otherwise from manual input in settings
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][0][3] = params[4] #xO1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][0][6] = 1 #OccO1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][0][10] = params[5] #UO1
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][1][6] = params[0] #OccTi
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][1][10] = params[1] #UTi
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][2][6] = params[2] #OccHo
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][2][10] = params[3] #UHo
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][3][6] = params[6] #OccO2
    gpx.data["Phases"]["Ho2Ti2O7"]["Atoms"][3][10] = params[7] #UO2

    # Phase information
    phase = gpx.phase(0)
    phase.data['Histograms']['HKLF ' + which_hkl]['Extinction'][1] = 'None'
    phase.data['Histograms']['HKLF ' + which_hkl]

    # TODO Check if this is needed? Idk what this is to be honest
    h = gpx.histograms()[0]
    #prms = phase.data['Histograms'][h.name]
    h.set_refinements({'Scale':True})
    
    # Do the refinement
    gpx.save()
    gpx.do_refinements()
    gpx.save()

    # Calculating chi**2 and saving Fobs and Fcalc to arrays
    ref_list = h.data['data'][1]['RefList']
    Fcalc_i = []
    Fobs_i = []
    sumchisq = 0
    N = 0
    for row in ref_list:
        Fcalc_i.append(row[7])
        Fobs_i.append(row[5])
        sumchisq = sumchisq + ((row[5]-row[7])**2)
        N += 1
    chisq = math.sqrt(sumchisq / (N-1))  # take square root instead of dividing by N
    print("chi**2:", chisq)
    iteration += 1
    return chisq, Fobs_i, Fcalc_i, iteration
