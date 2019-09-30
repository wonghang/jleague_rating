import numpy as np
import copy

__all__ = ['online_brent_rating']

class online_brent_rating:
    def __init__(self,epsilon=1e-5):
        self.epsilon = epsilon

        self.n = 1
        self.orating = np.array([1.],dtype=np.float64)
        self.gc = [0]
        self.tgc = 0
        self.name_map = {}
        self.name_map_inv = [""]
        self.nS = None
        self.ngc = None
        self.ntgc = None

    def __contains__(self,name):
        return name in self.name_map

    def __str__(self):
        if self.nS is None:
            return "<online_brent_rating at 0x%x, #game=%d, #players=%d>" % (id(self),self.tgc,self.n)
        else:
            return "<online_brent_rating at 0x%x, #game=%d, #players=%d, #updating=%d>" % (id(self),self.tgc,self.n,self.ntgc)

    def current(self,log=True):
        if log:
            return np.log(self.orating) - np.log(self.orating[0])
        else:
            return self.orating / self.orating[0]

    def names(self):
        return self.name_map_inv

    def __iter__(self):
        x = self.current()
        for (name,tid) in self.name_map.items():
            yield (name,x[tid])

    def get(self,name):
        try:
            idx = self.name_map[name]
        except KeyError:
            return 0.
        else:
            return np.log(self.orating[idx]) - np.log(self.orating[0])
    __getitem__=get

    def new_name(self,name):
        if self.nS is not None:
            raise ValueError("new name should not be created during updating state")

        try:
            return self.name_map[name]
        except KeyError:
            nid = self.n
            self.n += 1
            self.orating = np.append(self.orating,1.)
            self.gc.append(0)
            self.name_map[name] = nid
            self.name_map_inv.append(name)
            return nid

    def is_update_state(self):
        return self.nS is not None

    def start(self):
        if self.nS is not None:
            raise ValueError("already in updating state")
        self.nS = {}
        self.ngc = copy.copy(self.gc)
        self.ntgc = 0

    def add(self,name1,name2,s):
        if self.nS is None:
            raise ValueError("Please run .start() to enter updating state first")

        idx1 = self.name_map[name1]
        idx2 = self.name_map[name2]

        if s > 0:
            self.nS[(idx1,idx2)] = self.nS.get((idx1,idx2),0.) + 1
        elif s < 0:
            self.nS[(idx2,idx1)] = self.nS.get((idx2,idx1),0.) + 1
        else:
            self.nS[(idx1,idx2)] = self.nS.get((idx1,idx2),0.) + 0.5
            self.nS[(idx2,idx1)] = self.nS.get((idx2,idx1),0.) + 0.5

        self.ngc[idx1] += 1
        self.ngc[idx2] += 1
        self.ntgc += 1

    def commit(self,decay=1.,niter=1000):
        if self.nS is None:
            raise ValueError("Please run .start() to enter updating state and add some data first")

        e = self.epsilon
        cS = self.nS

        n = self.n
        # add dummy player
        for idx in range(1,self.n):
            cS[(idx,0)] = cS.get((idx,0),0.) + 0.5
            cS[(0,idx)] = cS.get((0,idx),0.) + 0.5

        # add diagonal
        for idx in range(self.n):
            cS[(idx,idx)] = 0.3

        x0 = np.ones((n,),dtype=np.float64)
        orating = np.array(self.orating,dtype=np.float64)
        num = np.empty((n,),dtype=np.float64)
        denom = np.empty((n,),dtype=np.float64)
        W = decay*np.array(self.gc)
        while True:
            denom[:] = W/(x0 + orating)
            num[:] = denom*orating

            for (i,j) in cS.keys():
                t = cS[(i,j)]/(x0[i]+x0[j])
                num[i] += t*x0[j]
                denom[j] += t

            x1 = num/denom # equation 17
            if np.max((x1-x0)/x0) < e:
                break
            niter -= 1
            if niter <= 0:
                raise ValueError("Failed to converge")
            (x0,x1) = (x1,x0)

        self.orating = x1
        self.gc = self.ngc
        self.tgc += self.ntgc
        self.nS = None
        self.ngc = None

    def predict(self,n1,n2):
        n1 = self.get(n1)
        n2 = self.get(n2)
        return 1./(1.+np.exp(-(n1-n2)))

if __name__ == "__main__":
    br = online_brent_rating()

    print(br.current())
    br.new_name("A")
    br.new_name("B")
    br.new_name("C")
    print(br.current())
    br.start()
    br.add("A","B",1)
    br.add("B","C",1)
    br.add("A","C",1)
    br.commit()
    print(br.current())
    br.start()
    br.add("A","B",-1)
    br.add("B","C",-1)
    br.add("A","C",-1)
    br.commit()
    print(br.current())
    br.new_name("D")
    br.new_name("E")
    print(br.current())
    print(str(br))
    br.start()
    br.add("D","E",1)
    print(str(br))
    br.commit()
    print(br.current())

    for (name,r) in br:
        print("%s => %g" % (name,r))
    print(br.predict("A","A"))
    print(br.predict("A","B"))
    print(br.predict("A","C"))
    print(br.predict("A","D"))
    print(br.predict("A","E"))
