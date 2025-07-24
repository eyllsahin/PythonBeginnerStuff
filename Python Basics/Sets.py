'SETS'
cs_courses = {'History','Math','Physics','CompSci'} #it gets rid of duplicates and does not care about order
print(cs_courses)
art_courses = {'History','Math','Physics','CompSci'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_set = set() #you cannot create an empty set with {} just like the others
empty_tuple=()
empty_tuple=tuple()
empty_list=[]
empty_list=list()


