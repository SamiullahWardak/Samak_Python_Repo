# Specialized collection has following types
# namedueple(), deque, Chainmap, Counter, OrderedDict, defaultdict,
# UserDict, UserList, UserString

# (1) namedtuple() returns a tuple with a named value for each element in the tuple.

from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict

a = namedtuple('thisSemester', 'name, technology, teacher, grade')
#              -tupleName-     -Attributes 1st, 2nd, 3rd, 4th
s = a('Data Science', 'Python', 'Naveed', 'A')
print("s-namedtuple: ", s)
# Via passing a list
v = a._make(['Artificial Intellegence', 'Python', 'Mosa Hodman', 'A'])
print("using list v: ", v)

# (2) deque pronounced as (dick) is an optimised list to perform insertion and deletion easily.

a = ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r', 'S']
d = deque(a)
print("deque d: ", d)
# operations
d.append('python')
print("appended d: ", d)
d.appendleft('Java')
print("appendeleft d: ", d)

# (3) Chainmap is a dictioonary like class for creating a single view of multiple mappings.

a = {1: 'edureka', 2: 'SoloLearn'}
b = {3: 'ML', 4: 'AI'}

a1 = ChainMap(a, b)
print('Chainmaped a1: ', a1)

# (4) Counter is a dictionary subclass for counting hashable objects.

x = [1,11,11,1,2,3,3,2,4,5,4,4,3,6,5,4,4,5,6,66,7,8,9,98,8,8,8,98]
count_of_each = Counter(x)
print('Each element occurred count_of_each:\n', count_of_each)
# Operations of Counter
print("List of its Elements: ", list(count_of_each.elements()))

# (5) OrderedDict is a Dictionary subclass which remembers the order in which they were added.

d = OrderedDict()
d[1] = 'H'
d[2] = 'E'
d[3] = 'W'
d[4] = 'A'
d[5] = 'D'
print("OrderedDict d: ", d)

# (6) DefaultDict is a dictionary subclass which calls a factory function for the missing kiys.
d = defaultdict(int)
d[1] = 'AFG'
d[2] = 'PAK'
print("Missing key in defaultdict d: ", d[3])  # prints 0


# UserDict, UserList, UserString are the wrapper around objects for eisear subclasses.
