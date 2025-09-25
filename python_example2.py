import ROOT as r
import sys

def python_example(samples=10000):
    # Histogram filled with a normal distribution
    #r.gStyle.SetOptStat(0)  # turn off default stats box in histograms
    r.gROOT.SetBatch(True)
    tr = r.TRandom3()

    hist1 = r.TH2F("hist1", "random gauss 2d;x;frequency", 100, 50, 150, 100, 50, 150)
    fpeak = r.TF2("fpeak",
                  "exp(-0.5*((x-[0])*(x-[0])/[1]/[1] + (y-[0])*(y-[0])/[1]/[1]))",
                50,150,50,150)
    fpeak.SetParameters(100,6)
    hist1.FillRandom("fpeak",samples)
    tc1 = r.TCanvas("c1","Canvas1")
    hist1.Draw("COLZ")   # CHANGED: 2D draw option
    tc1.Update()

    tc2 = r.TCanvas("c2","Canvas2")
    tc2.Divide(2,2)  # divide into 2x2 panels
    tc2.cd(1)
    hist1.Draw("COLZ")

    hist2 = hist1.Clone("hist2")
    hist2.SetTitle("Gauss+offset 2D;x;y")
    for i in range(samples//3):
        xu = tr.Uniform(50,150)
        yu = tr.Uniform(50,150)
        hist2.Fill(xu, yu)
    tc2.cd(2)
    hist2.Draw("COLZ")

    hist3 = hist1.Clone("hist3")
    hist3.SetTitle("Gauss+offset2 (1/x^{2}) 2D;x;y")
    base2 = r.TF1("base2","1/x/x",1,10)
    for i in range(samples*30):
        x = base2.GetRandom()*10+40
        y = base2.GetRandom()*10+40
        hist3.Fill(x, y)
    pad3 = tc2.cd(3)
    pad3.SetLogz()    
    hist3.Draw("COLZ")

    hist4 = hist1.Clone("hist4")
    hist4.SetTitle("Double Gaussian 2D;x;y")
    fpeak.SetParameter(1,20)
    hist4.FillRandom("fpeak",samples//2)
    tc2.cd(4)
    hist4.Draw("COLZ")


    tc2.Update()
    tc2.SaveAs("canvas2d_py.png")

    
if __name__ == '__main__':
    samples=10000
    if len(sys.argv)>1: samples=int(sys.argv[1])
    python_example(samples)