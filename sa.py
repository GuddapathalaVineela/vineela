'''import package
package.vinni.add()


from package import vinni
vinni.add()

from package.sum import rf
rf.add1()

from package import vinni
from package.sum import vinni as r
vinni.add()
r.add() '''
from package.sum import *
vinni.add()
