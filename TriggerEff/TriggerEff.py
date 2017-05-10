from ROOT import *

#Open File
f=TFile("HLTSelection.root")

#book histos
h_pt=TH1F("h_pt","h_pt",80,0,500)

h_probeTriggers=[]
hEff=[]
h_NProbe=[]

#choose TagTrigger
tag="HLT_IsoM18"
h_NTag=TH1F("h_NTag_"+tag,"h_NTag_"+tag,80,0,500)



probeTriggers={"HLT_PFJet40":False,"HLT_PFJet60":False,"HLT_PFJet80":False,"HLT_PFJet140":False,"HLT_PFJet200":False,"HLT_PFJet260":False,"HLT_PFJet320":False,"HLT_PFJet400":False,"HLT_PFJet450":False,"HLT_PFJet500":False}
#book histos
for probetrig in sorted(probeTriggers):
	h=TH1F(probetrig,probetrig,2,0,2)
	h_probeTriggers.append(h)

	h=TH1F("h_eff_"+probetrig,"h_eff_"+probetrig,80,0,500)
	hEff.append(h)

	h=TH1F("h_NProbe_"+probetrig,"h_NProbe_"+probetrig,80,0,500)
	h_NProbe.append(h)



#FitFunction for TurnOn
def eff(x, par): 
  return 0.5*par[2]*(erf(par[0]*(x[0]-par[1]))+1)


#get Tree
tree=f.Get("analysis/TriggerResults")
#get #Entries
n=tree.GetEntries()

#loop over all events
print n, " Events to Analyse"
for i in xrange(n):
  if i%10000==0: print "analyzing event Nr. ", i
  if i >10000: break
  tree.GetEntry(i) 
  h_pt.Fill(tree.JetPt)
  probeTriggers["HLT_PFJet40"]=tree.HLT_PFJet40
  probeTriggers["HLT_PFJet60"]=tree.HLT_PFJet60
  probeTriggers["HLT_PFJet80"]=tree.HLT_PFJet80
  probeTriggers["HLT_PFJet140"]=tree.HLT_PFJet140
  probeTriggers["HLT_PFJet200"]=tree.HLT_PFJet200
  probeTriggers["HLT_PFJet260"]=tree.HLT_PFJet260
  probeTriggers["HLT_PFJet320"]=tree.HLT_PFJet320
  probeTriggers["HLT_PFJet400"]=tree.HLT_PFJet400
  probeTriggers["HLT_PFJet450"]=tree.HLT_PFJet450

  #choose tagTrigger
  tagTrigger=  {"HLT_IsoM18":tree.HLT_IsoMu18}

  #loop over ProbeTriggers
  for i,trig in enumerate(probeTriggers):
  	#count events passing probeTrigger and tagTrigger
  	if(probeTriggers[trig]==1 and tagTrigger[tag]==1):
  		h_NProbe[i].Fill(tree.JetPt)
  	#count events passing tagTrigger
  	if():
  		h_NTag.Fill(tree.JetPt)
 #print and histos
c1=TCanvas()
c1.cd()

h_pt.Draw()
c1.SaveAs("JetPt.png")

c2=TCanvas()
c2.cd()
h_NTag.Draw()
c2.SaveAs("h_NProbe0.png")


raw_input("press enter")