"""Detect artificial assay outliers after correcting plate offsets with explicit reference controls."""
from kit import *
TITLE='Control-Anchored Assay Quality Monitoring'
LIVE=False

def plate(seed,anomalies=False):
    rng=np.random.default_rng(seed);offset=rng.normal(0,2,4);x=rng.normal(0,1,(120,4))+offset;y=np.zeros(120,int)
    if anomalies:
        ids=rng.choice(np.arange(20,120),12,replace=False);x[ids,2]+=7;y[ids]=1
    return x,y
def correct(x,control_count=20):
    if not 1<=control_count<len(x):raise ValueError('Valid reference controls required')
    return x-np.median(x[:control_count],axis=0)
def fit(x):
    center=np.median(x,axis=0);scale=1.4826*np.median(abs(x-center),axis=0);return center,np.maximum(scale,1e-6)
def scores(x,center,scale):return np.max(abs((x-center)/scale),axis=1)
def run(d,a):
    train=np.concatenate([correct(plate(a.seed+i)[0])[20:] for i in range(3)]);center,scale=fit(train);validation=correct(plate(a.seed+10)[0])[20:];threshold=float(np.quantile(scores(validation,center,scale),.98));test,y=plate(a.seed+20,True);x=correct(test)[20:];y=y[20:];p=scores(x,center,scale)>threshold
    return dict(test=classification(y,p),always_normal_baseline=classification(y,np.zeros_like(y)),threshold=threshold,validation_normal_wells=len(validation),test_wells=len(y)),dict(center=center,scale=scale,threshold=np.array(threshold),test_corrected=x,test_labels=y)

if __name__=="__main__":main(run)
