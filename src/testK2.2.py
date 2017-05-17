import sys
import os

modulepath = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(modulepath, "..", "..", "src"))

import sdata.test
import sdata.experiments.ks2
import pandas as pd

def _fixed_uuid():
    fixed_uuids=['60a90898f0c94b23984b174a74a2a47a', '6322a66775604c32af74039575221fe0', '9bec8c67e09b456f96a9e23b04d9441a', 'ea4fa966bedb4104b9754a4f5f5d8a80', 'd061d7a58b2341128dd95412ff6ab36f', 'e4130bc9719e42dd9149e24ab7169398', '8b534e9795624650828be6f39828c153', '82212590f1c2420e8066d9d4e84dbd48', '37f5a429a2a1471d99b342fb95a8d16e', '96a550261de64848b128f982803f2daf', 'e3172927f41c4cfa96f71d76cd59b1e9', 'ba6ea9a119e84e95b304219e009c61a8', 'c161746eef1c4caf9e34f611e9dc4d5d', 'b7dc0d91def94a74ade3767e6a7fc27b', '4253242656e84463807f454b59fcb210', 'de60b7b98bb943ae801f43ccb102d47c', '923e2ef4319e4788a7ed06df7d1940c0', 'cc67e24c09a14d96aace36770d7c7253', 'f81f468b80c2428cae375d4dde321749', 'ea1ba03b578f47839f65a6804e8df1aa', 'f1a62a91b6384c6aa8163f4f2731dc90', '38b1eb86216048238fce60d262eb433c', '9fb394da4a274c7191d549980a3fc5e4', 'f5376c16774e4e8cb3701b54b275663a', '24b4b16be47f4a53ad07c9c3065e4721', '2403e75fb44a45cdae716d807d10a23f', 'a89c49ea00924d19a959d3246d1555b0', '8a17ac6db7f248b8ab48f33e9c68e642', 'ba1e75fac4c54244bdf894c90c5c9433', '7c090410e84747a39230bbfb677feb4b', '71827185aa2b48eea00eca4b29ea360b', 'eaf70185ef52492eb166368dedf8c293', 'e296ecaa56f14b199597dc110e3295df', 'eb885e0e50d047e2b176df6f9537338c', 'd94c000fe9dd4e7cb7b92c2eb88fab58', '4f6a7eb6ec184f828e61cb58bde3ae38', '31bc7501c9554b42b1d537f7b1c3b7c2', '07a670df750649a58c4f3550a4fff568', '85ab8c8694ef40e49d626e768a234323', '5425056193aa4eceae3284e1025be685', '2092edfc1ef442b1b8ccdfa8e3d80942', '60e0a331aae94bc5be69d9554972a2eb', '143bae95ef054e309660f8ac7b821e61', 'e8949cc7d39b4241aa5ddae63392747a', 'efba81a764304b379522a0b04b5c8e51', '70717fcec2fd46169ce645f0ef1e2838', '5a92c55dc9e84eb686dc2c962d21260e', '6730db061a05419e9b2860a215a3d511', 'd8f85fb0b4cd4a858b68621c2a0c2544', '126fffa1dbd54ea58076f152f7b3aa4a', '1b9daeff4ac04bdba483231cfe2f2928', 'a3fd969dd9ca4a4098b83c8a9a1322f0', 'daac5f2b7a1248fc8f3e0aad95eb7a8b', 'ca257d83bb3442d59c9c641ca54ce437', '447f48c0e24848e3bdc58eb4e90eef94', '8d0d4544dc264fbcb18d3954a9707a59', '0dc66d06054d4e65aebd1a7cd7b61f02', '8946db8393be4b7ebb982f1fc6b66b58', '222b02610b564b339cefba9229a6dc69', '9c46d6ff4ce44ae49f169c1b6b4cd136', '87aed4b0d3004593a8f7abd9b5011375', '5836150560d449fa9fb1e6ece43914c1', 'b926c2c318a042c58070d94f3074f9fa', '3cb3cebb0ba242b69c862e4d64c6e594', 'b12d51a756254606b299559b6e115d46', '5c73c9ed582c4aacab8c55ed82af1d5e', '464933693a8f45bdba4460e418044afe', '31f59ead75414a58b235d1fc5c1d8054', '1945ead3bf844c1fb4dc726e4f665ef5', 'cf82de1361b34d90aee21d190cd8fb28', 'e58513ab1516481e91114c4481c9c62a', 'f9b67376adb0469aa5a06723617c64a2', '05b8ca9b26f44a0cb2eaeee860caeabf', 'e649b9a64cbc48859537d2c3449f7095', '0dd448f82cdc427c96c2c940b044a46c', '65e0629b1a7040c4a8443d58ffc1aa3a', '62a4142dd2744a698cda373e7af4ad92', '120eff225b394c88bac9153638ddeda0', '4a48f820e60c432488be68174248cb24', '9dcf98ed8f04481aa4793e6e7303f615', '8beae3f5adb041a4a903d4fe01745345', '42acc26c1afc44669543f9b9b0626366', 'e98c2f050a75438cbe7c520493a00ffe', '2c4da182e2c54ead977e55c8e0e58686', '07ef87f1889c450ab3ed7a29519f0a84', 'dbd8a04eb6794a1b9a66a1e0f53c08b0', '1f6c577dc78e41bd819a69a3e67d0267', '3213a345ec15440b8812b47f94987b38', '024725091cd64a86be390ba649a473ae', '61e34f60c7f848f7aa83b84964fddb4e', '5ea58d41726448df9ab1f09967873b8a', 'e4b8485737574c82b0c0e86aef01f377', '62f7f9738e0141cfb3bf2e8ae10a28a9', 'ad04dc26ea784809aae39d6adc9817f7', '58724a5ba7a64c61a9e9c7c4306f0bf2', '8af74b40b501461296f9412b6904168f', '15c659ba99ae44ea9dfcf65fed76fa0c', 'bd80ad679d954ae18a1bb1cc60097b9a', '0e4f0d796d574173b26a07dcc961c5ea', 'ffa78242021d4951993f2f027bfb2921']
    for uid in fixed_uuids:
        yield uid

fixed_uuid =_fixed_uuid()


def import_ks2_series(file_path):
    """load singe test series"""

    df = pd.read_excel(file_path, sheetname="Daten", header=None, skiprows=3, parse_cols=None, dtypes=float)
    filename = os.path.split(file_path)[1]
    print("filename", filename)
    name = os.path.splitext(filename)[0]
    print("name", name)
    values = name.split("_")
    vsid = values[0]
    specimen = values[1]
    connection = values[2]
    mat1name = values[3]
    t1 = values[4]
    t2 = values[6]
    try:
        t1 = float(t1.replace(",", "."))
        t2 = float(t2.replace(",", "."))
    except ValueError as exp:
        pass
    mat2name = values[5]
    load = values[7]
    if specimen.lower() in ["ks2", "ks-2"]:
        series = sdata.experiments.ks2.KS2_TestSeries(name=name)
        series.metadata.set_attr(name="vsid", value=vsid, description="Test Series ID", unit="-", dtype="str")
        series.metadata.set_attr(name="test_program", value= tpname, description="name of the testprogram", unit="-", dtype="str")
        angle = values[8]
        try:
            angle = float(angle.lower().replace("°","").replace("grad",""))
        except ValueError as exp:
            pass
        direction = values[9]
        cls = sdata.experiments.ks2.KS2_Test

    elif specimen.lower() in ["scherzug"]:
        series = sdata.experiments.lapshear.Lapshear_TestSeries(name=name)
        series.metadata.set_attr(name="vsid", value=vsid, description="Test Series ID", unit="-", dtype="str")
        cls = sdata.experiments.lapshear.Lapshear_Test

    for i, idxs in enumerate([[1, 2], [6, 7], [11, 12], [16, 17], [21, 22]]):

        test = cls(name="{}_{:02d}".format(name, i))
        test.metadata.set_attr(name = "test_program", value= tpname, description= "name of the testprogram", unit = "-", dtype="str")
        test.metadata.set_attr(name="test", value=name, description= "name of the test", unit="-", dtype="str")
        test.metadata.set_attr(name="test_series", value=name, description="name of the testseries", unit="-", dtype="str")
        test.metadata.set_attr(name="vsid", value=vsid, description="Test Series ID", unit="-", dtype="str")
        if test.__class__.__name__.startswith("KS2"):
            test.metadata.set_attr(name="angle", value=angle, description="loading angle", unit="grad", dtype=float)
            test.metadata.set_attr(name="direction", value=direction, description="direction", unit="-", dtype="str")
        test.metadata.set_attr(name="testseries", value=series.uuid, description="Test Series UUID", unit="-", dtype="str")
        test.metadata.set_attr(name="specimen", value=specimen, description="name of specimen", unit="-", dtype="str")
        test.metadata.set_attr(name="connection", value=connection, description="connection type", unit="-", dtype="str")
        test.metadata.set_attr(name="mat1name", value= mat1name, description="name of the first material", unit="-", dtype="str")
        test.metadata.set_attr(name="t1", value= t1, description="thickness of the first material", unit="mm",
                               dtype="float")
        test.metadata.set_attr(name="t2", value=t2, description="thickness of the second material", unit="mm",
                               dtype="float")
        test.metadata.set_attr(name="mat2name", value=mat2name, description="name of the second material", unit="-",
                               dtype="str")
        test.metadata.set_attr(name="load", value=load, description="type of the liability, loading speed", unit="-",
                               dtype="str")

        try:
            dfchosen = df[idxs]
            dfchosen.dropna(inplace=True)

        except KeyError as exp:
            print("skip {}".format(idxs))
            continue

        dfchosen.columns = ["s", "F"]
        table = sdata.Table(name="Test_{:02d}".format(i))
        table.metadata.set_attr(name="col s", value="s", description="Displacement", unit="mm", dtype="str")
        table.metadata.set_attr(name="col F", value="F", description="Force", unit="kN", dtype="str")
        table.data = dfchosen
        series.add_data(test)
        test.add_data(table)


    return series

if __name__ == '__main__':
    path = "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/"
            #"Reihe_06_HC340LA_1,5_ENAW6016_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_07_HC340LA_1,5_ENAW6016_3,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_08_HC340LA_2,0_ENAW6016_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_09_HC340LA_2,0_ENAW6016_3,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_11_HC340LA_1,5_AlSi7Mg0,3_3,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_13_HC340LA_1,0_HC340LA_1,5", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_15_HC340LA_1,5_HC340LA_1,5", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_16_HC340LA_1,5_HC340LA_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_17_HC340LA_2,0_HC340LA_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_25_HCT980XD_1,75_ENAW6016_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_26_HCT980XD_1,75_HC340LA_1,5", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_27_22MnB5_1,0_ENAW6016_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_28_22MnB5_1,5_ENAW7021_1,5", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_33_ENAW6016_1,0_HC340LA_1,5", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_35_ENAW6016_1,5_HC340LA_2,0", "/method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_36_ENAW6016_2,0_HC340LA_1,5", "file:///method/fosta/P1032-Einseitig_Zugänglich/1_Ergebnisse/Reihe_40_ENAW6016_1,5_AlSi7Mg0,3_3,0"]
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for index, file_i in enumerate(filenames):
            if file_i.endswith(".xlsx"):
                    files.append(os.path.join(dirpath, file_i))
    tpname = "P1032"
    exportpath = "/tmp/tp_ks"
    if os.path.exists(exportpath):
        sdata.testprogram.TestProgram.clear_folder(exportpath)
    tp = sdata.testprogram.TestProgram.from_folder(exportpath)
    tp.metadata.set_attr(name="P1032-Einseitig_Zugänglich", value=tpname, unit="-", dtype="str")
    # for fil in os.listdir(path):
    #     print(fil)
    #     if fil.endswith(".xlsx"):
    #         files.append(fil)
    # print(files)
    for fil in files:
        print("_" * 80)
        file_path = os.path.join(path, fil)
        if "reihe" in file_path.lower():

            print("load {}".format(file_path))
            series = import_ks2_series(file_path)
            tp.add_series(series)
        else:
            print("skip {}".format(file_path))

    tp.to_folder(exportpath)
    tp.tree_folder(exportpath)
