// This code may be compiled to make a stand alone exe
// or it can be run from the ROOT command line as:

// root [0] .L cpp_example.cpp  or .L cpp_example.cpp+
// root [1] cpp_example

#include "TApplication.h"
#include "TROOT.h"
#include "TH2F.h"
#include "TF2.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TRandom3.h"
//#include <cstdlib>
//#include <cmath>
//#include <iostream>

using namespace std;
using namespace ROOT::Math;


void cpp_example2(int samples=10000){
  // gStyle->SetOptStat(0);  // turn off default stats box in histograms

  auto tr = new TRandom3();

  auto hist1 = new TH2F("hist1","random gauss 2D;x;y",100,50,150,100,50,150);
  auto fpeak = new TF2("fpeak", "exp(-0.5*((x-[0])*(x-[0])/[1]/[1] + (y-[0])*(y-[0])/[1]/[1]))", 50,150,50,150);
  fpeak->SetParameters(100,6);
  hist1->FillRandom("fpeak",samples);

  auto tc2 = new TCanvas("c2","Canvas2");
  tc2->Divide(2,2);
  tc2->cd(1);
  hist1->Draw("COLZ");

  auto hist2 = (TH2F*) hist1->Clone("hist2");
  hist2->SetTitle("Gauss+offset 2D;x;y");
  for (int i=0; i<samples/3; ++i){
    double xu = tr->Uniform(50,150);
    double yu = tr->Uniform(50,150);
    hist2->Fill(xu,yu);
  }
  tc2->cd(2);
  hist2->Draw("COLZ");

  auto hist3 = (TH2F*) hist1->Clone("hist3");
  hist3->SetTitle("Gauss+offset2 (1/x^{2}) 2D;x;y");
  auto base2 = new TF1("base2","1/x/x",1,10);
  for (int i=0; i<samples*30; ++i){
    double x = base2->GetRandom()*10+40;
    double y = base2->GetRandom()*10+40;
    hist3->Fill(x,y);
  }
  auto pad3 = tc2->cd(3);
  pad3->SetLogz();
  hist3->Draw("COLZ");

  auto hist4 = (TH2F*) hist1->Clone("hist4");
  hist4->SetTitle("Double Gaussian 2D;x;y");
  fpeak->SetParameter(1,20);
  hist4->FillRandom("fpeak",samples/2);
  tc2->cd(4);
  hist4->Draw("COLZ");

  tc2->SaveAs("canvas2d_cpp.png");
}

int main(int argc, char **argv) {
  int nsamples=10000;
  if (argc>1) nsamples=atoi(argv[1]);


  gROOT->SetBatch(true);
  cpp_example2(nsamples);

  return 0;
}