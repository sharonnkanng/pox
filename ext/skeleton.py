# Copyright 2013 <Your Name Here>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A skeleton POX component

You can customize this to do whatever you like.  Don't forget to
adjust the Copyright above, and to delete the Apache license if you
don't want to release under Apache (but consider doing so!).

Rename this file to whatever you like, .e.g., mycomponent.py.  You can
then invoke it with "./pox.py mycomponent" if you leave it in the
ext/ directory.

Implement a launch() function (as shown below) which accepts commandline
arguments and starts off your component (e.g., by listening to events).

Edit this docstring and your launch function's docstring.  These will
show up when used with the help component ("./pox.py help --mycomponent").
"""

# Import some POX stuff
from pox.core import core                     # Main POX object
import pox.openflow.libopenflow_01 as of      # OpenFlow 1.0 library
import pox.lib.packet as pkt                  # Packet parsing/construction
from pox.lib.addresses import EthAddr, IPAddr # Address types
import pox.lib.util as poxutil                # Various util functions
import pox.lib.revent as revent               # Event library
import pox.lib.recoco as recoco               # Multitasking library
from pox.lib.recoco import TestTask, Sleep    # Classes for testing
import datetime

# Create a logger for this component
log = core.getLogger()


def _go_up (event):
  # Event handler called when POX goes into up state
  # (we actually listen to the event in launch() below)
  log.info("Skeleton application ready (to do nothing).")
  # test1()
  # test2()
  # test3()
  # test4()
  # test5()
  # test6()
  # test7()
  # test8()
  # test9()
  # test10()


# A single, high priority task
def test1 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, True)
  t0.start()

# A single, mid priority task
def test2 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, True)
  t0.start(priority=.5)

# A single, low priority task
def test3 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, True)
  t0.start(priority=.01)

# Many, high priority tasks
def test4 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, False)
  t1 = TestTask(0, 4, dt, False)
  t2 = TestTask(0, 4, dt, False)
  t3 = TestTask(0, 4, dt, True)
  t0.start(priority=.9)
  t1.start(priority=.85)
  t2.start()
  t3.start(priority=.95)

# Many, mid priority tasks
def test5 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, False)
  t1 = TestTask(0, 4, dt, False)
  t2 = TestTask(0, 4, dt, False)
  t3 = TestTask(0, 4, dt, True)
  t0.start(priority=.55)
  t1.start(priority=.5)
  t2.start(priority=.45)
  t3.start(priority=.4)

# Many, low priority tasks
def test6 ():
  dt = datetime.datetime.now()
  t0 = TestTask(0, 4, dt, False)
  t1 = TestTask(0, 4, dt, False)
  t2 = TestTask(0, 4, dt, False)
  t3 = TestTask(0, 4, dt, True)
  t0.start(priority=.1)
  t1.start(priority=.05)
  t2.start(priority=.01)
  t3.start(priority=.001)

# Add one task to each of the 10 priority-based deques
def test7 ():
  tasks = []
  priority = .95
  for x in range(9):
    dt = datetime.datetime.now()
    tasks.append(TestTask(0, 4, dt, False))
  tasks.append(TestTask(0, 4, dt, True))
  for y in tasks:
    y.start(priority=priority)
    priority -= .1
  
# Add one task to each of the 10 priority-based deques
# Plus additional high priority tasks
def test8 ():
  tasks = []
  morehightasks = []
  for x in range(10):
    dt = datetime.datetime.now()
    tasks.append(TestTask(0, 4, dt, False))
  for x in range(4):
    dt = datetime.datetime.now()
    morehightasks.append(TestTask(0, 4, dt, False))
  morehightasks.append(TestTask(0, 4, dt, True))
  priority = .95
  for y in tasks:
    y.start(priority=priority)
    priority -= .1
  priority = .95
  for y in morehightasks:
    y.start(priority=priority)
    priority -= .01

# Add one task to each of the 10 priority-based deques
# Plus additional mid priority tasks
def test9 ():
  tasks = []
  moremidtasks = []
  for x in range(10):
    dt = datetime.datetime.now()
    tasks.append(TestTask(0, 4, dt, False))
  for x in range(4):
    dt = datetime.datetime.now()
    moremidtasks.append(TestTask(0, 4, dt, False))
  moremidtasks.append(TestTask(0, 4, dt, True))
  priority = .95
  for y in tasks:
    y.start(priority=priority)
    priority -= .1
  priority = .52
  for y in moremidtasks:
    y.start(priority=priority)
    priority -= .01

# Add one task to each of the 10 priority-based deques
# Plus additional low priority tasks
def test10 ():
  tasks = []
  morelowtasks = []
  for x in range(10):
    dt = datetime.datetime.now()
    tasks.append(TestTask(0, 4, dt, False))
  for x in range(4):
    dt = datetime.datetime.now()
    morelowtasks.append(TestTask(0, 4, dt, False))
  morelowtasks.append(TestTask(0, 4, dt, True))
  priority = .95
  for y in tasks:
    y.start(priority=priority)
    priority -= .1
  priority = .06
  for y in morelowtasks:
    y.start(priority=priority)
    priority -= .01


@poxutil.eval_args
def launch (foo, bar = False):
  """
  The default launcher just logs its arguments
  """
  # When your component is specified on the commandline, POX automatically
  # calls this function.

  # Add whatever parameters you want to this.  They will become
  # commandline arguments.  You can specify default values or not.
  # In this example, foo is required and bar is not.  You may also
  # specify a keyword arguments catch-all (e.g., **kwargs).

  # For example, you can execute this component as:
  # ./pox.py skeleton --foo=3 --bar=4

  # Note that arguments passed from the commandline are ordinarily
  # always strings, and it's up to you to validate and convert them.
  # The one exception is if a user specifies the parameter name but no
  # value (e.g., just "--foo").  In this case, it receives the actual
  # Python value True.
  # The @pox.util.eval_args decorator interprets them as if they are
  # Python literals.  Even things like --foo=[1,2,3] behave as expected.
  # Things that don't appear to be Python literals are left as strings.

  # If you want to be able to invoke the component multiple times, add
  # __INSTANCE__=None as the last parameter.  When multiply-invoked, it
  # will be passed a tuple with the following:
  # 1. The number of this instance (0...n-1)
  # 2. The total number of instances for this module
  # 3. True if this is the last instance, False otherwise
  # The last is just a comparison between #1 and #2, but is convenient.

  log.warn("Foo: %s (%s)", foo, type(foo))
  log.warn("Bar: %s (%s)", bar, type(bar))

  core.addListenerByName("UpEvent", _go_up)


def breakfast ():
  """
  Serves a Pythonic breakfast
  """
  # You can invoke other functions from the commandline too.  We call
  # these multiple or alternative launch functions.  To execute this
  # one, you'd do:
  # ./pox.py skeleton:breakfast

  import random
  items = "egg,bacon,sausage,baked beans,tomato".split(',')
  random.shuffle(items)
  breakfast = items[:random.randint(0,len(items))]
  breakfast += ['spam'] * random.randint(0,len(breakfast)+1)
  random.shuffle(breakfast)
  if len(breakfast) == 0: breakfast = ["lobster thermidor aux crevettes"]

  log.warn("Breakfast is served:")
  log.warn("%s and spam", ", ".join(breakfast))
